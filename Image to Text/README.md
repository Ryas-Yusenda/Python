# Image to Text Converter

A simple Python script that extracts text from images using EasyOCR library.

## Description

This project uses EasyOCR (Easy Optical Character Recognition) to detect and extract text from images. The extracted text is then processed to keep only alphanumeric characters.

## Installation

- Python installed on your system. [Get Python](https://www.python.org/downloads/)

# Quick Start

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Double click `main.py` or run in terminal `python main.py`

# Note

- Use GPU to speed up the process (Optional) [PyTorch](https://pytorch.org/)

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

# Special Thanks

- [easyocr](https://github.com/JaidedAI/EasyOCR)
