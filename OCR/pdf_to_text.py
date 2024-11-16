import os
import shutil
from pdf2image import convert_from_path
from paddleocr import PaddleOCR


def pdf_to_jpg(pdf_path):
    temp_folder = os.makedirs("temp", exist_ok=True)
    images = convert_from_path(
        pdf_path,
        output_folder=temp_folder,
        poppler_path="C:\\laragon\\bin\poppler\\poppler-24.08.0\\Library\\bin",
    )

    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save("temp/page" + str(i) + ".jpg", "JPEG")

    # list of path all images
    return [os.path.join("temp", image) for image in os.listdir("temp")]


def pdf_to_text(pdf_path, use_gpu=False):
    images = pdf_to_jpg(pdf_path)

    # Ensure PaddleOCR uses GPU
    ocr = PaddleOCR(use_gpu=use_gpu, use_space_char=True, lang="en")
    text = ""
    for image in images:
        result = ocr.ocr(image, cls=False)
        for line in result:
            for word in line:
                text += word[1][0] + " "
            text += "\n"
    # remove temp folder
    shutil.rmtree("temp")

    return text


if __name__ == "__main__":
    pdf_path = "sample.pdf"
    USE_GPU = True

    text = pdf_to_text(pdf_path, use_gpu=USE_GPU)
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)
