#!/usr/bin/env python3
"""
Annals local-bot concurrency + Superstack scrap blackout gate.

Usage:
  python3 scripts/local_bots/concurrency_gate.py check --bot-id enrich
  python3 scripts/local_bots/concurrency_gate.py acquire --bot-id enrich
  python3 scripts/local_bots/concurrency_gate.py release --bot-id enrich
  python3 scripts/local_bots/concurrency_gate.py status

Exit codes:
  0  — ok / acquired / not in blackout
  10 — scrap blackout (calendar window)
  11 — protected scraper process live
  12 — lock busy (another bot holds required lane)
  13 — unknown bot / config error
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parents[2]
SOT = REPO / "data" / "governance" / "platform-local-bots.json"
DEFAULT_LOCK_DIR = Path("/tmp/annals-bot-locks")


def load_sot() -> dict[str, Any]:
    return json.loads(SOT.read_text())


def bot_by_id(sot: dict[str, Any], bot_id: str) -> dict[str, Any] | None:
    for bot in sot.get("bots") or []:
        if bot.get("id") == bot_id:
            return bot
    return None


def lock_dir(sot: dict[str, Any]) -> Path:
    path = Path(sot.get("concurrency", {}).get("lock_dir") or DEFAULT_LOCK_DIR)
    path.mkdir(parents=True, exist_ok=True)
    return path


def now_in_tz(tz_name: str) -> datetime:
    return datetime.now(ZoneInfo(tz_name))


def parse_hhmm(value: str) -> tuple[int, int]:
    h, m = value.split(":")
    return int(h), int(m)


def minutes_since_midnight(dt: datetime) -> int:
    return dt.hour * 60 + dt.minute


def in_blackout_window(sot: dict[str, Any], now: datetime | None = None) -> tuple[bool, str]:
    blackout = sot.get("superstack_blackout") or {}
    tz = blackout.get("timezone") or sot.get("meta", {}).get("timezone") or "America/Port_of_Spain"
    now = now or now_in_tz(tz)
    cur = minutes_since_midnight(now)
    for window in blackout.get("windows") or []:
        start_h, start_m = parse_hhmm(window["start"])
        end_h, end_m = parse_hhmm(window["end"])
        start = start_h * 60 + start_m
        end = end_h * 60 + end_m
        if start <= cur < end:
            return True, f"blackout:{window.get('id')} ({window['start']}-{window['end']} {tz}) protects {window.get('protects')}"
    return False, ""


def scraper_processes_live(sot: dict[str, Any]) -> tuple[bool, str]:
    patterns = (sot.get("superstack_blackout") or {}).get("also_yield_when_process_matches") or []
    if not patterns:
        return False, ""
    try:
        out = subprocess.check_output(["ps", "-ax", "-o", "command="], text=True, stderr=subprocess.DEVNULL)
    except Exception as exc:
        return False, f"ps-unavailable:{exc}"
    for line in out.splitlines():
        # Ignore our own gate / grep noise
        if "concurrency_gate.py" in line or "annals-of-the-world/scripts/local_bots" in line:
            continue
        for pat in patterns:
            if pat in line:
                return True, f"scraper-live:{pat}"
    # Also check launchd "state = running" for protected labels when possible
    for scraper in (sot.get("superstack_blackout") or {}).get("protected_scrapers") or []:
        label = scraper.get("launchd_label")
        if not label:
            continue
        try:
            uid = os.getuid()
            printed = subprocess.check_output(
                ["launchctl", "print", f"gui/{uid}/{label}"],
                text=True,
                stderr=subprocess.DEVNULL,
            )
            if "state = running" in printed:
                # Ignore hung failsafe retry shells that are not actually scraping —
                # still treat launchd "running" as yield to be safe.
                return True, f"launchd-running:{label}"
        except Exception:
            continue
    return False, ""


def lock_path(sot: dict[str, Any], name: str) -> Path:
    return lock_dir(sot) / f"{name}.lock"


def read_lock(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
    except Exception:
        return {"bot_id": "unknown", "pid": None, "stale": True}
    pid = data.get("pid")
    if pid and not _pid_alive(pid):
        try:
            path.unlink(missing_ok=True)
        except Exception:
            pass
        return None
    return data


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def _is_python_script_cmd(cmd: str, script: str) -> bool:
    """True only when a Python interpreter is executing ``script`` (not git/rg/diff noise)."""
    if script not in cmd:
        return False
    # Require an interpreter token before the script name — rejects git/rg/editors
    # whose argv merely lists the path.
    head = cmd[: cmd.find(script)].lower()
    return "python" in head


def max_concurrent_llm(sot: dict[str, Any], bot: dict[str, Any]) -> int:
    """Per-lane LLM concurrency cap from SoT (Ollama / Grok independently)."""
    conc = sot.get("concurrency") or {}
    lane = bot.get("lane") or ""
    if lane == "grok":
        return max(1, int(conc.get("max_concurrent_grok") or 1))
    if lane == "ollama":
        return max(1, int(conc.get("max_concurrent_llm") or 1))
    return 1


def serialize_enrich_vs_significance(sot: dict[str, Any]) -> bool:
    return bool((sot.get("concurrency") or {}).get("serialize_enrich_vs_significance", True))


def _count_ollama_peers(my_id: str) -> tuple[int, str]:
    """Count live Ollama-lane enrich/sig Python processes (excluding self)."""
    peer_needles = [
        ("enrich", "ai_enrich_autonomous.py"),
        ("significance", "backfill_significance.py"),
    ]

    def _is_peer(line: str, peer_id: str, needle: str) -> bool:
        if not _is_python_script_cmd(line, needle):
            return False
        if peer_id == "enrich" and "--model grok" in line:
            return False
        if peer_id == "significance" and "--model grok" in line:
            return False
        # Own dispatch wrapper / child may appear; ignore exact bot-id markers for self.
        if f"--bot-id {my_id}" in line:
            return False
        return True

    my_pid = os.getpid()
    count = 0
    last = ""
    try:
        out = subprocess.check_output(
            ["ps", "-ax", "-o", "pid=,command="], text=True, stderr=subprocess.DEVNULL
        )
    except Exception as exc:
        return 0, f"ps-unavailable:{exc}"
    seen_pids: set[int] = set()
    for line in out.splitlines():
        if "concurrency_gate.py" in line or "dispatch_bot.py" in line:
            continue
        try:
            pid_str, _, cmd = line.strip().partition(" ")
            pid = int(pid_str)
            if pid == my_pid or pid in seen_pids:
                continue
        except ValueError:
            cmd = line
            pid = -1
        for peer_id, needle in peer_needles:
            if _is_peer(cmd, peer_id, needle):
                if pid > 0:
                    seen_pids.add(pid)
                count += 1
                last = peer_id
                break
    return count, last


def _count_grok_peers(my_id: str) -> tuple[int, str]:
    peer_needles = [
        ("enrich-grok", "ai_enrich_autonomous.py"),
        ("significance-grok", "backfill_significance.py"),
        ("edges-grok", "ai_edge_bot.py"),
    ]

    def _is_peer(line: str, peer_id: str, needle: str) -> bool:
        if not _is_python_script_cmd(line, needle):
            return False
        if "ai_enrich_autonomous.py" in line and "--model grok" not in line:
            return False
        if "ai_edge_bot.py" in line and "--extract-only" in line:
            return False
        if "backfill_significance.py" in line and "--model grok" not in line:
            return False
        if f"--bot-id {my_id}" in line:
            return False
        return True

    my_pid = os.getpid()
    count = 0
    last = ""
    try:
        out = subprocess.check_output(
            ["ps", "-ax", "-o", "pid=,command="], text=True, stderr=subprocess.DEVNULL
        )
    except Exception as exc:
        return 0, f"ps-unavailable:{exc}"
    seen_pids: set[int] = set()
    for line in out.splitlines():
        if "concurrency_gate.py" in line or "dispatch_bot.py" in line:
            continue
        try:
            pid_str, _, cmd = line.strip().partition(" ")
            pid = int(pid_str)
            if pid == my_pid or pid in seen_pids:
                continue
        except ValueError:
            cmd = line
            pid = -1
        for peer_id, needle in peer_needles:
            if _is_peer(cmd, peer_id, needle):
                if pid > 0:
                    seen_pids.add(pid)
                count += 1
                last = peer_id
                break
    return count, last


def llm_peer_live(sot: dict[str, Any], bot: dict[str, Any]) -> tuple[bool, str]:
    """True when lane already at max_concurrent_llm / max_concurrent_grok.

    Ollama and Grok lanes are independent. When max_concurrent_llm>1, multiple
    enrich waiters may run in parallel (slot locks still gate).
    """
    lane = bot.get("lane") or ""
    if lane not in ("ollama", "grok"):
        return False, ""
    my_id = bot.get("id") or ""
    cap = max_concurrent_llm(sot, bot)
    if lane == "ollama":
        count, last = _count_ollama_peers(my_id)
        # Optional hard serialize enrich vs significance even when cap>1.
        if serialize_enrich_vs_significance(sot) and count > 0:
            if my_id.startswith("enrich") and last == "significance":
                return True, f"llm-peer-live:significance (serialize)"
            if my_id.startswith("significance") and last.startswith("enrich"):
                return True, f"llm-peer-live:enrich (serialize)"
    else:
        count, last = _count_grok_peers(my_id)
    if count >= cap:
        return True, f"llm-peer-live:{last or 'peer'} ({count}/{cap})"
    return False, ""


def _write_lock(path: Path, bot: dict[str, Any], holder: int) -> None:
    payload = {
        "bot_id": bot["id"],
        "pid": holder,
        "acquired": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "lane": bot.get("lane"),
    }
    fd = os.open(str(path), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    with os.fdopen(fd, "w") as fh:
        json.dump(payload, fh)


def acquire_locks(
    sot: dict[str, Any],
    bot: dict[str, Any],
    wait_seconds: int = 0,
    holder_pid: int | None = None,
) -> tuple[bool, str]:
    locks = list(bot.get("locks") or [])
    peer_busy, peer_reason = llm_peer_live(sot, bot)
    if peer_busy:
        return False, peer_reason
    if not locks:
        return True, "no-locks"
    # Prefer caller/dispatch PID — gate CLI PID dies immediately after acquire.
    holder = int(holder_pid or os.getpid())
    cap = max_concurrent_llm(sot, bot)
    deadline = time.time() + max(0, wait_seconds)
    while True:
        held: list[Path] = []
        acquired_names: list[str] = []
        busy_reason = ""
        try:
            for name in locks:
                # Skip enrich_sig exclusive when SoT allows enrich∥sig within LLM cap.
                if name == "enrich_sig" and not serialize_enrich_vs_significance(sot):
                    continue
                # Slot fan-out for the ollama lock when parallel LLM is enabled.
                if name == "ollama" and cap > 1 and (bot.get("lane") or "") == "ollama":
                    slot_taken = None
                    for i in range(cap):
                        slot_name = f"ollama_slot_{i}"
                        path = lock_path(sot, slot_name)
                        if read_lock(path):
                            continue
                        try:
                            _write_lock(path, bot, holder)
                        except FileExistsError:
                            continue
                        held.append(path)
                        slot_taken = slot_name
                        break
                    if not slot_taken:
                        busy_reason = f"lock-busy:ollama all {cap} slots full"
                        raise RuntimeError(busy_reason)
                    acquired_names.append(slot_taken)
                    continue

                path = lock_path(sot, name)
                existing = read_lock(path)
                if existing:
                    busy_reason = (
                        f"lock-busy:{name} held_by={existing.get('bot_id')} "
                        f"pid={existing.get('pid')}"
                    )
                    raise RuntimeError(busy_reason)
                _write_lock(path, bot, holder)
                held.append(path)
                acquired_names.append(name)
            return True, "acquired:" + ",".join(acquired_names)
        except FileExistsError:
            busy_reason = busy_reason or "lock-race"
        except RuntimeError as exc:
            busy_reason = str(exc)
        # Roll back any partial holds
        for path in held:
            try:
                data = read_lock(path)
                if data and data.get("pid") == holder:
                    path.unlink(missing_ok=True)
            except Exception:
                pass
        if time.time() >= deadline:
            return False, busy_reason or "lock-busy"
        time.sleep(2)


def release_locks(
    sot: dict[str, Any],
    bot: dict[str, Any],
    holder_pid: int | None = None,
) -> None:
    holder = int(holder_pid or os.getpid())
    names = list(bot.get("locks") or [])
    # Also release any ollama_slot_* held by this bot/pid when parallel LLM is on.
    cap = max_concurrent_llm(sot, bot)
    if "ollama" in names and cap > 1:
        names.extend(f"ollama_slot_{i}" for i in range(cap))
    for name in names:
        path = lock_path(sot, name)
        data = read_lock(path)
        if not data:
            continue
        if data.get("bot_id") == bot["id"] or data.get("pid") == holder:
            try:
                path.unlink(missing_ok=True)
            except Exception:
                pass


def check_bot(sot: dict[str, Any], bot: dict[str, Any]) -> tuple[int, str]:
    """
    Gate policy:
      - Calendar blackout when respect_blackout=true
      - Live scraper yield when respect_blackout=true UNLESS bot.lane == ollama
        (Annals LLM on :11434 does not contend with Superstack media scrapers;
         RAM-heavy heavy_scan / network_write still yield.)
      - File locks always enforced
    """
    respect = bot.get("respect_blackout", True)
    lane = bot.get("lane") or ""
    # Ollama lane can opt into process yield via explicit flag; default skip.
    yield_on_process = bot.get(
        "yield_on_scraper_process",
        False if lane == "ollama" else respect,
    )
    if respect:
        blocked, reason = in_blackout_window(sot)
        if blocked:
            return 10, reason
    if yield_on_process:
        live, live_reason = scraper_processes_live(sot)
        if live:
            return 11, live_reason
    peer_busy, peer_reason = llm_peer_live(sot, bot)
    if peer_busy:
        return 12, peer_reason
    # Soft check locks without acquiring
    cap = max_concurrent_llm(sot, bot)
    for name in bot.get("locks") or []:
        if name == "enrich_sig" and not serialize_enrich_vs_significance(sot):
            continue
        if name == "ollama" and cap > 1 and lane == "ollama":
            # Free if any slot is empty
            if any(not read_lock(lock_path(sot, f"ollama_slot_{i}")) for i in range(cap)):
                continue
            return 12, f"lock-busy:ollama all {cap} slots full"
        existing = read_lock(lock_path(sot, name))
        if existing:
            return 12, f"lock-busy:{name} held_by={existing.get('bot_id')}"
    return 0, "ok"


def status_report(sot: dict[str, Any]) -> dict[str, Any]:
    tz = (sot.get("superstack_blackout") or {}).get("timezone") or "America/Port_of_Spain"
    now = now_in_tz(tz)
    blocked, reason = in_blackout_window(sot, now)
    live, live_reason = scraper_processes_live(sot)
    locks = {}
    for path in sorted(lock_dir(sot).glob("*.lock")):
        locks[path.stem] = read_lock(path)
    cutover = (sot.get("meta") or {}).get("appwrite_cutover") or {}
    return {
        "now": now.isoformat(),
        "timezone": tz,
        "in_blackout": blocked,
        "blackout_reason": reason or None,
        "scraper_live": live,
        "scraper_reason": live_reason or None,
        "locks": locks,
        "bots_enabled": [b["id"] for b in sot.get("bots") or [] if (b.get("schedule") or {}).get("enabled", True)],
        "appwrite_cutover": {
            "employ_bots": bool(cutover.get("employ_bots", False)),
            "target": cutover.get("target"),
            "paused_until_employ": cutover.get("paused_until_employ") or [],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Annals local-bot concurrency gate")
    parser.add_argument("action", choices=["check", "acquire", "release", "status"])
    parser.add_argument("--bot-id", default="")
    parser.add_argument("--wait-seconds", type=int, default=0)
    parser.add_argument(
        "--holder-pid",
        type=int,
        default=0,
        help="PID of the long-lived dispatch holder (not this CLI process)",
    )
    args = parser.parse_args()

    sot = load_sot()
    holder_pid = args.holder_pid or None

    if args.action == "status":
        print(json.dumps(status_report(sot), indent=2))
        return 0

    if not args.bot_id:
        print("ERROR: --bot-id required", file=sys.stderr)
        return 13

    bot = bot_by_id(sot, args.bot_id)
    if not bot:
        print(f"ERROR: unknown bot_id={args.bot_id}", file=sys.stderr)
        return 13

    if args.action == "check":
        code, msg = check_bot(sot, bot)
        print(msg)
        return code

    if args.action == "acquire":
        code, msg = check_bot(sot, bot)
        if code != 0:
            print(msg)
            return code
        ok, msg = acquire_locks(
            sot, bot, wait_seconds=args.wait_seconds, holder_pid=holder_pid
        )
        print(msg)
        return 0 if ok else 12

    if args.action == "release":
        release_locks(sot, bot, holder_pid=holder_pid)
        print("released")
        return 0

    return 13


if __name__ == "__main__":
    sys.exit(main())
