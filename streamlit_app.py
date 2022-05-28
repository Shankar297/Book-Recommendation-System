import streamlit as st
import pandas as pd
import pickle
import numpy as np
import requests


def recommend(book_name):
    # index fetch
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[-1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)
    return data


popular_df = pickle.load(open('popular.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

books_list = pt.index.tolist()

st.title('Books Recommendation Engine')
st.subheader('Created by Shankar Wagh')

selected_movie_name = st.selectbox(
    'Select any books to find similar books',
    books_list
)
if st.button('Recommend'):
    names = recommend(selected_movie_name)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(names[0][2])
        st.text(names[0][0])
        st.text(names[0][1])
    with col2:
        st.image(names[1][2])
        st.text(names[1][0])
        st.text(names[1][1])
    with col3:
        st.image(names[2][2])
        st.text(names[2][0])
        st.text(names[2][1])
    with col4:
        st.image(names[3][2])
        st.text(names[3][0])
        st.text(names[3][1])
