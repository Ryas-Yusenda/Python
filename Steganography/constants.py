"""
This module contains constants used for steganography operations,
including input and output image file names and the message to hide.
"""

INPUT_IMAGE = "image.png"

OUTPUT_IMAGE = "image_enc.png"

MESSAGE_HIDE = """
[
    {"username": "john_doe", "email": "john.doe@example.com", "password": "Pass123!"},
    {"username": "jane_smith", "email": "jane.smith@example.com", "password": "Secure#456"},
    {"username": "michael_lee", "email": "michael.lee@example.com", "password": "MyPass789*"},
    {"username": "sarah_connor", "email": "sarah.connor@example.com", "password": "SarahC@123"},
    {"username": "emma_brown", "email": "emma.brown@example.com", "password": "Password$2024"},
    {"username": "alex_jones", "email": "alex.jones@example.com", "password": "Alex!Pass2023"},
    {"username": "chris_wang", "email": "chris.wang@example.com", "password": "Chris#Pass321"},
    {"username": "lucy_martin", "email": "lucy.martin@example.com", "password": "Lucy2024$#"},
    {"username": "tom_clark", "email": "tom.clark@example.com", "password": "TomClark!99"},
    {"username": "linda_garcia", "email": "linda.garcia@example.com", "password": "LindaGarcia#77"}
]
"""
