import streamlit as st
import requests
from textblob import TextBlob

# Streamlit interface
st.title('Book Searcher and Sentiment Analysis')

# Input for book ID
book_id = st.number_input('Enter Book ID:', min_value=1, value=1)

# Button to fetch book data
if st.button('Fetch Book'):
    response = requests.get(f'http://127.0.0.1:5000/books/{book_id}')
    if response.status_code == 200:
        book_data = response.json()
        st.write(f"Title: {book_data['title']}")
        st.write(f"Author: {book_data['author']}")
        st.write(f"Year Published: {book_data['year']}")

        # Sentiment analysis
        sentiment = TextBlob(book_data['title']).sentiment
        st.write(f"Sentiment of Title: {'Positive' if sentiment.polarity > 0 else 'Negative' if sentiment.polarity < 0 else 'Neutral'}")
    else:
        st.error('Book not found!')

# Running the app
# To run this app, use: streamlit run streamlit_app.py
