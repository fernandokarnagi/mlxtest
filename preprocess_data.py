import pandas as pd
import random
import json

# Load CSV dataset
file_path = '/opt/mlx/data/symptoms_diagnosis.csv'
df = pd.read_csv(file_path)
print(df.head())

# Reformat the csv data into text data
csv_data = []
for _, row in df.iterrows():
    diagnosis = row['label']
    symptoms = row['text']
    prompt = f"You are a medical diagnosis expert. You will give answer to patient's question based on the symptoms they have. Symptoms: '{symptoms}'. Question: 'What is the diagnosis I have?'. Response: You may be diagnosed with {diagnosis}."
    csv_data.append({"text": prompt})

random.shuffle(csv_data)
print("First 10 entries:")
print(csv_data[:10])

# Calculate split indices
total_records = len(csv_data)
train_split = int(total_records * 2 / 3)
test_split = int(total_records * 1 / 6)

print(f"Total records: {total_records}")
print(f"Train split: {train_split}")
print(f"Test split: {test_split}")

# Split the data
train_data = csv_data[:train_split]
test_data = csv_data[train_split:train_split + test_split]
valid_data = csv_data[train_split + test_split:]

# Save the split data to jsonl files
with open('/opt/mlx/data/train.jsonl', 'w') as train_file:
    for entry in train_data:
        train_file.write(json.dumps(entry) + '\n')

with open('/opt/mlx/data/test.jsonl', 'w') as test_file:
    for entry in test_data:
        test_file.write(json.dumps(entry) + '\n')

with open('/opt/mlx/data/valid.jsonl', 'w') as valid_file:
    for entry in valid_data:
        valid_file.write(json.dumps(entry) + '\n')

print("Data files created successfully!")