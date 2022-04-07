from src.spotify.get_reco_tracks import get_reco_tracks
from src.spotify.get_token import get_token
from src.spotify.search_tracks import search_tracks
from src.spotify.get_genres import get_genres
from src.spotify.get_features import get_features


class Spotify:
    def __init__(self):
        self.get_token()


Spotify.get_token = get_token
Spotify.search_tracks = search_tracks
Spotify.get_genres = get_genres
Spotify.get_features = get_features
Spotify.get_reco_tracks = get_reco_tracks
