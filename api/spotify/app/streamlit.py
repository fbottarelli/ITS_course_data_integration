import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_artist_comparison(artist1_id, artist2_id):
    # Invia una richiesta POST all'API Flask con gli ID degli artisti
    response = requests.post("http://localhost:5000/artists_comparison", json={"artist1_id": artist1_id, "artist2_id": artist2_id})
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Errore nella ricezione dei dati dall'API")
        return None

def plot_features_comparison(data_tracks, artist1_id, artist2_id):
    # Crea un DataFrame dai dati delle tracce
    df = pd.DataFrame(data_tracks)
    
    # Crea lo scatter plot
    fig, ax = plt.subplots()
    colors = {artist1_id: 'blue', artist2_id: 'red'}  # Sostituisci con gli ID reali degli artisti
    
    for artist_id, group in df.groupby('artist_id'):
        ax.scatter(group['danceability'], group['loudness'], alpha=0.7, label=group['artist'].iloc[0], c=colors[artist_id])
    
    plt.title('Confronto Danceability vs. Loudness')
    plt.xlabel('Danceability')
    plt.ylabel('Loudness (dB)')
    plt.legend(title='Artist')
    st.pyplot(fig)

def show_average_features(data_tracks):
    # Crea un DataFrame dai dati delle tracce
    df = pd.DataFrame(data_tracks)
    
    # Assicurati che tutte le colonne di interesse siano numeriche
    numeric_columns = ['loudness', 'danceability', 'energy', 'valence', 'tempo', 'artist']
    df = df[numeric_columns]
    # Calcola la media delle caratteristiche audio per artista
    average_features = df.groupby('artist').mean()[['loudness', 'danceability', 'energy', 'valence', 'tempo']]
    
    # Visualizza la tabella delle medie
    st.write("Media delle Caratteristiche Audio per Artista:")
    st.dataframe(average_features)



def main():
    st.title("Confronto Artisti su Spotify")

    artist1_id = st.text_input("Inserisci l'ID Spotify del primo artista")
    artist2_id = st.text_input("Inserisci l'ID Spotify del secondo artista")

    if st.button("Confronta"):
        if artist1_id and artist2_id:
            data = get_artist_comparison(artist1_id, artist2_id)
            if data:
                # Visualizzazione delle immagini degli artisti
                artist1, artist2 = data['data_artists']
                col1, col2 = st.columns(2)
                with col1:
                    st.image(artist1['image'], caption=artist1['name'])
                    st.markdown(f"**Nome:** {artist1['name']}")
                    st.markdown(f"**Follower:** {artist1['followers']:,}")
                    st.markdown(f"**Popolarità:** {artist1['popularity']}")
                    st.markdown(f"**Generi:** {', '.join(artist1['genres'])}")
                with col2:
                    st.image(artist2['image'], caption=artist2['name'])
                    st.markdown(f"**Nome:** {artist2['name']}")
                    st.markdown(f"**Follower:** {artist2['followers']:,}")
                    st.markdown(f"**Popolarità:** {artist2['popularity']}")
                    st.markdown(f"**Generi:** {', '.join(artist2['genres'])}")
                
                # Visualizzazione del grafico delle loudness
                plot_features_comparison(data['data_tracks'], artist1_id, artist2_id)
                # Mostra la tabella delle medie delle caratteristiche audio
                show_average_features(data['data_tracks'])
        else:
            st.error("Per favore inserisci gli ID di entrambi gli artisti.")

if __name__ == "__main__":
    main()

