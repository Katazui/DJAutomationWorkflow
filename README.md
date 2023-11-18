# DJAutomationWorkflow
Tools to organize your DJ workflow 

### Table of Contents
- [DJ Pool File Organizer](#dj-pool-file-organizer)
   

# DJ Pool File Organizer

This Python script is designed to help DJs organize their music files efficiently. It automatically sorts music files from specified source folders into a structured directory based on the date. Additionally, it offers the option to create new date-based folders or insert files into the latest existing folder. 

## Prerequisites

Before running this script, ensure that you have the following:
- Python installed on your system.
- The music files you want to organize should be in a supported format (e.g., `.mp3`, `.m4a`, `.wav`, etc...).
- Appropriate read and write permissions to the involved directories.

## Setup

1. **Specify Paths**: 
   - Update the `dj_pool_base_path` with the path to your main DJ Pool directory.
   - Update `source_folders` with the paths to the folders containing the files you wish to organize.
   - Set `downloads_folder` to the path of your Downloads folder.

2. **Running the Script**: 
   - Run the script in a Python environment.
   - You will be prompted to choose whether to create a new folder for today's date or use the most recent folder.
   - Based on your choice, the script will move files from the source folders and Downloads folder to the target location.

## Script Functionality

- **File Moving**: Moves files from specified source folders to a target folder organized by date.
- **Folder Creation**: Automatically creates new folders based on the current date, or finds and uses the latest existing folder.
- **User Input**: Prompts the user to either create a new folder or use the latest folder.
- **Subfolder for Converted Files**: Inside the target folder, a subfolder named `converted` is created, where `.mp3` files from the Downloads folder are specifically moved.

## Code Explanation

[Check out the code](/organizeSongsToDJPool.py)

```python
import os
import shutil
from datetime import datetime, timedelta

# Paths for DJ Pool directory, source folders, and Downloads folder
dj_pool_base_path = "/path/to/DJPool"
source_folders = ["path/to/source1", "path/to/source2"]
downloads_folder = "/path/to/Downloads"

# Function to move files to a specified folder
def move_files_to_folder(target_folder):
    # [Code to move files from source folders and Downloads folder]

# User input for folder choice and logic for folder creation and file moving
user_choice = input("Do you want to create a new folder? (yes/no): ")
if user_choice == 'yes':
    # [Code to handle new folder creation and file moving]
elif user_choice == 'no':
    # [Code to find the latest folder and move files there]
else:
    print("Invalid input. Exiting.")
