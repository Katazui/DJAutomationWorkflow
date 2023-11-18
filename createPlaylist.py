import os
import mutagen
from mutagen.easyid3 import EasyID3

# Define the path to your DJ Pool folder
dj_pool_path = "/path/to/pool"

# Define the genres you are interested in
genres = [
    "Rap", "R&B", "Top 40", "Pop", "Country", "Hip Hop", "Christmas", "Latin", 
    "Reggaeton", "Dance", "Electronic", "House", "EDM", "Trap", "Dubstep", 
    "Moombahton", "Twerk", "Rock", "Alternative", "Indie", "Funk", "Soul", 
    "Jazz", "Blues", "Oldies", "Disco", "Folk", "Classical", "Instrumental", 
    "Soundtrack", "Kids", "Christian", "Gospel", "Holiday", "Other", "Acapella", 
    "Clean", "Dirty", "Intro", "Quick Hit", "Short Edit", "Extended", "Remix", 
    "Mashup", "Bootleg", "Redrum", "Transition", "Drum & Bass", "Techno", 
    "Trance", "Afrobeat", "Bachata", "Salsa", "Reggae", "Dancehall", 
    "Deep House", "Tech House", "Progressive House", "Tropical House", 
    "Future Bass", "Glitch Hop", "Nu Disco", "Halloween", 
    "Ambient", "Hardstyle", "Psytrance", "Breakbeat", "UK Garage", "Grime", 
    "Future House", "Bass House", "Electro House", "Jersey Club", "Baltimore Club", 
    "Vocal House", "Latin Pop", "K-Pop", "J-Pop", "Cumbia", "Soca", "African", 
    "Bhangra", "Acapella Out", "Acapella In", "Segue", "Segue Mix", 
    "Drum Edit", "Bass Edit", "Instrumental", "Re-Drum", "Ampiano"
]

title_keywords = ["Intro", "Dirty", "Clean", "Transition", "Slam", "Edit", "Remix", "Acap", "Quick", "Quickie", "Short", "Explict", "Instrumental"]

# Create dictionaries to hold filenames for each genre and title keyword
genre_files = {genre: [] for genre in genres}
genre_files['NoGenre'] = []
keyword_files = {keyword: [] for keyword in title_keywords}

# Function to get the genre from the file's metadata
def get_genre(file_path):
    try:
        audio = EasyID3(file_path)
        return audio['genre'][0] if 'genre' in audio and audio['genre'][0] in genres else 'NoGenre'
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 'NoGenre'

# Function to categorize files based on title keywords
def categorize_by_title(file_path):
    filename = os.path.basename(file_path)
    for keyword in title_keywords:
        if keyword.lower() in filename.lower():
            keyword_files[keyword].append(file_path)
            break

# Create directories for playlists
playlists_path = os.path.join(dj_pool_path, "AutomatedPlaylists")
genres_path = os.path.join(playlists_path, "Genres")
keywords_path = os.path.join(playlists_path, "Keywords")
os.makedirs(genres_path, exist_ok=True)
os.makedirs(keywords_path, exist_ok=True)        

# Walk through the folder and add files to the respective lists
for root, dirs, files in os.walk(dj_pool_path):
    for file in files:
        if file.endswith('.mp3'):
            file_path = os.path.join(root, file)
            genre = get_genre(file_path)
            genre_files[genre].append(file_path)
            categorize_by_title(file_path)

# Write the .m3u files for genres in Genres folder
for genre, files in genre_files.items():
    if files:
        playlist_path = os.path.join(genres_path, f"{genre}.m3u")
        with open(playlist_path, 'w') as playlist:
            for file in files:
                playlist.write(f"{file}\n")
            print(f"Genre playlist created: {playlist_path}")

# Write the .m3u files for title keywords in Keywords folder
for keyword, files in keyword_files.items():
    if files:
        playlist_path = os.path.join(keywords_path, f"{keyword}.m3u")
        with open(playlist_path, 'w') as playlist:
            for file in files:
                playlist.write(f"{file}\n")
            print(f"Keyword playlist created: {playlist_path}")
