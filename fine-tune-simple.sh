#!/bin/bash

# Step 1: Download a small base model (Qwen2.5-0.5B is great for testing)
python -c "
from mlx_lm import load
model, tokenizer = load('Qwen/Qwen2.5-0.5B-Instruct')
print('Model downloaded!')
"

# Step 2: Run LoRA fine-tuning
mlx_lm.lora \
  --model Qwen/Qwen2.5-0.5B-Instruct \
  --train \
  --data ./data \
  --iters 100 \
  --batch-size 2 \
  --lora-layers 4 \
  --learning-rate 1e-4 \
  --adapter-path ./adapters \
  --val-batches 2