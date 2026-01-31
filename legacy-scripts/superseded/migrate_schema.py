"""Run repository schema/constraint setup script safely.

This helper will try to run an existing `setup_constraints.py` if present, using runpy.
It avoids repeating constraint logic across multiple places.
"""
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
setup_file = ROOT / "setup_constraints.py"


def main():
    if setup_file.exists():
        print(f"Found {setup_file}, executing it to apply constraints...")
        runpy.run_path(str(setup_file), run_name="__main__")
    else:
        print("No setup_constraints.py found at repo root. Please add one or update this script.")


if __name__ == "__main__":
    main()
