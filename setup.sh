#!/bin/bash
# Project environment setup — finds Python and runs setup.py

PYTHON=""

if command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
elif [ -f ".venv/bin/python" ]; then
    PYTHON=".venv/bin/python"
else
    echo "Error: Python not found. Please install Python 3.9+"
    exit 1
fi

echo "Using Python: $PYTHON"
$PYTHON setup.py
