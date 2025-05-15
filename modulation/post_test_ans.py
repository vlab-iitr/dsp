import streamlit as st

# Define the MCQs and their answers
questions = [
        {
            "question": "Q1. What is the bandwidth requirement for an AM signal with a maximum modulating frequency of 5 kHz?",
            "options": ["a. 5 kHz",
                        "b. 10 kHz",
                        "c. 15 kHz",
                        "d. 20 kHz"],
            "answer": "b. 10 kHz"
        },
        {
            "question": "Q2. Which term refers to the ratio of the amplitude of the modulating signal to the amplitude of the carrier signal?",
            "options": ["a. Modulation depth", "b. Modulation index", "c. Signal-to-noise ratio", "d. Bandwidth efficiency"],
            "answer": "b. Modulation index"
        },
        {
            "question": "Q3. Phase modulation is closely related to which other modulation technique?",
            "options": ["a. Amplitude Modulation (AM)", "b. Frequency Modulation (FM)", "c. Pulse-Code Modulation (PCM)", "d. Quadrature Amplitude Modulation (QAM)"],
            "answer": "b. Frequency Modulation (FM)"
        },
        {
            "question": "Q4. Which modulation technique requires the largest bandwidth? ",
            "options": ["a. AM", "b. FM", "c. PM", "d. All require the same bandwidth"],
            "answer": "b. FM"
        },
        {
            "question": "Q5. In AM, the total power transmitted is split between the carrier and:",
            "options": ["a. Sidebands", "b. Noise", "c. Phase variation", "d. Harmonics"],
            "answer": "a. Sidebands"
        }
    ]
 

def post_ans7():
    st.markdown('<div class="my-custom-text">Study and Demonstrate the Amplitude, Frequency and Phase Modulation</div>',unsafe_allow_html=True)
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

def post_warning7():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"   


