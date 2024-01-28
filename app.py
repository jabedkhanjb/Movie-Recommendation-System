import pickle
import streamlit as st
import pandas as pd

st.header("Movies Recommendation System Using Machine Learning")

# Load data from the pickled file
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values


st.selectbox(
    'Search your movie', movie_list
)

