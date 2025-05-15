import streamlit as st


# Define the MCQs and their answers
questions = [
        {
            "question": "Q1. Power spectral density function is a?",
            "options": [
            "a. Real and even function",
            "b. Non negative function",
            "c. Periodic",
            "d. All of the mentioned"
            ],
            "answer": "d. All of the mentioned"
            
        },
        {
            "question": "Q2. Energy spectral density defines?",
            "options": [
            "a. Signal energy per unit area",
            "b. Signal energy per unit bandwidth",
            "c. Signal power per unit area",
            "d. Signal power per unit bandwidth"
            ],
            "answer": "b. Signal energy per unit bandwidth"
            
        },
        {
            "question": "Q3. Power spectrum describes distribution of _________ under frequency domain.",
            "options": [
            "a. Mean",
            "b. Variance",
            "c. Gaussian",
            "d. None of the mentioned"
            ],
            "answer": "b. Variance"
            
        },
        {
            "question": "Q4. How can power spectral density of non periodic signal be calculated?",
            "options": [
            "a. By integrating",
            "b. By truncating",
            "c. By converting to periodic",
            "d. None of the mentioned"
            ],
            "answer": "b. By truncating"
    
        },
        {
            "question": "Q5. According to Parseval’s theorem the energy spectral density curve is equal to?",
            "options": [
            "a. Area under magnitude of the signal",
            "b. Area under square of the magnitude of the signal",
            "c. Area under square root of magnitude of the signal",
            "d. None of the mentioned"
            ],
            "answer": "b. Area under square of the magnitude of the signal"
            
        }
    ]


def pre_ans2():
    st.markdown('<div class="my-custom-text">Study the Power Spectrum Analysis</div>',unsafe_allow_html=True)
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

def pre_warning2():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"

