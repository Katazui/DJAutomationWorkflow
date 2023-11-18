import os
import shutil
from datetime import datetime, timedelta

# Base path of your DJ Pool directory
dj_pool_base_path = "/Users/Music/Local DJ Pool/DJ Pool"

# Folders to check for files
source_folders = [
    "/Users/Music/Local DJ Pool/Output_DJCity",
    "/Users/Music/Local DJ Pool/Output_ExportMP3",
    "/Users/Music/Local DJ Pool/Output_Platinum_Notes"
]

# Path to the Downloads folder
downloads_folder = "/Users/haleakala/Downloads"

# Function to move files to the specified folder
def move_files_to_folder(target_folder):
    # Move files from source folders to target folder
    for source_folder in source_folders:
        for filename in os.listdir(source_folder):
            file_path = os.path.join(source_folder, filename)
            if os.path.isfile(file_path):
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} to {target_folder}")

    # Create a 'Converted' subfolder in the target folder
    converted_folder = os.path.join(target_folder, "converted")
    if not os.path.exists(converted_folder):
        os.makedirs(converted_folder)

    # Move .mp3 files from Downloads to the 'Converted' subfolder
    for filename in os.listdir(downloads_folder):
        if filename.endswith('.mp3') or filename.endswith('.MP3') or filename.endswith('.m4a') or filename.endswith('.M4A') or filename.endswith('.wav') or filename.endswith('.WAV') or filename.endswith('.aiff') or filename.endswith('.AIFF') or filename.endswith('.aac') or filename.endswith('.AAC') or filename.endswith('.flac') or filename.endswith('.FLAC'):
            file_path = os.path.join(downloads_folder, filename)
            shutil.move(file_path, os.path.join(converted_folder, filename))
            print(f"Moved: {filename} to {converted_folder}")

# Ask user for the choice
user_choice = input("Do you want to create a new folder? (yes/no): ").strip().lower()

# Logic based on user choice
if user_choice == 'yes':
    now = datetime.now()
    if now.hour < 3:
        now -= timedelta(days=1)
    year = now.strftime("%Y")
    month = now.strftime("%Y-%m")
    date_folder = now.strftime("%Y-%m-%d")
    year_path = os.path.join(dj_pool_base_path, year)
    month_path = os.path.join(year_path, month)
    date_path = os.path.join(month_path, date_folder)
    for path in [year_path, month_path, date_path]:
        if not os.path.exists(path):
            os.makedirs(path)
    move_files_to_folder(date_path)
elif user_choice == 'no':
    # Find the latest folder
    latest_year = sorted([d for d in os.listdir(dj_pool_base_path) if os.path.isdir(os.path.join(dj_pool_base_path, d)) and d.isdigit()], reverse=True)[0]
    latest_month = sorted([d for d in os.listdir(os.path.join(dj_pool_base_path, latest_year)) if os.path.isdir(os.path.join(dj_pool_base_path, latest_year, d))], reverse=True)[0]
    latest_day = sorted([d for d in os.listdir(os.path.join(dj_pool_base_path, latest_year, latest_month)) if os.path.isdir(os.path.join(dj_pool_base_path, latest_year, latest_month, d))], reverse=True)[0]
    latest_folder = os.path.join(dj_pool_base_path, latest_year, latest_month, latest_day)
    move_files_to_folder(latest_folder)
else:
    print("Invalid input. Exiting.")
