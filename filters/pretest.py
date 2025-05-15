import streamlit as st

# Define the MCQs and their answers
questions = [
        {
            "question": "Q1. FIR stands for ____?",
            "options": ["a. Finite Impulse Filter",
                        "b. Infinite Impulse Filter",
                        "c. Finite Impedance Filter",
                        "d. Finite Impulse Fire"],
            "answer": "a. Finite Impulse Filter",
            "feedback":""
        },
        {
            "question": "Q2. Which of the following is the impulse response of FIR filter?",
            "options": ["a. Infinite", "b. Finite", "c. Zero", "d. Negative"],
            "answer": "b. Finite",
            "feedback":""
        },
        {
            "question": "Q3. Which windowing technique is primarily used for designing FIR filters with a very specific frequency response shape?",
            "options": ["a. Rectangular window", "b. Hamming window", "c. Kaiser window", "d. Bartlett window"],
            "answer": "c. Kaiser window",
            "feedback":""
        },
        {
            "question": "Q4. Which of the following is an advantage of using FIR filters over IIR filters? ",
            "options": ["a. FIR filters have linear phase response",
                        "b. FIR filters require fewer coefficients",
                        "c. FIR filters can be easily implemented with feedback loops", 
                        "d. FIR filters are more computationally efficient "],
            "answer": "a. FIR filters have linear phase response",
            "feedback":""
        },
        {
            "question": "Q5. Which of the following are the components used in FIR filter?",
            "options": [
                "a. Adders",
                "b. Multipliers",
                "c. Logic gates",
                "d. All the above"
            ],
            "answer": "d. All the above",
            "feedback":""
        }
    ]


# Initialize the user answers if not already initialized
def test6():
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
    
    st.markdown('<div class="my-custom-text">Design of FIR and IIR Filters and Demonstrate the Filtering Operation</div>',unsafe_allow_html=True)
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

