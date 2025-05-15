
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

    
def post_ans4():
    st.markdown('<div class="my-custom-text">Study the Linear and Circular Convolution of Two Signals</div>',unsafe_allow_html=True)
    st.divider()
    st.markdown('<div class="my-custom-h3-text">Posttest</div>',unsafe_allow_html=True)

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

def post_warning4():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"

       
