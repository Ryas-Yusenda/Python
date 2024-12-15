"""
This module contains constants used for steganography operations,
including input and output image file names and the message to hide.
"""

INPUT_IMAGE = "image.png"

OUTPUT_IMAGE = "image_enc.png"

MESSAGE_HIDE = """
[
    {
        "website": "www.example.com",
        "email": "john.doe@example.com",
        "password": "Pass123!"
    },
    {
        "website": "www.example.com",
        "email": "jane.smith@example.com",
        "password": "Secure#456"
    }
]
"""
