#!/bin/bash

# Merge LoRA weights permanently into model weights
mlx_lm.fuse \
  --model Qwen/Qwen2.5-0.5B-Instruct \
  --adapter-path ./adapters \
  --save-path ./fused-model

# Run inference from fused model (no adapter overhead)
mlx_lm.generate \
  --model ./fused-model \
  --prompt "What is your return policy?"