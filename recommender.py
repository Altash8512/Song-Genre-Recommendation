import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("c:\\Users\\altam\\Desktop\\Major-Project-1\\spotify_dataset.csv")

# Drop rows with missing values
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

# Select numerical columns for clustering
numerical_df = df.select_dtypes(include=['float64', 'int64'])

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(numerical_df)

# Perform K-Means clustering
k = 4
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(scaled_features)

def recommend_songs(track_name, df):
    """Recommends songs from the same cluster as the input song."""
    try:
        cluster = df[df['track_name'] == track_name]['cluster'].iloc[0]
        recommended_songs = df[df['cluster'] == cluster].sample(5)['track_name']
        return recommended_songs
    except IndexError:
        return "Song not found."

# Example usage:
print("Recommendations for 'bad guy':")
print(recommend_songs('bad guy', df))