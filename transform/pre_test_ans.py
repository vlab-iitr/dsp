import streamlit as st

# Define the MCQs and their answers
questions = [
      {
      "question": "Q1. What is the primary purpose of the Fast Fourier Transform (FFT) in DSP?",
      "options": {
        "a. To convert a time-domain signal into the frequency domain",
        "b. To increase the amplitude of a signal",
        "c. To remove noise from a signal",
        "d. To detect phase shifts in real-time"
      },
      "answer": "a. To convert a time-domain signal into the frequency domain",
      "explanation": "The FFT is an efficient algorithm to compute the Discrete Fourier Transform (DFT), which helps analyze the frequency content of a signal."
    },
    {
      "question": "Q2. What is the main advantage of the Discrete Cosine Transform (DCT) over the FFT?",
      "options": {
        "a. DCT only works with real signals",
        "b. DCT is computationally faster",
        "c. DCT represents data with fewer coefficients for compression",
        "d. DCT can handle complex numbers better"
      },
      "answer": "c. DCT represents data with fewer coefficients for compression",
      "explanation": "DCT is widely used in image and audio compression (e.g., JPEG, MP3) because it concentrates energy in a few coefficients, making data easier to compress."
    },
    {
      "question": "Q3. What does the Discrete Sine Transform (DST) primarily do?",
      "options": {
        "a. Decomposes a signal into odd harmonics",
        "b. Converts a time-domain signal into the frequency domain like FFT",
        "c. Removes high-frequency components",
        "d. Enhances low-frequency content"
      },
      "answer": "a. Decomposes a signal into odd harmonics",
      "explanation": "DST is similar to DCT but represents the signal using only odd harmonics, making it useful in certain boundary-condition problems."
    },
    {
      "question": "Q4. Why is the Hilbert Transform useful in signal processing?",
      "options": {
        "a. It finds the energy of a signal",
        "b. It creates an analytic signal with real and imaginary parts",
        "c. It removes noise from a signal",
        "d. It compresses the signal"
      },
      "answer": "b. It creates an analytic signal with real and imaginary parts",
      "explanation": "The Hilbert Transform is used to construct an analytic signal, allowing for instantaneous amplitude and phase extraction."
    },
    {
      "question": "Q5. What is the purpose of the Wavelet Transform in DSP?",
      "options": {
        "a. It analyzes signals in both time and frequency domains",
        "b. It replaces the FFT for all applications",
        "c. It removes phase distortion",
        "d. It can only be used for image processing"
      },
      "answer": "a. It analyzes signals in both time and frequency domains",
      "explanation": "Wavelet Transform provides multi-resolution analysis, making it useful for non-stationary signals such as ECG, EEG, and speech."
    },
    
 
    ]

    
def pre_ans5():
    st.markdown('<div class="my-custom-text">Spectral Analysis of Signals using Signal Transform Functions</div>',unsafe_allow_html=True)
    st.divider()
    st.markdown('<div class="my-custom-h3-text">Pretest</div>',unsafe_allow_html=True)
    correct_answers = 0
    correct_answers = sum([1 for idx, user_answer in enumerate(st.session_state.user_answers) if user_answer == questions[idx]["answer"]])
    

    # Loop through questions and update feedback
    for idx, (user_answer, question) in enumerate(zip(st.session_state.user_answers, questions)):
        feedback = check_answer(user_answer, question["answer"])
        st.markdown(f"<p style='font-weight:bold;font-size:20px;margin-top:10px'>{question['question']}</p>", unsafe_allow_html=True)
        for option in question["options"]:
            color = "green" if option == user_answer and option == question["answer"] else \
                    "red" if option == user_answer and option != question["answer"] else "gray"
            st.markdown(f"<p style='color:{color};font-size:16px'>{option}</p>", unsafe_allow_html=True)
        st.write(f"**Solution:** {feedback}")

    st.markdown(f"<p style='color:blue;font-size:18px;font-weight:bold;margin-top:10px'>You got {correct_answers} out of {len(questions)} correct!</p>", unsafe_allow_html=True)

def pre_warning5():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"

 
