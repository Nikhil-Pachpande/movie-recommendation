import streamlit as st
import pickle
import pandas as pd
import requests


# For fetching the Poster of the recommended movies
# get the poster from the api key of the source
# def fetch_poster(movie_id):
#     url = 'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     poster = 'https://image.tmdb.com/t/p/w500/' + poster_path
#     return poster


# This function will recommend a list of movies based on similarity to the movie name we'll provide
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetching the poster from the API
        # recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies  # , recommended_movies_posters


# load the pickle of the model that we have created and saved in jupyter
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
# Similarity
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')
# Taking input from the user
selected_movie_name = st.selectbox(
    'Type or select a name of the movie you have watched to show recommendations.', movies['title'].values)

# Button to show the recommendations
if st.button('Show Recommendations'):
    # names, posters = recommend(selected_movie_name)
    names = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    st.text('The top 5 movies recommended for you are:')
    for i in range(0, 5):
        st.text(names[i])
        # st.image(posters[i])
