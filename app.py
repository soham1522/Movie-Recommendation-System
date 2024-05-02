import pickle
import streamlit as st
import requests
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    
    for i in distances:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    

    return recommended_movie_names
# Use raw string literal or forward slashes to avoid escape character interpretation
movies_dict = pickle.load(open(r'C:\Users\soham\OneDrive\Desktop\projects\Movie Recommender System\movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open(r'C:\Users\soham\OneDrive\Desktop\projects\Movie Recommender System\similarity.pkl', 'rb'))
st.title('Movie Recommender System')

option = st.selectbox("Which Movie Would you like to select??", movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)