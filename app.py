import pickle
import streamlit as st
import pandas as pd   


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = cs[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True , key = lambda x:x[1])[1:6]
    L=[]
    for i in movies_list:
        L.append(movies.iloc[i[0]].title)
    return L
 

movies = pickle.load(open("Source_code\movies_dict.pkl" , "rb"))
movies = pd.DataFrame(movies)
cs = pickle.load(open("Source_code\cs.pkl" , "rb"))

st.title("Recommendations Engine")
selected_movie = st.selectbox("Seach or select the movie" , movies['title'].values)

if st.button("Recommend"):
    recommended_movies = recommend(selected_movie)
    for x in recommended_movies:
        st.write(x)



    









