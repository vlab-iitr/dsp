import streamlit as st

# Define the MCQs and their answers
questions = [
        {
            "question": "Q1. What is the purpose of modulation in communication systems?",
            "options": ["a. To eliminate noise from the signal ",
                        "b. To increase the frequency of the signal",
                        "c. To encode information onto a carrier wave for transmission",
                        "d. To amplify the transmitted signal "],
            "answer": "c. To encode information onto a carrier wave for transmission",
            "feedback":""
        },
        {
            "question": "Q2. Which of the following is NOT a modulation technique? ",
            "options": ["a. Amplitude Modulation (AM)", "b. Frequency Modulation (FM)", "c. Pulse Modulation (PM)", "d. Analog Multiplexing"],
            "answer": "d. Analog Multiplexing",
            "feedback":""
        },
        {
            "question": "Q3. Which of the following is an application of AM?",
            "options": ["a. Satellite communication", "b. AM radio broadcasting", "c. Wi-Fi communication", "d. Mobile telephony"],
            "answer": "b. AM radio broadcasting",
            "feedback":""
        },
        {
            "question": "Q4. In FM, the parameter of the carrier wave that is varied is:",
            "options": ["a. Amplitude", "b. Frequency", "c. Phase", "d. Wavelength"],
            "answer": "b. Frequency",
            "feedback":""
        },
        {
            "question": "Q5. In PM, the parameter of the carrier wave that is varied is:",
            "options": ["a. Frequency", "b. Amplitude", "c. Phase", "d. Wavelength"],
            "answer": "c. Phase",
            "feedback":""
        }
    ]

    
# Initialize the user answers if not already initialized
def test7():
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

    st.markdown('<div class="my-custom-text">Study and Demonstrate the Amplitude, Frequency and Phase Modulation</div>',unsafe_allow_html=True)
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
      

