import streamlit as st
import pickle
import pandas as pd
import requests
#fetch poster
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']

# Function to recommend movies based on similarity
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    recommend_movies_poster=[]
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(i[0])
    return recommend_movies

# Load the data from pickle files
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Convert the dictionary to a DataFrame
movies = pd.DataFrame(movies_dict)

# Streamlit app title
st.title('Movie Recommender System')

# Dropdown menu for selecting a movie
selected_movie_name = st.selectbox('Choose a movie:', movies['title'].values)

# Button to get recommendations
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write('Recommended Movies:')
    for title in recommendations:
        st.write(title)
