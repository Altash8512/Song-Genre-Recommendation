import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv('spotify_dataset.csv')
    df = df.dropna()
    df = df.drop_duplicates()
    return df

df = load_data()

# Feature scaling and clustering
@st.cache_data
def get_clusters(df):
    audio_features = ['danceability', 'energy', 'key', 'loudness', 'speechiness',
                      'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[audio_features])

    k = 4 # From our earlier analysis
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    df['cluster'] = kmeans.fit_predict(scaled_features)
    return df

df = get_clusters(df)

# Streamlit app interface
st.title("Spotify Song Recommendation System")

# Dropdown for Genre
genre_list = df['playlist_genre'].dropna().unique()
selected_genre = st.selectbox("Select a Genre", sorted(genre_list))

# Filter playlists based on selected genre
filtered_df_genre = df[df['playlist_genre'] == selected_genre]

# Dropdown for Playlist Name
playlist_names = filtered_df_genre['playlist_name'].dropna().unique()
selected_playlist = st.selectbox("Select a Playlist Name", sorted(playlist_names))

# Filter subgenres based on selected playlist
filtered_df_playlist = filtered_df_genre[filtered_df_genre['playlist_name'] == selected_playlist]
subgenre_list = filtered_df_playlist['playlist_subgenre'].dropna().unique()
selected_subgenre = st.selectbox("Select a Subgenre", sorted(subgenre_list))

# Number of recommendations
num_recommendations = st.slider("Number of Recommendations", min_value=1, max_value=10, value=5)

# Get and display recommendations when the button is clicked
if st.button("Recommend Songs"):
    # Filter the dataset based on selected genre, playlist, and subgenre
    user_filtered_df = filtered_df_playlist[filtered_df_playlist['playlist_subgenre'] == selected_subgenre]

    if not user_filtered_df.empty:
        # Choose a random song from the filtered dataframe
        base_song = user_filtered_df.sample(1)
        # Get the cluster of the base song
        base_cluster = base_song['cluster'].iloc[0]
        # Get recommendations from the same cluster, excluding the base song
        recommendations = df[(df['cluster'] == base_cluster) & (df['track_id'] != base_song['track_id'].iloc[0])].sample(num_recommendations)
        st.write(f"Recommendations based on your selection:")
        st.dataframe(recommendations[['track_name', 'track_artist', 'playlist_genre']])
    else:
        st.write("No songs found for the selected combination.")
