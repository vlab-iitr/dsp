import streamlit as st

# Define the MCQs and their answers
questions = [
        {
            "question": "Q1. What is the purpose of modulation in communication systems?",
            "options": ["a. To eliminate noise from the signal ",
                        "b. To increase the frequency of the signal",
                        "c. To encode information onto a carrier wave for transmission",
                        "d. To amplify the transmitted signal "],
            "answer": "c. To encode information onto a carrier wave for transmission",
            "feedback":""
        },
        {
            "question": "Q2. Which of the following is NOT a modulation technique? ",
            "options": ["a. Amplitude Modulation (AM)", "b. Frequency Modulation (FM)", "c. Pulse Modulation (PM)", "d. Analog Multiplexing"],
            "answer": "d. Analog Multiplexing",
            "feedback":""
        },
        {
            "question": "Q3. Which of the following is an application of AM?",
            "options": ["a. Satellite communication", "b. AM radio broadcasting", "c. Wi-Fi communication", "d. Mobile telephony"],
            "answer": "b. AM radio broadcasting",
            "feedback":""
        },
        {
            "question": "Q4. In FM, the parameter of the carrier wave that is varied is:",
            "options": ["a. Amplitude", "b. Frequency", "c. Phase", "d. Wavelength"],
            "answer": "b. Frequency",
            "feedback":""
        },
        {
            "question": "Q5. In PM, the parameter of the carrier wave that is varied is:",
            "options": ["a. Frequency", "b. Amplitude", "c. Phase", "d. Wavelength"],
            "answer": "c. Phase",
            "feedback":""
        }
    ]
  
    
def pre_ans7():
    st.markdown('<div class="my-custom-text">Design of FIR and IIR Filters (LPF/HPF/BPF/BSF) and Demonstrate the Filtering Operation</div>',unsafe_allow_html=True)
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

def pre_warning7():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"

