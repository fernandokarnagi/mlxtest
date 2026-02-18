#!/bin/bash
# run_inference.sh - Execute inference.py within venv

cd /opt/mlx

# Check if venv exists, create if not
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
fi

source venv/bin/activate
python inference.py