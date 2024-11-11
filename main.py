import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URL = os.getenv("SPOTIPY_REDIRECT_URI")

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    redirect_uri="YOUR_REDIRECT_URI",
    scope="user-library-read"
))



def get_artist():
    pass

def get_track():
    try:
        track = sp.track("nonexistent_id")
    except spotipy.exceptions.SpotifyException as e:
        print("Spotify API error:", e)


def get_album():
    pass

track_id = "3n3Ppam7vgaVa1iaRUc9Lp"  # Replace with a Spotify track ID
track = sp.track(track_id)
print("Track name:", track['name'])
print("Artist:", track['artists'][0]['name'])
print("Album:", track['album']['name'])

artist_name = "Radiohead"
results = sp.search(q=artist_name, type="artist", limit=1)
artist = results['artists']['items'][0]
print("Artist name:", artist['name'])
print("Followers:", artist['followers']['total'])
print("Genres:", artist['genres'])
