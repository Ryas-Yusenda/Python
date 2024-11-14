"""
File Organizer Module

This module provides functionality to organize files in a specified folder into subfolders based on file types.
It categorizes files into predefined types such as Archives, Documents, Images, and Videos, and moves them into
corresponding subfolders within the specified folder. Files that do not match any predefined types are moved to
an "_Others" folder. The module also attempts to remove empty subfolders after organizing the files.

Functions:
- organize_folder(folder): Organizes files in the specified folder into subfolders based on file types.

Note:
- System or restricted files like 'desktop.ini' are skipped.
- If a file cannot be moved due to permission issues, it is skipped.
- Empty subfolders are removed, but non-empty directories are left intact.

Example:
    organize_folder("/path/to/folder")
"""

import os
import shutil


def organize_folder(folder):
    """
    Organizes files in the specified folder into subfolders based on file types.
    """
    # output_folder = os.path.join(folder, "output")
    output_folder = folder
    file_types = {
        "Archives": [".zip", ".rar"],
        "Documents": [".docx", ".txt", ".pptx", ".xlsx", ".doc"],
        "Documents/pdf": [".pdf"],
        "Images": [".jpeg", ".jpg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mov"],
    }

    skip_files = ["desktop.ini", "Thumbs.db"]

    # Traverse through all files in folder and subfolders
    for root, dirs, files in os.walk(folder, topdown=False):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Skip system or restricted files like 'desktop.ini'
            if filename.lower() in skip_files:
                print(f"Skipped {filename} (system file)")
                continue

            ext = os.path.splitext(filename)[1].lower()

            # Determine target folder based on file extension
            target_folder = os.path.join(output_folder, "_Others")
            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(output_folder, folder_name)
                    break  # Exit loop once the correct folder is found

            # Create target folder if it doesn't exist and move file
            try:
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} to {os.path.basename(target_folder)}")
            except PermissionError:
                print(f"Permission denied for {filename}, skipping file.")

        # Remove empty subfolders or use rmtree for non-empty directories
        for dir_name in dirs:
            subfolder_path = os.path.join(root, dir_name)
            if os.path.isdir(subfolder_path):
                try:
                    os.rmdir(subfolder_path)  # Try to remove empty subfolders
                    print(f"Removed empty folder {subfolder_path}")
                except OSError:
                    print(f"Cannot remove {subfolder_path}, directory not empty.")


# Call the function
organize_folder("path/to/folder")
