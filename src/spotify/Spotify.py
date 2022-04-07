from src.spotify.get_token import get_token
from src.spotify.search_tracks import search_tracks


class Spotify:
    def __init__(self):
        self.get_token()


Spotify.get_token = get_token
Spotify.search_tracks = search_tracks
