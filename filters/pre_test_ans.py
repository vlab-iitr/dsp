import streamlit as st

# Define the MCQs and their answers
questions = [
        {
            "question": "Q1. FIR stands for ____?",
            "options": ["a. Finite Impulse Filter",
                        "b. Infinite Impulse Filter",
                        "c. Finite Impedance Filter",
                        "d. Finite Impulse Fire"],
            "answer": "a. Finite Impulse Filter",
            "feedback":""
        },
        {
            "question": "Q2. Which of the following is the impulse response of FIR filter?",
            "options": ["a. Infinite", "b. Finite", "c. Zero", "d. Negative"],
            "answer": "b. Finite",
            "feedback":""
        },
        {
            "question": "Q3. Which windowing technique is primarily used for designing FIR filters with a very specific frequency response shape?",
            "options": ["a. Rectangular window", "b. Hamming window", "c. Kaiser window", "d. Bartlett window"],
            "answer": "c. Kaiser window",
            "feedback":""
        },
        {
            "question": "Q4. Which of the following is an advantage of using FIR filters over IIR filters? ",
            "options": ["a. FIR filters have linear phase response",
                        "b. FIR filters require fewer coefficients",
                        "c. FIR filters can be easily implemented with feedback loops", 
                        "d. FIR filters are more computationally efficient "],
            "answer": "a. FIR filters have linear phase response",
            "feedback":""
        },
        {
            "question": "Q5. Which of the following are the components used in FIR filter?",
            "options": [
                "a. Adders",
                "b. Multipliers",
                "c. Logic gates",
                "d. All the above"
            ],
            "answer": "d. All the above",
            "feedback":""
        }
    ]

    
def pre_ans6():
    st.markdown('<div class="my-custom-text">Design of FIR and IIR Filters and Demonstrate the Filtering Operation</div>',unsafe_allow_html=True)
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

def pre_warning6():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"
    
 