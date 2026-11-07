#!/usr/bin/env python3
"""
Dispatch one Annals local bot by id from platform-local-bots.json.

Applies Superstack scrap blackout + lane locks, then runs the bot command.
Intended as the launchd ProgramArguments entry (via run_job.zsh).

Usage:
  python3 scripts/local_bots/dispatch_bot.py --bot-id enrich
  python3 scripts/local_bots/dispatch_bot.py --bot-id sync --force
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SOT = REPO / "data" / "governance" / "platform-local-bots.json"
GATE = REPO / "scripts" / "local_bots" / "concurrency_gate.py"
ENV_EXPAND = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)(?::-([^}]*))?\}")


def expand_arg(value: str) -> str:
    def repl(match: re.Match[str]) -> str:
        key = match.group(1)
        default = match.group(2) if match.group(2) is not None else ""
        return os.environ.get(key, default)

    return ENV_EXPAND.sub(repl, value)


def load_dotenv() -> None:
    env_path = REPO / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export ") :]
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key and key not in os.environ:
            os.environ[key] = value


def load_shared_env() -> None:
    shared = Path.home() / ".config" / "annals" / "env"
    if not shared.exists():
        return
    for line in shared.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key and key not in os.environ:
            os.environ[key] = value


def gate(action: str, bot_id: str) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(GATE), action, "--bot-id", bot_id],
        cwd=str(REPO),
        capture_output=True,
        text=True,
    )
    msg = (proc.stdout or proc.stderr or "").strip()
    return proc.returncode, msg


def build_command(bot: dict) -> list[str]:
    script = bot.get("script") or ""
    script_path = REPO / script
    args = [expand_arg(a) for a in (bot.get("args") or [])]
    runner = bot.get("runner")

    if script.endswith(".sh"):
        return ["bash", str(script_path), *args]

    if runner == "npx_tsx" or script.endswith(".ts"):
        return ["npx", "tsx", str(script_path), *args]

    module = bot.get("module")
    if module:
        return [sys.executable, "-m", module, *args]

    if script.endswith(".py"):
        return [sys.executable, str(script_path), *args]

    raise SystemExit(f"Unsupported script type for bot {bot.get('id')}: {script}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bot-id", required=True)
    parser.add_argument("--force", action="store_true", help="Skip blackout/lock checks (ops only)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    load_shared_env()
    load_dotenv()

    # Prefer Homebrew node/python paths on Mini
    homebrew = "/opt/homebrew/bin"
    os.environ["PATH"] = f"{homebrew}:{Path.home() / '.local' / 'bin'}:{os.environ.get('PATH', '')}"

    sot = json.loads(SOT.read_text())
    bot = next((b for b in sot.get("bots") or [] if b.get("id") == args.bot_id), None)
    if not bot:
        print(f"[dispatch] unknown bot_id={args.bot_id}", file=sys.stderr)
        return 13

    cutover = (sot.get("meta") or {}).get("appwrite_cutover") or {}
    paused_until = set(cutover.get("paused_until_employ") or [])
    if (
        not cutover.get("employ_bots", True)
        and args.bot_id in paused_until
        and not args.force
    ):
        print(
            f"[dispatch] bot {args.bot_id} frozen until local Appwrite cutover "
            f"(meta.appwrite_cutover.employ_bots=true) — skip"
        )
        return 0

    if bot.get("status") == "paused" and not args.force:
        if (bot.get("schedule") or {}).get("kind") != "keepalive":
            print(f"[dispatch] bot {args.bot_id} status=paused — skip")
            return 0

    if not (bot.get("schedule") or {}).get("enabled", True) and bot.get("id") != "bot-server":
        # Keepalive bots still run; disabled cron bots skip
        if (bot.get("schedule") or {}).get("kind") != "keepalive":
            print(f"[dispatch] bot {args.bot_id} disabled in SoT — skip")
            return 0

    # always_on bot-server is started via its own LaunchAgent KeepAlive, not this dispatcher
    if bot.get("id") == "bot-server":
        print("[dispatch] bot-server is KeepAlive — use its LaunchAgent, not dispatch")
        return 0

    if not args.force:
        code, msg = gate("acquire", args.bot_id)
        if code != 0:
            print(f"[dispatch] skip {args.bot_id}: {msg} (exit {code})")
            return 0  # soft skip — not a launchd failure storm

    cmd = build_command(bot)
    print(f"[dispatch] start {args.bot_id}: {shlex.join(cmd)}")
    if args.dry_run:
        if not args.force:
            gate("release", args.bot_id)
        return 0

    started = time.time()
    try:
        proc = subprocess.run(cmd, cwd=str(REPO))
        elapsed = int(time.time() - started)
        print(f"[dispatch] done {args.bot_id} status={proc.returncode} elapsed={elapsed}s")
        return proc.returncode
    finally:
        if not args.force:
            gate("release", args.bot_id)


if __name__ == "__main__":
    sys.exit(main())
