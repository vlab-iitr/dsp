import streamlit as st

# Define the MCQs and their answers
questions = [
        {
            "question": "Q1. Spectrogram is the graph plotted against?",
            "options": [
            "a. Frequency domain",
            "b. Time domain",
            "c. Frequency & Time domain",
            "d. None of the mentioned"
            ],
            "answer": "b. Time domain"
            
        },
        {
             "question": "Q2. When two periodic sinusoids added then the result is ________.",
            "options": [
            "a. Sinusoidal signal",
            "b. Periodic signal",
            "c. Both a and b",
            "d. None of the above"
            ],
            "answer": "a. Sinusoidal signal"
            
        },
        {
            "question": "Q3. A signal is said to be a power/energy signal if the total energy/power transmitted is ________.",
            "options": [
            "a. One",
            "b. Zero",
            "c. Finite",
            "d. None of the above"
            ],
            "answer": "c. Finite"
            
        },
        {
            "question": "Q4. _______ methods are used to find whether the signal is periodic or not.",
            "options": [
            "a. Ratio method",
            "b. GCD method",
            "c. Both a and b",
            "d. None of the above"
            ],
            "answer": "b. GCD method"
            
        },
        {
            "question": "Q5. The power spectral density (PSD) of a signal is defined as:",
            "options": [
                "a. The total energy of the signal",
                "b. The power at each frequency divided by the frequency bandwidth",
                "c. The ratio of the energy to the time duration of the signal",
                "d. The energy distribution of the signal across time"
            ],
            "answer": "b. The power at each frequency divided by the frequency bandwidth"
            
        }
    ]


def post_ans2():
    st.markdown('<div class="my-custom-text">Study the Power Spectrum Analysis</div>',unsafe_allow_html=True)
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

def post_warning2():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"
