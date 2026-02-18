#!/usr/bin/env python3
"""
Inference script for MLX LLMs
This script demonstrates how to use a fine-tuned model for inference
"""

from mlx_lm import load, generate

def run_inference(
    base_model="Qwen/Qwen2.5-0.5B-Instruct",
    adapter_path="./adapters",
    prompt="What is your return policy?",
    max_tokens=200,
):
    print(f"Loading model with LoRA adapters from: {adapter_path}")
    
    # Load base model + merge LoRA adapters
    model, tokenizer = load(
        base_model,
        adapter_path=adapter_path,  # MLX merges adapters on load
    )
    
    # Format prompt to match training format
    formatted_prompt = f"<|user|>
{prompt}
<|assistant|>
"
    
    print(f"
📝 Prompt: {prompt}")
    print("-" * 40)
    
    # Generate response
    response = generate(
        model,
        tokenizer,
        prompt=formatted_prompt,
        max_tokens=max_tokens,
        verbose=True,  # streams output to terminal
    )
    
    return response

if __name__ == "__main__":
    # Test with training domain questions
    questions = [
        "What is your return policy?",
        "How do I track my order?",
    ]
    
    for q in questions:
        run_inference(prompt=q)
        print("
" + "="*50 + "
")