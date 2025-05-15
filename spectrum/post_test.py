
import streamlit as st

# Define the MCQs and their answers
questions = [
        {
            "question": "Q1. Spectrogram is the graph plotted against?",
            "options": [
            "a. Frequency domain",
            "b. Time domain",
            "c. Frequency & Time domain",
            "d. None of the mentioned"
            ],
            "answer": "b. Time domain"
            
        },
        {
             "question": "Q2. When two periodic sinusoids added then the result is ________.",
            "options": [
            "a. Sinusoidal signal",
            "b. Periodic signal",
            "c. Both a and b",
            "d. None of the above"
            ],
            "answer": "a. Sinusoidal signal"
            
        },
        {
            "question": "Q3. A signal is said to be a power/energy signal if the total energy/power transmitted is ________.",
            "options": [
            "a. One",
            "b. Zero",
            "c. Finite",
            "d. None of the above"
            ],
            "answer": "c. Finite"
            
        },
        {
            "question": "Q4. _______ methods are used to find whether the signal is periodic or not.",
            "options": [
            "a. Ratio method",
            "b. GCD method",
            "c. Both a and b",
            "d. None of the above"
            ],
            "answer": "b. GCD method"
            
        },
        {
            "question": "Q5. The power spectral density (PSD) of a signal is defined as:",
            "options": [
                "a. The total energy of the signal",
                "b. The power at each frequency divided by the frequency bandwidth",
                "c. The ratio of the energy to the time duration of the signal",
                "d. The energy distribution of the signal across time"
            ],
            "answer": "b. The power at each frequency divided by the frequency bandwidth"
            
        }
    ]


# Initialize the user answers if not already initialized
def post2():
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
    
    st.markdown('<div class="my-custom-text">Study the Power Spectrum Analysis</div>',unsafe_allow_html=True)
    st.divider()
    st.markdown('<div class="my-custom-h3-text">Posttest</div>',unsafe_allow_html=True)
    
    # Loop over the questions and create radio buttons for each one
    for idx, question in enumerate(questions):       
        # Display the question and options
        user_answer = st.radio(
            question["question"],
            question["options"],
            key=f"question_{idx}",
            index=None  # Retain selected answer if available
        )
        
        # Store the user's answer in session state
        st.session_state.user_answers[idx] = user_answer

