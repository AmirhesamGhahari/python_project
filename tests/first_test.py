import datetime
import yaml
import time
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import json



def extract_recently_played(sp: Spotify) -> list:
    """
    Extract recently played tracks from Spotify.
    """
    results = sp.current_user_recently_played(limit=50)  # Fetch up to 50 recently played tracks
    print(results.keys())
    #print(results['items'].keys())
    print(results['items'][0].keys())
    print("========")
    print(results['items'][0]['track'].keys())
    tracks = results['items']
    data = []
    for track in tracks:
        played_at = track['played_at']  # Timestamp of playback
        duration_ms = track['track']['duration_ms']  # Duration in milliseconds
        track_name = track['track']['name']
        album_name = track['track']['album']['name']
        artist_name = track['track']['artists'][0]['name']
        popularity = track['track']['popularity']
        data.append({"played_at": played_at, "duration_ms": duration_ms, 
                     "artist_name": artist_name, "popularity": popularity, "track_name": track_name, 
                     "album_name": album_name
                     })
    return data

def testing_1():

    # --- Configuration ---
    with open("../configs/spotify.yaml") as config_file:
        config = yaml.safe_load(config_file)
    print(datetime.datetime.now().time())
    print(config["spotify"]["client_id"])  # Access a nested value
    print("========")
    SPOTIFY_CLIENT_ID = config["spotify"]["client_id"]
    SPOTIFY_CLIENT_SECRET = config["spotify"]["client_secret"]
    SPOTIFY_APP_NAME = config["spotify"]["app_name"]
    SPOTIFY_REDIRECT_URI = config["spotify"]["redirect_uri"]


    # Initialize Spotify Authentication
    scope = "user-read-recently-played"
    sp = Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=scope
    ))

    if sp is None:
        print("Spotify object is none")
    
    data = extract_recently_played(sp)
    print(json.dumps(data, indent=4))
    

    
    

testing_1()