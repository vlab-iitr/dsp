
import streamlit as st

# Define the MCQs and their answers
questions = [
    {
      "question": "Q1. Which method is used to perform convolution faster using the frequency domain?",
      "options": [
        "a. Laplace Transform",
        "b. Fourier Transform",
        "c. Fast Fourier Transform (FFT)",
        "d. Z-Transform"
      ],
      "answer": "c. Fast Fourier Transform (FFT)",
      "explanation": "Convolution in the time domain is equivalent to multiplication in the frequency domain, which can be computed efficiently using the FFT."
    },
    {
      "question": "Q2. What is circular convolution used for?",
      "options": [
        "a. Finding impulse response",
        "b. Filtering continuous signals",
        "c. Convolution of periodic signals",
        "d. Calculating power spectral density"
      ],
      "answer": "c. Convolution of periodic signals",
      "explanation": "Circular convolution is used in Fourier analysis for periodic signals and is often computed using the DFT (Discrete Fourier Transform)."
    },
    {
      "question": "Q3. What is the key difference between linear and circular convolution?",
      "options": [
        "a. Circular convolution is computed using FFT, while linear convolution is not",
        "b. Linear convolution results in aliasing, while circular convolution does not",
        "c. Linear convolution is used for periodic signals, circular convolution is not",
        "d. Circular convolution considers signal periodicity, linear convolution does not"
      ],
      "answer": "d. Circular convolution considers signal periodicity, linear convolution does not",
      "explanation": "Circular convolution assumes that the input signals are periodic, whereas linear convolution assumes finite-length sequences."
    },
    {
      "question": "Q4. If two discrete-time signals of lengths M and N are convolved, what is the length of the resulting signal?",
      "options": [
        "a. M+N−1",
        "b. M+N",
        "c. max(M, N)",
        "d. M⋅N"
      ],
      "answer": "a. M+N−1",
      "explanation": "The length of a convolved sequence is given by M+N−1 for linear convolution."
    },
    {
      "question": "Q5. What is the result of convolving a signal with a unit impulse?",
      "options": [
        "a. The original signal is unchanged",
        "b. The signal is reversed",
        "c. The signal is scaled by a constant factor",
        "d. The signal's frequency response is modified"
      ],
      "answer": "a. The original signal is unchanged",
      "explanation": "The unit impulse function acts as an identity operator in convolution, meaning convolution with an impulse results in the same signal."
    }
  ]

# Initialize the user answers if not already initialized
def post4():
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
    
    st.markdown('<div class="my-custom-text">Study the Linear and Circular Convolution of Two Signals</div>',unsafe_allow_html=True)
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

