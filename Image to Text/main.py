"""Module for extracting and cleaning text from images using EasyOCR."""

import os
import logging
import easyocr
import regex as re
import time


def clean_text(text):
    """Remove all characters except letters and numbers from the input text."""
    return re.sub(r"[^a-zA-Z0-9]+", "", text)


def extract_text_from_image(image_path):
    """Extract and clean text from an image file using EasyOCR.

    Args:
        image_path (str): Path to the image file to process.
    """
    try:
        start_time = time.time()
        reader = easyocr.Reader(["en"])
        result = reader.readtext(image_path)

        for detection in result:
            text = detection[1]
            cleaned_text = clean_text(text)
            print(cleaned_text)

        end_time = time.time()
        process_time = end_time - start_time
        print(f"\nProcessing time: {process_time:.2f} seconds")

    except FileNotFoundError:
        logging.error("Image file not found: %s", image_path)
    except (ValueError, RuntimeError) as e:
        logging.error("Error processing image: %s", str(e))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    INPUT_IMAGE = "image.jpeg"
    extract_text_from_image(INPUT_IMAGE)
    os.system("pause")
