# YouTube Subtitle

A simple Python script that extracts the subtitle from a YouTube video.

## Description

This project uses `youtube-transcript-api` to extract the subtitle from a YouTube video.

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

3. Download the model from [Hugging Face](https://huggingface.co/openai/whisper-large-v3-turbo)

   ```bash
   ct2-transformers-converter --model openai/whisper-large-v3-turbo --output_dir whisper-large-v3-turbo-ct2 --copy_files tokenizer.json preprocessor_config.json --quantization float16
   ```

4. Run the script:

   ```bash
   python main.py
   ```

# Special Thanks

- [Hugging Face](https://huggingface.co/)
- [Faster Whisper](https://github.com/guoyww/faster-whisper)
