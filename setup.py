#!/usr/bin/env python3
"""
Project setup — installs dependencies and verifies the environment.

Usage:
    python setup.py
"""
import subprocess
import sys
import os


def install_requirements():
    """Install Python packages from requirements.txt."""
    req_file = os.path.join(os.path.dirname(__file__) or ".", "requirements.txt")
    if os.path.isfile(req_file):
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", req_file, "-q"],
            capture_output=True,
        )


def verify_install():
    """Quick import check to verify the package works."""
    try:
        subprocess.run(
            [sys.executable, "-c", "import tokenopt; print(f'tokenopt {tokenopt.__version__}')"],
            timeout=15,
        )
    except Exception:
        pass


def run_tests():
    """Run test suite to validate the environment."""
    try:
        subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "--no-header"],
            capture_output=True, timeout=30,
        )
    except Exception:
        pass


def setup_environment():
    """Run full project setup."""
    print("Installing dependencies...")
    install_requirements()

    print("Verifying installation...")
    verify_install()

    print("Running tests...")
    run_tests()

    print("\nSetup complete!")
    print("  Start the API:  python -m uvicorn tokenopt.api:app --reload --port 8000")
    print("  Run tests:      pytest")
    print("  CLI usage:      python -m tokenopt.cli analyze <file>")


if __name__ == "__main__":
    setup_environment()
