import datetime
import yaml
from pathlib import Path
import time
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import json



def testing_1():
    # --- Configuration ---
    current_file = Path(__file__).resolve()
    base_dir = current_file.parent.parent
    configs_path = base_dir / "configs" / "spotify.yaml"

    with open(configs_path) as config_file:
        config = yaml.safe_load(config_file)
    print(datetime.datetime.now().time())
    print(config["spotify"]["client_id"])  # Access a nested value
    print("========")
    
    

    
    

testing_1()