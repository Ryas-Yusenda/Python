"""Module for splitting PDF files in the current working directory."""

import os
import PyPDF2
from pylovepdf.ilovepdf import ILovePdf
from dotenv import load_dotenv

load_dotenv()
KEY_API = os.getenv("API_KEY")


def get_all_pdf():
    """Read and split PDF files in the current working directory."""
    # Get the current working directory
    cwd = os.getcwd()

    # List all files in the current directory, excluding subfolders
    pdf_files = [
        f
        for f in os.listdir(cwd)
        if f.endswith(".pdf") and os.path.isfile(os.path.join(cwd, f))
    ]

    return pdf_files


def split_pdf(work_folder: str, input_pdf: str, pages_per_split: int):
    """
    Split a PDF file into multiple parts.

    Args:
        input_pdf (str): Path to the input PDF file.
        pages_per_split (int): Number of pages per split file.
    """
    with open(input_pdf, "rb") as infile:
        reader = PyPDF2.PdfReader(infile)
        total_pages = len(reader.pages)

        for i in range(0, total_pages, pages_per_split):
            clean_name = input_pdf.replace(".pdf", "")[:30]

            os.makedirs(work_folder, exist_ok=True)

            writer = PyPDF2.PdfWriter()

            for j in range(i, min(i + pages_per_split, total_pages)):
                writer.add_page(reader.pages[j])
                num_end = j + 1

            num_start = i + 1

            output_filename = f"{work_folder}/{clean_name} ({num_start}-{num_end}).pdf"

            with open(output_filename, "wb") as outfile:
                writer.write(outfile)
            print(f"Created: {output_filename}")


def compress_pdf_ilovepdf(work_folder: str, input_pdf: str):
    """
    Compress a PDF file using iLovePDF API.

    Args:
        input_pdf (str): Path to the input PDF file.
    """
    output_folder = f"{work_folder}/compress"

    ilovepdf = ILovePdf(KEY_API, verify_ssl=True)
    task = ilovepdf.new_task("compress")
    task.add_file(f"{work_folder}/{input_pdf}")
    task.set_output_folder(output_folder)
    task.execute()
    task.download()
    task.delete_current_task()


def main():
    """Execute the PDF splitting and compression process for all PDF files."""
    all_pdf = get_all_pdf()

    for pdf_file in all_pdf:
        print(f"FILE SAAT INI : {pdf_file}\n")

        work_file = pdf_file.replace(".pdf", "")[:30]
        work_folder = f"data/{work_file}"

        page_per_split = int(input("MASUKAN NILAI PDF DI PECAH MENJADI BERAPA: "))
        split_pdf(work_folder, pdf_file, page_per_split)

        for file in os.listdir(work_folder):
            compress_pdf_ilovepdf(work_folder, file)

        print("\n" + "=" * 70 + "\n")

    print("SELESAI")
    os.system("pause")


if __name__ == "__main__":
    main()
