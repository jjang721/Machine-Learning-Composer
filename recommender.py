import streamlit as st
import pickle
import numpy as np
import ctypes

# --- Load compiled C library ---
lib = ctypes.CDLL('./retrieval.so')
lib.best_match.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64),
    np.ctypeslib.ndpointer(dtype=np.float64),
    ctypes.c_int,
    ctypes.c_int
]
lib.best_match.restype = ctypes.c_int

def find_best_match(query, dataset):
    return lib.best_match(
        np.array(query, dtype=np.float64),
        np.array(dataset, dtype=np.float64),
        len(dataset),
        len(query)
    )

# --- Streamlit UI ---
st.header("Classical Recommender System using Machine Learning")

# Load data
model = pickle.load(open('artifacts/model.pkl', 'rb'))
music_name = pickle.load(open('artifacts/music_name.pkl', 'rb'))
music = pickle.load(open('artifacts/music.pkl', 'rb'))

# Example button to test
if st.button("Test C Search"):
    query = [0.1, 0.2, 0.3]
    dataset = [
        [0.1, 0.2, 0.3],
        [0.9, 0.1, 0.4],
        [0.0, 0.0, 1.0]
    ]
    idx = find_best_match(query, dataset)
    st.write("Best match index:", idx)
