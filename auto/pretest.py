import streamlit as st

questions = [
    {
      "question": "Q1. Autocorrelation is a function which matches?",
      "options": {
        "a. Two same signals",
        "b. Two different signals",
        "c. One signal with its delayed version",
        "d. None of the mentioned"
      },
      "answer": "c. One signal with its delayed version"
    },
    {
      "question": "Q2. Autocorrelation is a function of?",
      "options": {
        "a. Time",
        "b. Frequency",
        "c. Time difference",
        "d. Frequency difference"
      },
      "answer": "c. Time difference"
    },
    {
      "question": "Q3. Autocorrelation is maximum at _______.",
      "options": {
        "a. Unity",
        "b. Origin",
        "c. Infinite point",
        "d. None of the mentioned"
      },
      "answer": "b. Origin"
    },
    {
      "question": "Q4. Autocorrelation function of periodic signal is equal to _______.",
      "options": {
        "a. Energy of the signal",
        "b. Power of the signal",
        "c. Its area in frequency domain",
        "d. None of the mentioned"
      },
      "answer": "b. Power of the signal"
    },
    {
      "question": "Q5. Autocorrelation is a _______ function.",
      "options": {
        "a. Real and even",
        "b. Real and odd",
        "c. Complex and even",
        "d. Complex and odd"
      },
      "answer": "a. Real and even"
    }
    
  ]


# Initialize the user answers if not already initialized
def test3():
    # Check if 'user_answers' exists in session_state, otherwise initialize it
    if 'user_answers' not in st.session_state:
        # Initialize user_answers with 'None' for each question (based on number of questions)
        st.session_state.user_answers = [None] * 5  # Adjust the number '5' to match the number of questions

    st.markdown(
    """
    <style>
        p {
            font-family: Georgia, serif;
        }
        
    </style>
    """, 
    unsafe_allow_html=True
    )
    
    st.markdown('<div class="my-custom-text">Study the Autocorrelation Analysis</div>',unsafe_allow_html=True)
    st.divider()
    st.markdown('<div class="my-custom-h3-text">Pretest</div>',unsafe_allow_html=True)

    
    # Loop over the questions and create radio buttons for each one
    for idx, question in enumerate(questions):
        # Check if the selected answer already exists in session_state
        if st.session_state.user_answers[idx] is not None:
            selected_answer = st.session_state.user_answers[idx]
        else:
            selected_answer = None
        
        # Display the question and options
        user_answer = st.radio(
            question["question"],
            question["options"],
            key=f"question_{idx}",
            index=None  # Retain selected answer if available
        )
        
        # Store the user's answer in session state
        st.session_state.user_answers[idx] = user_answer

