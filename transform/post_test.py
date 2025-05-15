import streamlit as st

# Define the MCQs and their answers
questions = [
        {
      "question": "Q1. What is the key advantage of the Chirp-Z Transform over the FFT?",
      "options": {
        "a. It is always faster than the FFT",
        "b. It provides frequency analysis over arbitrary frequency ranges",
        "c. It works only with real-valued signals",
        "d. It does not require a sampling rate"
      },
      "answer": "b. It provides frequency analysis over arbitrary frequency ranges",
      "explanation": "Unlike FFT, which computes frequencies at fixed intervals, Chirp-Z Transform (CZT) allows flexible frequency resolution."
    },
    {
      "question": "Q2. In under-sampling detection, what happens if the sampling rate is lower than twice the highest frequency?",
      "options": {
        "a. The signal disappears",
        "b. The signal is distorted due to aliasing",
        "c. The signal remains unchanged",
        "d. The amplitude of the signal decreases"
      },
      "answer": "b. The signal is distorted due to aliasing",
      "explanation": "Aliasing occurs when a signal is sampled below the Nyquist rate, causing overlapping frequencies in the spectrum."
    },
    {
      "question": "Q3. What is the significance of the unit impulse signal in DSP?",
      "options": {
        "a. It has all frequency components equally distributed",
        "b. It acts as a bandpass filter",
        "c. It removes noise from a signal",
        "d. It is used only in analog processing"
      },
      "answer": "a. It has all frequency components equally distributed",
      "explanation": "The unit impulse function contains all frequencies with equal amplitude, making it useful for system analysis."
    },
    {
      "question": "Q4. What is the key difference between FFT and DCT?",
      "options": {
        "a. DCT does not have imaginary components",
        "b. FFT is always faster than DCT",
        "c. DCT can be used for time-domain filtering",
        "d. FFT is better for data compression"
      },
      "answer": "a. DCT does not have imaginary components",
      "explanation": "Unlike FFT, which produces complex-valued outputs, DCT outputs only real values, making it suitable for compression."
    },
    {
      "question": "Q5. How does the Hilbert Transform extract the envelope of a signal?",
      "options": {
        "a. By filtering out high frequencies",
        "b. By computing the analytic signal and taking the magnitude",
        "c. By applying a lowpass filter",
        "d. By taking the FFT and removing imaginary components"
      },
      "answer": "b. By computing the analytic signal and taking the magnitude",
      "explanation": "The Hilbert Transform produces an analytic signal, whose magnitude represents the envelope of the original signal."
    }
 
    ]

# Initialize the user answers if not already initialized
def post5():
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
    
    st.markdown('<div class="my-custom-text">Spectral Analysis of Signals using Signal Transform Functions</div>',unsafe_allow_html=True)
    st.divider()
    st.markdown('<div class="my-custom-h3-text">Posttest</div>',unsafe_allow_html=True)
    
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

# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"

