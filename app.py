import streamlit as st
import pickle
import pandas as pd
import requests

def  fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=77f4b161e6b1c08c8880790a703fc69e'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    LST = list(enumerate(Similarity[movie_index]))
    LS = sorted(LST, reverse=True, key=lambda y: y[1])
    Lo = LS[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for TP in Lo:

        movie_id=movies['movie_id'][TP[0]]

        recommended_movies.append(movies['title'][TP[0]])

        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters



movie_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
Similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)


if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
