#!/usr/bin/env python3
"""
Install Annals local-bot LaunchAgents from platform-local-bots.json.

Only touches com.annals.* labels. Never modifies com.caricom.* Superstack agents.

Usage:
  python3 scripts/local_bots/install_mac_launch_agents.py
  python3 scripts/local_bots/install_mac_launch_agents.py --dry-run
  python3 scripts/local_bots/install_mac_launch_agents.py --uninstall
"""
from __future__ import annotations

import argparse
import json
import os
import plistlib
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SOT = REPO / "data" / "governance" / "platform-local-bots.json"
LABEL_PREFIX = "com.annals."
AGENTS_DIR = Path.home() / "Library" / "LaunchAgents"
LOG_DIR = Path.home() / "Library" / "Logs" / "annals-bots"
RUN_JOB = REPO / "scripts" / "local_bots" / "run_job.zsh"
SERVER_START = REPO / "scripts" / "local_bot_server_start.sh"


def which_python() -> str:
    venv = REPO / ".venv" / "bin" / "python3"
    if venv.exists():
        return str(venv)
    return sys.executable


def expand_cron_field(field: str, min_v: int, max_v: int) -> list[int] | None:
    """Return list of values, or None if wildcard (caller handles)."""
    if field == "*":
        return None
    values: set[int] = set()
    for part in field.split(","):
        part = part.strip()
        if part.startswith("*/"):
            step = int(part[2:])
            values.update(range(min_v, max_v + 1, step))
            continue
        if "-" in part and "/" in part:
            range_part, step_s = part.split("/", 1)
            a, b = range_part.split("-", 1)
            step = int(step_s)
            values.update(range(int(a), int(b) + 1, step))
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            values.update(range(int(a), int(b) + 1))
            continue
        values.add(int(part))
    return sorted(v for v in values if min_v <= v <= max_v)


def cron_to_calendar(cron: str) -> list[dict]:
    """Convert 5-field cron to launchd StartCalendarInterval dicts (local TZ)."""
    parts = cron.split()
    if len(parts) != 5:
        raise ValueError(f"expected 5-field cron, got: {cron}")
    minutes = expand_cron_field(parts[0], 0, 59) or list(range(0, 60))
    hours = expand_cron_field(parts[1], 0, 23)
    dom = expand_cron_field(parts[2], 1, 31)
    month = expand_cron_field(parts[3], 1, 12)
    dow = expand_cron_field(parts[4], 0, 6)

    # launchd Weekday: 0 = Sunday
    slots: list[dict] = []
    hour_list = hours if hours is not None else list(range(0, 24))
    # Avoid combinatorial explosion for */5 every hour — still fine (12*24=288)
    for h in hour_list:
        for m in minutes:
            slot: dict = {"Hour": h, "Minute": m}
            if dom is not None and len(dom) == 1:
                slot["Day"] = dom[0]
            if month is not None and len(month) == 1:
                slot["Month"] = month[0]
            if dow is not None:
                for d in dow:
                    s = dict(slot)
                    s["Weekday"] = d
                    slots.append(s)
            else:
                slots.append(slot)
    return slots


def base_env() -> dict:
    return {
        "PATH": "/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin",
        "HOME": str(Path.home()),
    }


def plist_for_bot(bot: dict) -> dict:
    bot_id = bot["id"]
    label = (bot.get("launchd") or {}).get("label") or f"{LABEL_PREFIX}{bot_id}"
    log_path = str(LOG_DIR / f"{bot_id}.log")
    env = base_env()

    if bot_id == "bot-server":
        return {
            "Label": label,
            "ProgramArguments": ["/bin/bash", str(SERVER_START)],
            "WorkingDirectory": str(REPO),
            "RunAtLoad": True,
            "KeepAlive": True,
            "ProcessType": "Background",
            "EnvironmentVariables": env,
            "StandardOutPath": log_path,
            "StandardErrorPath": log_path,
        }

    plist: dict = {
        "Label": label,
        "ProgramArguments": ["/bin/zsh", str(RUN_JOB), "--bot-id", bot_id],
        "WorkingDirectory": str(REPO),
        "RunAtLoad": False,
        "ProcessType": "Background",
        "EnvironmentVariables": env,
        "StandardOutPath": log_path,
        "StandardErrorPath": log_path,
    }

    schedule = bot.get("schedule") or {}
    launchd = bot.get("launchd") or {}

    # Aggressive KeepAlive / worker bots: relaunch immediately after each run.
    # ThrottleInterval caps crash/retry meltdown; soft-skips sleep inside dispatch.
    if schedule.get("kind") in ("keepalive", "worker") or launchd.get("KeepAlive"):
        plist["RunAtLoad"] = True
        plist["KeepAlive"] = True
        throttle = int(
            schedule.get("throttle_seconds")
            or launchd.get("ThrottleInterval")
            or 10
        )
        plist["ThrottleInterval"] = max(5, throttle)
        return plist

    cron = schedule.get("cron")
    if not cron:
        raise ValueError(f"bot {bot_id} missing schedule.cron")

    # Prefer StartInterval for simple every-N-minute jobs (Superstack pattern:
    # */2 → StartInterval 120s). Avoids calendar slot explosion and keeps
    # ollama/light/network lanes tight for 24/7 continuous work.
    # Allow sub-minute via schedule.interval_seconds when set.
    parts = cron.split()
    interval_lanes = {"always_on", "light", "ollama", "network_write"}
    if schedule.get("interval_seconds"):
        plist["StartInterval"] = max(15, int(schedule["interval_seconds"]))
        plist["RunAtLoad"] = True
        return plist
    if (
        len(parts) == 5
        and parts[0].startswith("*/")
        and parts[1] == "*"
        and parts[2] == "*"
        and parts[3] == "*"
        and parts[4] == "*"
        and bot.get("lane") in interval_lanes
    ):
        step = int(parts[0][2:])
        # Allow 30s workers via */1 with interval_seconds override; default floor 60.
        plist["StartInterval"] = max(30, step * 60) if step == 1 else max(60, step * 60)
        if step == 1:
            plist["StartInterval"] = 60
        plist["RunAtLoad"] = True
        return plist

    slots = cron_to_calendar(cron)
    if len(slots) == 1:
        plist["StartCalendarInterval"] = slots[0]
    else:
        plist["StartCalendarInterval"] = slots
    return plist


def bootout(label: str) -> None:
    uid = os.getuid()
    target = f"gui/{uid}/{label}"
    subprocess.run(["launchctl", "bootout", target], capture_output=True)


def bootstrap(plist_path: Path) -> None:
    uid = os.getuid()
    domain = f"gui/{uid}"
    subprocess.run(["launchctl", "bootstrap", domain, str(plist_path)], check=False)


def enable(label: str) -> None:
    uid = os.getuid()
    subprocess.run(["launchctl", "enable", f"gui/{uid}/{label}"], check=False)


def uninstall(sot: dict, dry_run: bool) -> None:
    AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    for bot in sot.get("bots") or []:
        label = (bot.get("launchd") or {}).get("label") or f"{LABEL_PREFIX}{bot['id']}"
        if not label.startswith(LABEL_PREFIX):
            print(f"[refuse] refusing to touch non-annals label {label}")
            continue
        path = AGENTS_DIR / f"{label}.plist"
        print(f"[uninstall] {label}")
        if dry_run:
            continue
        bootout(label)
        if path.exists():
            path.unlink()


def install(sot: dict, dry_run: bool) -> None:
    AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    RUN_JOB.chmod(RUN_JOB.stat().st_mode | 0o111)

    for bot in sot.get("bots") or []:
        schedule = bot.get("schedule") or {}
        if not schedule.get("enabled", True) and bot.get("id") != "bot-server":
            print(f"[skip] {bot['id']} disabled")
            continue
        label = (bot.get("launchd") or {}).get("label") or f"{LABEL_PREFIX}{bot['id']}"
        if not label.startswith(LABEL_PREFIX):
            raise SystemExit(f"Refusing non-annals label: {label}")
        # Never write caricom labels
        if label.startswith("com.caricom."):
            raise SystemExit("Refusing to write com.caricom.*")

        plist = plist_for_bot(bot)
        path = AGENTS_DIR / f"{label}.plist"
        slot_count = 1
        sci = plist.get("StartCalendarInterval")
        if isinstance(sci, list):
            slot_count = len(sci)
        print(f"[install] {label}  slots={slot_count}  -> {path}")
        if dry_run:
            continue
        bootout(label)
        with path.open("wb") as fh:
            plistlib.dump(plist, fh)
        bootstrap(path)
        enable(label)

    print("\nDone. Superstack com.caricom.* agents were not modified.")
    print("Status:  bash scripts/local_bots/ctl.sh status")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--uninstall", action="store_true")
    args = parser.parse_args()

    sot = json.loads(SOT.read_text())
    prefix = sot.get("meta", {}).get("label_prefix", LABEL_PREFIX)
    if prefix != LABEL_PREFIX:
        print(f"[warn] SoT label_prefix={prefix} (expected {LABEL_PREFIX})")

    # Safety: refuse if somehow asked to operate outside annals
    never = (sot.get("superstack_blackout") or {}).get("never_touch_labels") or []
    print(f"[safety] never_touch_labels={never}")

    if args.uninstall:
        uninstall(sot, args.dry_run)
    else:
        install(sot, args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
