import streamlit as st

# Define the MCQs and their answers
questions = [
        {
            "question": "Q1. Power spectral density function is a?",
            "options": [
            "a. Real and even function",
            "b. Non negative function",
            "c. Periodic",
            "d. All of the mentioned"
            ],
            "answer": "d. All of the mentioned"
            
        },
        {
            "question": "Q2. Energy spectral density defines?",
            "options": [
            "a. Signal energy per unit area",
            "b. Signal energy per unit bandwidth",
            "c. Signal power per unit area",
            "d. Signal power per unit bandwidth"
            ],
            "answer": "b. Signal energy per unit bandwidth"
            
        },
        {
            "question": "Q3. Power spectrum describes distribution of _________ under frequency domain.",
            "options": [
            "a. Mean",
            "b. Variance",
            "c. Gaussian",
            "d. None of the mentioned"
            ],
            "answer": "b. Variance"
            
        },
        {
            "question": "Q4. How can power spectral density of non periodic signal be calculated?",
            "options": [
            "a. By integrating",
            "b. By truncating",
            "c. By converting to periodic",
            "d. None of the mentioned"
            ],
            "answer": "b. By truncating"
            
        },
        {
            "question": "Q5. According to Parseval’s theorem the energy spectral density curve is equal to?",
            "options": [
            "a. Area under magnitude of the signal",
            "b. Area under square of the magnitude of the signal",
            "c. Area under square root of magnitude of the signal",
            "d. None of the mentioned"
            ],
            "answer": "b. Area under square of the magnitude of the signal"
            
        }
    ]

# Initialize the user answers if not already initialized
def test2():
    # Check if 'user_answers' exists in session_state, otherwise initialize it
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = [None] * 5  # Adjust this number based on the number of questions

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
    st.markdown('<div class="my-custom-h3-text">Pretest</div>',unsafe_allow_html=True)
    
    # Display MCQs
    for idx, question in enumerate(questions):
        # Display the question and options
        user_answer = st.radio(
            question["question"],
            question["options"],
            key=f"question_{idx}",
            index=None 
        )

        # Store the user's answer in session state
        st.session_state.user_answers[idx] = user_answer

