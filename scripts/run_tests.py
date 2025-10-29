"""
Run all tests in the tests/ directory.
"""
import subprocess

def main():
    print("Running tests...")
    subprocess.run(["pytest", "tests/"])

if __name__ == "__main__":
    main()
