import streamlit as st
import requests
import random

# Title of the web app
st.title('Open Trivia Quiz')

# Function to get trivia data from the API
def get_trivia_questions(amount=10, type='boolean'):
    url = f"https://opentdb.com/api.php?amount={amount}&type={type}"
    response = requests.get(url)
    data = response.json()
    return data['results']

# Sidebar options to select the number of questions and type
number = st.sidebar.selectbox('Number of Questions:', [5, 10, 15, 20], index=1)
type_of_questions = st.sidebar.radio('Type of Questions:', ['boolean', 'multiple'])

# Initialize session state to store user answers and scores
if 'submitted_answers' not in st.session_state:
    st.session_state.submitted_answers = []
if 'score' not in st.session_state:
    st.session_state.score = 0

# Function to display questions and options for user to select an answer
def quiz(questions):
    for i, question in enumerate(questions, start=1):
        st.subheader(f"Question {i}:")
        st.write(question['question'])

        # Multiple-choice handling
        if question['type'] == 'multiple':
            options = question['incorrect_answers'] + [question['correct_answer']]
            random.shuffle(options)  # Randomize the options
            answer = st.radio(f"Select an answer for question {i}:", options, key=f"question_{i}")
        # True/False handling
        else:
            answer = st.radio(f"Select True or False for question {i}:", ('True', 'False'), key=f"question_{i}")

        # Save the user's answer
        st.session_state.submitted_answers.append(answer)

# Function to calculate score
def calculate_score(questions):
    score = 0
    for question, submitted_answer in zip(questions, st.session_state.submitted_answers):
        if question['correct_answer'] == submitted_answer:
            score += 1
    return score

# Start the quiz
if st.button('Start Quiz'):
    # Clear previous answers
    st.session_state.submitted_answers.clear()
    st.session_state.score = 0

    # Load questions
    questions = get_trivia_questions(amount=number, type=type_of_questions)
    quiz(questions)

    # Submit answers
    if st.button('Submit Answers'):
        st.session_state.score = calculate_score(questions)
        st.write('Your Score: ', st.session_state.score, '/', len(questions))
        st.session_state.submitted_answers.clear()  # Clear answers for next round
