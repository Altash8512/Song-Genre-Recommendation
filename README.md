# Spotify Music Recommendation System

## Project Description

This project is a music recommendation system built using a Spotify dataset. It uses machine learning to group similar songs into clusters and recommends music based on these clusters. The project includes a data analysis notebook, a Python script with the core logic, and a Streamlit web application to provide a user-friendly interface for getting song recommendations.

## Features

- **Data Pre-processing:** Cleans the dataset by handling missing values and duplicates.
- **Exploratory Data Analysis:** Analyzes the relationships between different audio features using a correlation matrix.
- **Clustering:** Uses the K-Means algorithm to group songs based on their audio features.
- **Elbow Method:** Determines the optimal number of clusters for the K-Means algorithm.
- **Interactive Web App:** A Streamlit application that allows users to get song recommendations based on their choice of genre, playlist, and subgenre.

## Dataset

The project uses the `spotify_dataset.csv` file, which contains information about various songs, including their audio features, genre, and playlist information.

## Methodology

1.  **Data Pre-processing:** The dataset is loaded and cleaned to remove any missing or duplicate entries.
2.  **Feature Scaling:** The numerical audio features are scaled using `StandardScaler` to prepare them for the clustering algorithm.
3.  **Clustering:** The K-Means clustering algorithm is applied to the scaled features to group the songs into 4 distinct clusters. The optimal number of clusters was determined using the elbow method.
4.  **Recommendation Logic:** The recommendation system is based on the generated clusters. When a user requests a recommendation, a song is selected from their specified genre/playlist/subgenre, and other songs from the same cluster are recommended.

## Files in the Project

- **`app.py`:** The main file for the Streamlit web application. This is the file you will run to use the recommendation system.
- **`spotify_dataset.csv`:** The dataset used for the project.
- **`SpotifySongGenre.ipynb`:** A Jupyter Notebook containing the detailed step-by-step analysis, including data pre-processing, visualization, and model building.
- **`recommender.py`:** A Python script that contains the core logic for the recommendation system, including data cleaning, clustering, and the recommendation function.

## How to Use

1.  **Install the required libraries:**
    ```
    pip install streamlit pandas scikit-learn
    ```
2.  **Run the Streamlit app:** Open a terminal or command prompt, navigate to the project directory, and run the following command:
    ```
    streamlit run app.py
    ```
3.  This will open the application in your web browser. You can then select a genre, playlist, and subgenre to get song recommendations.

## Technologies Used

- Python
- pandas
- scikit-learn
- Streamlit
- Matplotlib
- Seaborn
