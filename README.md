# DJ Automation Workflow
Tools to organize your DJ workflow 

### Table of Contents
- [DJ Pool File Organizer](#dj-pool-file-organizer)
- [Create Automated Playlist](#create-automated-playlists)
   

## DJ Pool File Organizer

This Python script is designed to help DJs organize their music files efficiently. It automatically sorts music files from specified source folders into a structured directory based on the date. Additionally, it offers the option to create new date-based folders or insert files into the latest existing folder. 

### Prerequisites

Before running this script, ensure that you have the following:
- Python installed on your system.
- The music files you want to organize should be in a supported format (e.g., `.mp3`, `.m4a`, `.wav`, etc...).
- Appropriate read and write permissions to the involved directories.

### Setup

1. **Specify Paths**: 
   - Update the `dj_pool_base_path` with the path to your main DJ Pool directory.
   - Update `source_folders` with the paths to the folders containing the files you wish to organize.
   - Set `downloads_folder` to the path of your Downloads folder.

2. **Running the Script**: 
   - Run the script in a Python environment.
   - You will be prompted to choose whether to create a new folder for today's date or use the most recent folder.
   - Based on your choice, the script will move files from the source folders and Downloads folder to the target location.

### Script Functionality

[Check out the code](/organizeDJPool.py)

- **File Moving**: Moves files from specified source folders to a target folder organized by date.
- **Folder Creation**: Automatically creates new folders based on the current date, or finds and uses the latest existing folder.
- **User Input**: Prompts the user to either create a new folder or use the latest folder.
- **Subfolder for Converted Files**: Inside the target folder, a subfolder named `converted` is created, where `.mp3` files from the Downloads folder are specifically moved.

## Create Automated Playlists

This Python script is designed for DJs to organize a large collection of music files. It automatically sorts music files from a DJ pool folder into playlists based on their genre and certain keywords in the file titles.

### Prerequisites

Before running this script, you should have:

- Python installed on your system.
- The `mutagen` library installed. You can install it using pip: `pip install mutagen`.
- The music files you wish to organize, preferably in `.mp3` format.

### Setup

1. **Configure the Script**:
   - Set `dj_pool_path` to the path where your music files are stored.
   - Update the `genres` list to include the genres you're interested in.
   - Modify `title_keywords` with keywords that often appear in your file titles.

2. **Run the Script**:
   - Execute the script in a Python environment.
   - The script will process all `.mp3` files in the specified directory, organizing them into playlists based on genre and title keywords.

### Script Functionality

[Check out the code](/createPlaylist.py)

- **File Categorization**: The script categorizes music files based on genre information from their metadata and keywords in their titles.
- **Playlist Creation**: It creates `.m3u` playlist files for each genre and keyword.
- **Directory Structure**: Playlists are stored in separate "Genres" and "Keywords" folders within an "AutomatedPlaylists" folder in your DJ Pool path.
