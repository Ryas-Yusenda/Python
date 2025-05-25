# Folder Link Creator

A simple Python script that creates a junction (symbolic link) to a specified folder using Windows `mklink`.

## Description

This script allows the user to input a folder path and checks if a symbolic link with the same name already exists in the current directory. If it doesn't exist, the script creates a junction link (`/J`) using the Windows `mklink` command. Useful for creating shortcuts to project folders across drives or directories.

## Installation

- Python must be installed. [Get Python](https://www.python.org/downloads/)
- This script is intended to run on **Windows** systems only.

# Quick Start

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Run the script:

   ```bash
    python main.py
   ```

3. Enter the full path of the folder you want to link when prompted.

⚠️ Run the script as an Administrator to allow symbolic link creation.
