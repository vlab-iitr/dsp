
import streamlit as st

# Define the MCQs and their answers
questions = [
    {
      "question": "Q1. Autocorrelation function of white noise will have?",
      "options": {
        "a. Strong peak",
        "b. Infinite peak",
        "c. Weak peak",
        "d. None of the mentioned"
      },
      "answer": "a. Strong peak"
    },
    {
      "question": "Q2. What does autocorrelation measure in a signal?",
      "options": [
        "a. The similarity between two different signals",
        "b. The similarity of a signal with a time-shifted version of itself",
        "c. The power of the signal",
        "d. The frequency response of a system"
      ],
      "answer": "b. The similarity of a signal with a time-shifted version of itself"
    },
    {
      "question": "Q3. Which of the following is always true for an autocorrelation function?",
      "options": [
        "a. It is always negative",
        "b. It is maximum at τ=0",
        "c. It is always periodic",
        "d. It is always zero for all τ"
      ],
      "answer": "b. It is maximum at τ=0"
    },
    {
      "question": "Q4. The autocorrelation function of a real-valued signal is always:",
      "options": [
        "a. Complex",
        "b. Anti-symmetric",
        "c. Symmetric",
        "d. Random"
      ],
      "answer": "c. Symmetric"
    },
    {
      "question": "Q5. The area under the autocorrelation function of an energy signal gives:",
      "options": [
        "a. Power of the signal",
        "b. Total energy of the signal",
        "c. Frequency response of the signal",
        "d. Phase information of the signal"
      ],
      "answer": "b. Total energy of the signal"
    }
  ]

# Initialize the user answers if not already initialized
def post3():
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
    st.markdown('<div class="my-custom-h3-text">Posttest</div>',unsafe_allow_html=True)
    
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

