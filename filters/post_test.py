import streamlit as st

# Define the MCQs and their answers
questions = [
        {
            "question": "Q1. FIR filters operate on ___ type of input values?",
            "options": [
                "a. Present",
                "b. Past",
                "c. Next",
                "d. Both a and b"
            ],
            "answer": "d. Both a and b",
            "feedback":""
        },
        {
             "question": "Q2. FIR filter implements _____ transfer function?",
            "options": [
                "a. Zero",
                "b. Uni",
                "c. Bi",
                "d. Multi"
            ],
            "answer": "a. Zero",
            "feedback":""
        },
        {
            "question": "Q3. In this type of designing, the system function of IIR filter is expressed in which form?",
            "options": [
                "a. Parallel form",
                "b. Cascade form",
                "c. Mixed form",
                "d. Any of the mentioned"
            ],
            "answer": "b. Cascade form",
            "feedback":""
        },
        {
            "question": "Q4. Filters allow transmission of signals in a ____________.",
            "options": [
                "a. Certain band of frequencies",
                "b. Out of the band the frequencies will be rejected",
                "c. Both a and b",
                "d. None of the above"
            ],
            "answer": "a. Certain band of frequencies",
            "feedback":""
        },
        {
            "question": "Q5. Which technique is commonly used for designing IIR filters that maintains the frequency response of analog filters?",
            "options": [
                "a. Impulse invariant transformation",
                "b. Fourier transformation",
                "c. Rectangular windowing",
                "d. Bilinear transformation"
            ],
            "answer": "d. Bilinear transformation",
            "feedback":""
        }
    ]


# Initialize the user answers if not already initialized
def post6():
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

