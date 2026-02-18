#!/usr/bin/env python3
"""
Monitor script for Apple Silicon GPU and memory usage
"""

import subprocess
import time

def monitor_gpu_memory():
    """Monitor GPU and memory usage"""
    print("Starting GPU and memory monitoring...")
    print("Press Ctrl+C to stop monitoring")
    
    try:
        # Method 1: Using powermetrics (more detailed)
        print("\nMethod 1: Using powermetrics (detailed GPU monitoring)")
        print("Command: sudo powermetrics --samplers gpu_power -i 1000")
        print("Note: This requires sudo privileges and may need to be run separately")
        
        # Method 2: Using system_profiler (simpler)
        print("\nMethod 2: Using system_profiler (simpler)")
        print("Command: watch -n 1 \"system_profiler SPDisplaysDataType | grep 'Total VRAM'\"")
        print("Note: This command should be run in a separate terminal")
        
        # Alternative: Direct system_profiler command
        print("\nRunning system_profiler command for VRAM info:")
        result = subprocess.run(
            ["system_profiler", "SPDisplaysDataType"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse and display VRAM information
        for line in result.stdout.split('\n'):
            if 'Total VRAM' in line:
                print(f"VRAM Info: {line.strip()}")
                
    except subprocess.CalledProcessError as e:
        print(f"Error running system_profiler: {e}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user")

if __name__ == "__main__":
    monitor_gpu_memory()