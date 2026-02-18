#!/bin/bash
# run_fine_tune.sh - Execute fine_tune.py within venv

cd /opt/mlx

# Check if venv exists, create if not
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
fi

source venv/bin/activate
python fine_tune.py