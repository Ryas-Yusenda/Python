"""
This module provides functions to encode and decode messages 
within images using steganography techniques.
"""

import os
from PIL import Image
import stepic
from constants import MESSAGE_HIDE, INPUT_IMAGE, OUTPUT_IMAGE


def encode_message(input_image_path, output_image_path, message):
    """
    Encodes a message into an image and saves the result.

    Parameters:
    input_image_path (str): The path to the input image.
    output_image_path (str): The path where the encoded image will be saved.
    message (str): The message to be encoded into the image.
    """
    # Open the image and conversion to RGB mode
    image = Image.open(input_image_path).convert("RGB")

    # Encodes messages intogambar
    encoded_image = stepic.encode(image, message.encode())

    # Save a picture that is enveloped for encoded
    encoded_image.save(output_image_path, "PNG")
    print(f"Pesan berhasil disisipkan dan disimpan sebagai {output_image_path}")


def decode_message(encoded_image_path):
    """
    Decodes a hidden message from an encoded image.

    Parameters:
    encoded_image_path (str): The path to the encoded image from which the message will be extracted.
    """
    # Open the picture that has been inserted the message
    encoded_image = Image.open(encoded_image_path)

    # Decode Message from Image
    message = stepic.decode(encoded_image)

    # Show messages of decoding results
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(message)
    # print("Hidden message:", message)
    os.system("pause")


encode_message(INPUT_IMAGE, OUTPUT_IMAGE, MESSAGE_HIDE)

decode_message(OUTPUT_IMAGE)
