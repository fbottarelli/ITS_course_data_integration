import streamlit as st
import requests

# Title of the web app
st.title('Open Trivia Quiz')

# Function to get trivia data from the API
def get_trivia_questions(amount=10, type='boolean'):
    url = f"https://opentdb.com/api.php?amount={amount}&type={type}"
    response = requests.get(url)
    data = response.json()
    return data['results']

# Streamlit button to load questions
if st.button('Get Trivia Questions'):
    questions = get_trivia_questions()
    
    # Display each question and its correct answer
    for i, question in enumerate(questions, start=1):
        st.subheader(f"Question {i}")
        st.write(question['question'])
        st.write("Correct Answer:", question['correct_answer'])

# You can also provide options for the user to choose the number of questions and type
number = st.sidebar.selectbox('Number of Questions:', [5, 10, 15, 20], index=1)
type_of_questions = st.sidebar.radio('Type of Questions:', ['boolean', 'multiple'])

# Update the questions shown when the selection changes
if st.sidebar.button('Load Selected Trivia Questions'):
    questions = get_trivia_questions(amount=number, type=type_of_questions)
    for i, question in enumerate(questions, start=1):
        st.subheader(f"Question {i}")
        st.write(question['question'])
        st.write("Correct Answer:", question['correct_answer'])
