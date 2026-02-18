# MLX Fine-Tuning Workflow for Apple Silicon

A complete workflow for fine-tuning language models using the MLX framework on Apple Silicon Macs, optimized for customer support use cases.

## Purpose

This project provides a complete end-to-end workflow for fine-tuning language models using the MLX framework on Apple Silicon Macs. It's specifically designed for customer support applications, enabling you to train models to handle common support queries and interactions.

## Benefits

- **Apple Silicon Optimized**: Leverages the power of Apple's M-series chips for fast training and inference
- **LoRA Fine-tuning**: Efficient fine-tuning approach that requires minimal computational resources
- **Complete Workflow**: From data preparation to deployment in a single repository
- **Self-contained**: All scripts and dependencies are included for easy setup
- **Production Ready**: Includes monitoring and deployment scripts

## Architecture

```
mlx-finetuning/
├── data/                 # Training and validation data files
├── adapters/             # Fine-tuned LoRA adapter weights
├── fused-model/          # Final fused model (after deployment)
├── venv/                 # Virtual environment (gitignored)
├── *.py                  # Python scripts for each step
├── *.sh                  # Shell scripts for execution
├── requirements.txt       # Required Python packages
├── .gitignore            # Git ignore patterns
└── README.md             # This file
```

## How It Works

1. **Data Preparation**: `prepare_data.py` creates training data in the required JSONL format
2. **Fine-tuning**: `fine_tune.py` or `fine-tune-simple.sh` runs LoRA fine-tuning with the customer support dataset
3. **Inference Testing**: `inference.py` tests the fine-tuned model with sample questions
4. **Deployment**: `deploy.sh` fuses the LoRA adapters into the base model for production use

## Files and Their Purpose

### Python Scripts
- **`prepare_data.py`**: Creates training and validation data in MLX format with customer support Q&A
- **`fine_tune.py`**: Runs the LoRA fine-tuning process using MLX
- **`inference.py`**: Tests inference with the fine-tuned model
- **`monitor_usage.py`**: Monitors GPU and memory usage during training

### Shell Scripts
- **`fine-tune-simple.sh`**: Simple one-step fine-tuning script
- **`run_prepare_data.sh`**: Execute data preparation within venv
- **`run_fine_tune.sh`**: Execute fine-tuning within venv
- **`run_inference.sh`**: Execute inference testing within venv
- **`deploy.sh`**: Deploy the final fused model

### Configuration
- **`requirements.txt`**: Python dependencies including MLX and related packages
- **`.gitignore`**: Ignores virtual environment, model weights, and data files

## How to Run

### Prerequisites
- Apple Silicon Mac (M1, M2, M3, etc.)
- Python 3.8 or higher
- Git installed

### Setup
```bash
# Clone the repository
git clone https://github.com/fernandokarnagi/mlxtest.git
cd mlxtest

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Execution Steps

1. **Prepare Data**
   ```bash
   ./run_prepare_data.sh
   # or
   python prepare_data.py
   ```

2. **Fine-tune Model**
   ```bash
   ./run_fine_tune.sh
   # or
   ./fine-tune-simple.sh
   ```

3. **Test Inference**
   ```bash
   ./run_inference.sh
   # or
   python inference.py
   ```

4. **Deploy Model**
   ```bash
   ./deploy.sh
   ```

### Monitoring
```bash
# Monitor GPU usage during training
python monitor_usage.py
```

## Training Details

The workflow uses LoRA (Low-Rank Adaptation) fine-tuning which:
- Requires minimal computational resources
- Preserves the base model while adapting to new tasks
- Allows for efficient model deployment
- Supports quick experimentation and iteration

Training data includes customer support Q&A pairs covering:
- Return policies
- Order tracking
- International shipping
- Password reset
- Order modification

## Deployment

After fine-tuning, the `deploy.sh` script fuses the LoRA adapters into the base model, creating a single, optimized model file that can be used for production inference without requiring the adapter weights.

## Requirements

- Python 3.8+
- Apple Silicon Mac (M1, M2, M3, etc.)
- At least 8GB RAM (16GB recommended)
- Approximately 20GB of free disk space

## License

This project is licensed under the MIT License.