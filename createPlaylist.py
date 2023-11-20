import os
import mutagen
import concurrent.futures
from mutagen.easyid3 import EasyID3

# Define the path to your DJ Pool folder
dj_pool_path = "/Users/Music/Local DJ Pool/DJ Pool/"

# Define the genres you are interested in
genres = [
    "Rap", "R&B", "Top 40", "Pop", "Country", "Hip Hop", "Christmas", "Latin", 
    "Reggaeton", "Dance", "Electronic", "House", "EDM", "Trap", "Dubstep", "Electronica",
    "Moombahton", "Twerk", "Rock", "Alternative", "Indie", "Funk", "Soul", "Hardcore",
    "Jazz", "Blues", "Oldies", "Disco", "Folk", "Classical", "Instrumental", "Wedding",
    "Soundtrack", "Kids", "Christian", "Gospel", "Holiday", "Other", "#MIX", "New Year's Eve",
    "Mashup", "Bootleg", "Drum & Bass", "Techno", "#50KSET", "#BLEND",
    "Trance", "Afrobeats", "Bachata", "Salsa", "Reggae", "Dancehall", "#OUTRO", "Drill",
    "Deep House", "Tech House", "Progressive House", "Tropical House", "#CLEAN", "Loops",
    "Future Bass", "Glitch Hop", "Nu Disco", "Halloween", "#EDIT", "#INTRO", "#DROP", "Traditional",
    "Ambient", "Hardstyle", "Psytrance", "Breakbeat", "UK Garage", "Grime", "Drum Loops",
    "Future House", "Bass House", "Electro House", "Jersey Club", "Baltimore Club", "Tools",
    "Vocal House", "Latin Pop", "K-Pop", "J-Pop", "Cumbia", "Soca", "African", "Sample",
    "Bhangra", "Segue", "Segue Mix", "Instrumental", "Re-Drum", "Ampiano", "Dembow"
]

title_keywords = ["Transition", "Slam", "Edit", "Remix", "Instrumental", "Extended", "Redrum"]

grouped_playlists = {
    "Dirty": ["Dirty", "Explicit"],
    "Clean": ["Clean", "Radio"],
    "Quick Hits": ["Quick", "Quickie", "Short"],
    "Acappella": ["Acap", "Acapella", "Acapella In", "Acapella Out" ,"Acap In", "Acap Out"],
    "Intro": ["Intro", "Break Intro"],
    "Tools": ["Loops"]
}

# Create dictionaries to hold filenames for each genre, title keyword, and grouped playlists
genre_files = {genre: [] for genre in genres}
genre_files['NoGenre'] = []
keyword_files = {keyword: [] for keyword in title_keywords}
grouped_files = {group: [] for group in grouped_playlists}

# Function to process each file (both genre and keywords)
def process_file(file_path):
    genre_list = get_genre(file_path)
    for genre in genre_list:
        genre_files[genre].append(file_path)
    
    categorize_by_title(file_path)


# Function to get the genre from the file's metadata
def get_genre(file_path):
    try:
        audio = EasyID3(file_path)
        if 'genre' in audio:
            genre_list = [genre.strip() for genre in audio['genre'][0].split(',')]
            return [genre for genre in genre_list if genre in genres]
        else:
            return ['NoGenre']
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ['NoGenre']


# Function to categorize files based on title keywords
def categorize_by_title(file_path):
    filename = os.path.basename(file_path).lower()
    categorized = False

    for group, keywords in grouped_playlists.items():
        if any(keyword.lower() in filename for keyword in keywords):
            grouped_files[group].append(file_path)
            categorized = True
            break

    if not categorized:
        for keyword in title_keywords:
            if keyword.lower() in filename:
                keyword_files[keyword].append(file_path)
                break

# Create directories for playlists
playlists_path = os.path.join(dj_pool_path, "AutomatedPlaylists")
genres_path = os.path.join(playlists_path, "Genres")
keywords_path = os.path.join(playlists_path, "Keywords")
os.makedirs(genres_path, exist_ok=True)
os.makedirs(keywords_path, exist_ok=True)        

# # Walk through the folder and add files to the respective lists
# for root, dirs, files in os.walk(dj_pool_path):
#     for file in files:
#         if file.endswith('.mp3') or file.endswith('.MP3'):
#             file_path = os.path.join(root, file)
#             genre = get_genre(file_path)
#             genre_files[genre].append(file_path)
#             categorize_by_title(file_path)

# Using ThreadPoolExecutor to process files concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for root, _, files in os.walk(dj_pool_path):
        for file in files:
            if file.lower().endswith('.mp3'):
                file_path = os.path.join(root, file)
                futures.append(executor.submit(process_file, file_path))

    # Wait for all futures to complete
    concurrent.futures.wait(futures)

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

# Write the .m3u files for grouped playlists in Keywords folder
for group, files in grouped_files.items():
    if files:
        playlist_path = os.path.join(keywords_path, f"{group}.m3u")
        with open(playlist_path, 'w') as playlist:
            for file in files:
                playlist.write(f"{file}\n")
            print(f"Grouped playlist created: {playlist_path}")            
