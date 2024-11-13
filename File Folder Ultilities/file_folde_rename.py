"""
This module provides functions to rename files in various formats,
including kebab case, snake case, uppercase, and title case.
"""

import os
import re


def get_extension(filename):
    """Return the file extension of the given filename."""
    return filename.split(".")[-1]


def kebab_case(name):
    """Convert a filename to kebab case."""
    # Menghapus ekstensi terlebih dahulu
    name, extension = os.path.splitext(name)
    # Mengubah karakter non-alfanumerik menjadi spasi
    name = re.sub(r"[^A-Za-z0-9]+", " ", name)
    # Mengubah spasi menjadi strip dan huruf kecil
    kebab_name = re.sub(r"\s+", "-", name).lower()
    # Menambahkan kembali ekstensi jika ada
    return f"{kebab_name}{extension}"


def snake_case(name):
    """Convert a filename to snake case."""
    # Menghapus ekstensi terlebih dahulu
    name, extension = os.path.splitext(name)
    # Mengubah karakter non-alfanumerik menjadi spasi
    name = re.sub(r"[^A-Za-z0-9]+", " ", name)
    # Mengubah spasi menjadi underscore dan huruf kecil
    snake_name = re.sub(r"\s+", "_", name).lower()
    # Menambahkan kembali ekstensi jika ada
    return f"{snake_name}{extension}"


def uppercase(name):
    """Convert a filename to uppercase."""
    # Menghapus ekstensi terlebih dahulu
    name, extension = os.path.splitext(name)
    # Mengubah semua karakter menjadi huruf besar
    upper_name = name.upper()
    # Menambahkan kembali ekstensi jika ada
    return f"{upper_name}{extension}"


def title_case(name):
    """Convert a filename to title case."""
    # Menghapus ekstensi terlebih dahulu
    name, extension = os.path.splitext(name)
    # Mengubah nama menjadi Title Case
    title_name = name.title()
    # Menambahkan kembali ekstensi jika ada
    return f"{title_name}{extension}"


def main():
    """Main function to rename files in the current directory."""
    skip_files = ["README.md", "LICENSE", ".gitignore", "main.py"]
    skip_folders = [".git", ".github"]

    path = os.getcwd()
    filenames = os.listdir(path)

    for filename in filenames:
        if filename in skip_files or (
            os.path.isdir(filename) and filename in skip_folders
        ):
            continue

        # os.rename(filename, kebab_case(filename))
        # os.rename(filename, snake_case(filename))
        os.rename(filename, uppercase(filename))
        # os.rename(filename, title_case(filename))


if __name__ == "__main__":
    main()
