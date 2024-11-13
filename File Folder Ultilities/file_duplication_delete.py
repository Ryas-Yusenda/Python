"""
Find duplicate files in a specified folder based on their MD5 hash values.
"""

import os
import hashlib
from send2trash import send2trash

# File Folder Ultilities


def hash_file(filename):
    """
    Computes the MD5 hash of a file.

    Args:
        filename (str): The path to the file to be hashed.

    Returns:
        str: The MD5 hash of the file as a hexadecimal string.
    """
    h = hashlib.md5()
    with open(filename, "rb") as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()


def find_duplicates(folder, delete=False):
    """
    Finds and prints duplicate files in the given folder based on their hash values.

    Args:
        folder (str): The path to the folder where the search for duplicate files will be performed.

    Returns:
        None
    """
    hashes = {}
    for dirpath, _, filenames in os.walk(folder):
        for f in filenames:
            full_path = os.path.join(dirpath, f)
            file_hash = hash_file(full_path)
            if file_hash in hashes:
                if delete:
                    send2trash(full_path)
                    print(f"Deleted: {full_path}")
                else:
                    print(f"Duplicate found: {full_path} == {hashes[file_hash]}")
            else:
                hashes[file_hash] = full_path


PATH = str(input("Enter the path to the folder: "))
DELETE_FILES = str(input("Do you want to delete the duplicate files? (y/n): "))

if DELETE_FILES.lower() == "y":
    find_duplicates(PATH, True)
else:
    find_duplicates(PATH)
