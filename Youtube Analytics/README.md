# YouTube Comment Analyzer

A Python project to download YouTube video comments, process them with tokenization, stopword removal, and stemming (using Indonesian language), and visualize insights through word clouds and word frequency charts.

## Description

This project uses `youtube-comment-downloader` to fetch comments from a specified YouTube video ID. It then processes the comments with NLTK and Sastrawi libraries for natural language processing in Indonesian, including tokenization, stopwords removal, and stemming. The processed text is visualized as a word cloud and word frequency plot, which are saved as image files.

## Installation

- Ensure Python is installed on your system. [Get Python](https://www.python.org/downloads/)
- Install required dependencies:

  ```bash
    pip install youtube-comment-downloader wordcloud matplotlib nltk  Sastrawi pandas
  ```

  ```python
    import nltk
    nltk.download('all')
  ```

# Quick Start

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Run the script:

   ```bash
    python main.py
   ```

3. Enter the YouTube video ID when prompted.

4. The comments, word cloud images, and frequency plots will be saved inside data/<video_id>/ folder.
