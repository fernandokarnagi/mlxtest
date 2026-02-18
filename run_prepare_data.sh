#!/bin/bash
# run_prepare_data.sh - Execute prepare_data.py within venv

cd /opt/mlx

# Check if venv exists, create if not
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
fi

source venv/bin/activate
python prepare_data.py