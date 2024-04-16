from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Carica le credenziali di Spotify
load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_artist_info(artist_id):
    # Ottieni le informazioni sull'artista
    artist = sp.artist(artist_id)
    
    # Estrai i dati necessari
    artist_data = {
        'name': artist['name'],
        "id": artist['id'],
        'followers': artist['followers']['total'],
        'popularity': artist['popularity'],
        'genres': artist['genres'],
        'image': artist['images'][0]['url'] if artist['images'] else None
    }
    
    return artist_data

def get_track_features(track_id):
    # Ottieni le audio features per la traccia
    features = sp.audio_features(track_id)[0]
    if features:
        # Rimuovi le chiavi non necessarie
        features = {key: value for key, value in features.items() if key not in ['type', 'id', 'uri', 'track_href', 'analysis_url']}
    return features

def get_top_tracks(artist_id):
    results = sp.artist_top_tracks(artist_id)
    tracks = results['tracks'][:10]  # Limita a 10 le top tracks
    
    track_data = []
    for track in tracks:
        track_details = {
            'name': track['name'],
            'album': track['album']['name'],
            'artist': track['artists'][0]['name'],
            'artist_id': track['artists'][0]['id'],
            # 'artist_genres': track['artists'][0]['genres'],
            'release_date': track['album']['release_date'],
            'popularity': track['popularity'],
            'album_cover': track['album']['images'][0]['url'] if track['album']['images'] else None,
            'track_id': track['id']
        }
        # Aggiungi le audio features per ogni traccia
        track_features = get_track_features(track['id'])
        if track_features:
            track_details.update(track_features)
        
        track_data.append(track_details)
    
    return track_data

@app.route('/artists_comparison', methods=['POST'])
def artist_top_tracks():
    data = request.json
    artist1_id = data.get('artist1_id')
    artist2_id = data.get('artist2_id')
    # Ottieni info sugli artisti
    artist1_info = get_artist_info(artist1_id)
    artist2_info = get_artist_info(artist2_id)
    # Ottieni i top tracks per entrambi gli artisti
    artist1_tracks = get_top_tracks(artist1_id)
    artist2_tracks = get_top_tracks(artist2_id)
    
    df1 = pd.DataFrame(artist1_tracks)
    df2 = pd.DataFrame(artist2_tracks)
    
    combined_df = pd.concat([df1, df2])
    
    # Salva il DataFrame localmente
    combined_df.to_csv('top_tracks_with_selected_features.csv', index=False)
    
    return jsonify({'message': 'Top tracks retrieved and saved successfully.', 'data_tracks': combined_df.to_dict(orient='records'), 'data_artists': [artist1_info, artist2_info]})

if __name__ == '__main__':
    app.run(debug=True)