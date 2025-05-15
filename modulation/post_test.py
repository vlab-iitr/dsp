import streamlit as st

# Define the MCQs and their answers
questions = [
        {
            "question": "Q1. What is the bandwidth requirement for an AM signal with a maximum modulating frequency of 5 kHz?",
            "options": ["a. 5 kHz",
                        "b. 10 kHz",
                        "c. 15 kHz",
                        "d. 20 kHz"],
            "answer": "b. 10 kHz"
        },
        {
            "question": "Q2. Which term refers to the ratio of the amplitude of the modulating signal to the amplitude of the carrier signal?",
            "options": ["a. Modulation depth", "b. Modulation index", "c. Signal-to-noise ratio", "d. Bandwidth efficiency"],
            "answer": "b. Modulation index"
        },
        {
            "question": "Q3. Phase modulation is closely related to which other modulation technique?",
            "options": ["a. Amplitude Modulation (AM)", "b. Frequency Modulation (FM)", "c. Pulse-Code Modulation (PCM)", "d. Quadrature Amplitude Modulation (QAM)"],
            "answer": "b. Frequency Modulation (FM)"
        },
        {
            "question": "Q4. Which modulation technique requires the largest bandwidth? ",
            "options": ["a. AM", "b. FM", "c. PM", "d. All require the same bandwidth"],
            "answer": "b. FM"
        },
        {
            "question": "Q5. In AM, the total power transmitted is split between the carrier and:",
            "options": ["a. Sidebands", "b. Noise", "c. Phase variation", "d. Harmonics"],
            "answer": "a. Sidebands"
        }
    ]


# Initialize the user answers if not already initialized
def post7():
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
    
    st.markdown('<div class="my-custom-text">Study and Demonstrate the Amplitude, Frequency and Phase Modulation</div>',unsafe_allow_html=True)
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

