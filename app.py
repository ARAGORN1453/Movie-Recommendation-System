import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key="YOUR API KEY"&language=en-US".format( movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movies=pickle.load(open("movies.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
movies_list=movies["title"].values

st.title("Movie Recommendation Site ")

import streamlit.components.v1 as components
imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
]

imageCarouselComponent(imageUrls=imageUrls, height=200)
select_value=st.selectbox("Select movie name ",movies_list)

def recommend(movie_name):
    index=movies[movies["title"]==movie_name].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    recommend_movies=[]
    recommend_posters=[]
    for i in distance[0:5]:
        movies_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_posters.append(fetch_poster(movies_id))
    return  recommend_movies,recommend_posters

if st.button("Show Recommend"):
    recommended_movie_name,recomended_movie_poster=recommend(select_value)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(recommended_movie_name[0])
        st.image(recomended_movie_poster[0])
    with col2:
        st.text(recommended_movie_name[1])
        st.image(recomended_movie_poster[1])
    with col3:
        st.text(recommended_movie_name[2])
        st.image(recomended_movie_poster[2])
    with col4:
        st.text(recommended_movie_name[3])
        st.image(recomended_movie_poster[3])
    with col5:
        st.text(recommended_movie_name[4])
        st.image(recomended_movie_poster[4])
