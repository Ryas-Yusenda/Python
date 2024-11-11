# Steganography With Python

A simple Python script that hiding arbitrary data within images by slightly modifying the colors.

## Description

Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video. The word steganography combines the Greek words steganos, meaning "covered, concealed, or protected," and graphein meaning "writing".

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

3. Edit constants in `constants.py`:

   ```python
   # Constants
   IMAGE_PATH = "image.png"
   OUTPUT_PATH = "output.png"
   DATA = """Hello, World!"""
   ```

4. Double click `main.py` or run in terminal `python main.py`
