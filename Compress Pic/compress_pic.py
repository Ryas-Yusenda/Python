"""Module for compressing JPEG images using PIL."""

import os
from PIL import Image


def compress_me(file: str, percent: int):
    """Compress a JPEG image to the specified quality percentage.

    Args:
        file (str): Name of the image file to compress
        percent (int): Compression quality (0-100)
    """
    # Get the path of the file
    filepath = os.path.join(os.getcwd(), file)

    # open the image
    picture = Image.open(filepath)
    picture.save(f"Compressed/{file}", "JPEG", optimize=True, quality=percent)
    return


def main():
    """Process and compress all JPEG images in the current working directory."""
    # finds current working dir
    cwd = os.getcwd()

    formats = (".jpg", ".jpeg", ".png")

    # Add this line to get compression quality from user
    print("Best compression quality is 95")
    percent = int(input("Enter compression quality (0-100): "))

    # create folder to save new image
    os.makedirs("Compressed", exist_ok=True)

    # looping through all the files
    # in a current directory
    for file in os.listdir(cwd):

        # If the file format is JPG or JPEG
        if os.path.splitext(file)[1].lower() in formats:
            print("compressing", file)
            compress_me(file, percent)

    print("Done")
    os.system("pause")


# Driver code
if __name__ == "__main__":
    main()
