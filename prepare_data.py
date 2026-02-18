# prepare_data.py
import json

# Simple customer support Q&A dataset
training_examples = [
    {
        "prompt": "What is your return policy?",
        "completion": "Our return policy allows returns within 30 days of purchase with original receipt."
    },
    {
        "prompt": "How do I track my order?",
        "completion": "You can track your order by logging into your account and visiting the Orders section."
    },
    {
        "prompt": "Do you offer international shipping?",
        "completion": "Yes, we ship to over 50 countries. International shipping takes 7-14 business days."
    },
    {
        "prompt": "How do I reset my password?",
        "completion": "Click 'Forgot Password' on the login page, enter your email, and follow the reset link."
    },
    {
        "prompt": "Can I change my order after placing it?",
        "completion": "Orders can be modified within 1 hour of placement by contacting our support team."
    },
]

# Write training data
with open("data/train.jsonl", "w") as f:
    for ex in training_examples:
        # MLX expects this format for fine-tuning
        record = {
            "text": "<|user|>\n" + ex['prompt'] + "\n<|assistant|>\n" + ex['completion']
        }
        f.write(json.dumps(record) + "\n")

# Write validation data (subset)
with open("data/valid.jsonl", "w") as f:
    for ex in training_examples[:2]:
        record = {
            "text": "<|user|>\n" + ex['prompt'] + "\n<|assistant|>\n" + ex['completion']
        }
        f.write(json.dumps(record) + "\n")

print("✅ Data prepared successfully")