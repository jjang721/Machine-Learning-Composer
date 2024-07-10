import pickle
import streamlit as st
import numpy as np

st.header("Classical Recommender System using Machine Learning")
model = pickle.load(open('artifacts/model.pkl', 'rb'))
music_name = pickle.load(open('artifacts/music_name.pkl', 'rb'))
music = pickle.load(open('artifacts/music.pkl', 'rb'))

def fetch_music(suggestion):
    composer_name = []
    ids_index = []
    poster_url = []

    for composer in suggestion:
        composer_name.append(music.index[composer])
    
    for i in composer_name[0]:
        ids = np.where(music.index[composer] == i)
        ids_index.append(ids)
        
    return composer_name
    
 

def recommend_composer(composer_name):
    music_list = []
    song_id = np.where(music.index == composer_name)[0][0]
    music_array = music.values
    filtered_music = music_array[:, ~np.all(np.isnan(music_array), axis=0)]

    input_data = music.iloc[song_id].values.reshape(1, -1)  # Select a single row
    if input_data.shape[1] != filtered_music.shape[1]:
        raise ValueError("The input data must have the same number of features as the fitted data.")

    # Find the nearest neighbors
    distance, suggestion = model.kneighbors(input_data, n_neighbors=6)

    music_url = fetch_music(suggestion)

    for i in range(len(suggestion)):
        songs = music.index[suggestion[i]]
        for j in songs:
            music_list.append(j)
    return music_list, music_url

selected_music = st.selectbox(
    "Type or select a composer",
    music_name
)

if st.button("Recommendation for you!"):
    recommendation_composer = recommend_composer(selected_music)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(recommendation_composer[1])

    with col2:
        st.text(recommendation_composer[2])

    # with col3:
    #     st.text(recommendation_composer[3])
