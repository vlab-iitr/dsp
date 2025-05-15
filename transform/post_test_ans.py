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

 
def post_ans5():
    st.markdown('<div class="my-custom-text">Spectral Analysis of Signals using Signal Transform Functions</div>',unsafe_allow_html=True)
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

def post_warning5():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"
