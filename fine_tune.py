#!/usr/bin/env python3
"""
Fine-tuning script for MLX LLMs
This script demonstrates how to fine-tune a model using LoRA adaptation
"""

import subprocess
import sys

def run_finetune(
    model_name="Qwen/Qwen2.5-0.5B-Instruct",
    data_dir="./data",
    adapter_path="./adapters",
    iters=100,
    batch_size=2,
    lora_layers=4,
    learning_rate=1e-4,
):
    """Run MLX LoRA fine-tuning"""
    
    cmd = [
        sys.executable, "-m", "mlx_lm.lora",
        "--model", model_name,
        "--train",
        "--data", data_dir,
        "--iters", str(iters),
        "--batch-size", str(batch_size),
        "--lora-layers", str(lora_layers),
        "--learning-rate", str(learning_rate),
        "--adapter-path", adapter_path,
        "--val-batches", "2",
    ]
    
    print(f"🚀 Starting fine-tune: {model_name}")
    print(f"   Iterations: {iters}, Batch size: {batch_size}")
    print(f"   LoRA layers: {lora_layers}, LR: {learning_rate}")
    print("-" * 50)
    
    result = subprocess.run(cmd, check=True)
    
    if result.returncode == 0:
        print(f"
✅ Fine-tuning complete! Adapters saved to: {adapter_path}")
    
    return adapter_path

if __name__ == "__main__":
    run_finetune()