import streamlit as st

# Define the MCQs and their answers
questions = [
        {
            "question": "Q1. FIR filters operate on ___ type of input values?",
            "options": [
                "a. Present",
                "b. Past",
                "c. Next",
                "d. Both a and b"
            ],
            "answer": "d. Both a and b",
            "feedback":""
        },
        {
             "question": "Q2. FIR filter implements _____ transfer function?",
            "options": [
                "a. Zero",
                "b. Uni",
                "c. Bi",
                "d. Multi"
            ],
            "answer": "a. Zero",
            "feedback":""
        },
        {
            "question": "Q3. In this type of designing, the system function of IIR filter is expressed in which form?",
            "options": [
                "a. Parallel form",
                "b. Cascade form",
                "c. Mixed form",
                "d. Any of the mentioned"
            ],
            "answer": "b. Cascade form",
            "feedback":""
        },
        {
            "question": "Q4. Filters allow transmission of signals in a ____________.",
            "options": [
                "a. Certain band of frequencies",
                "b. Out of the band the frequencies will be rejected",
                "c. Both a and b",
                "d. None of the above"
            ],
            "answer": "a. Certain band of frequencies",
            "feedback":""
        },
        {
            "question": "Q5. Which technique is commonly used for designing IIR filters that maintains the frequency response of analog filters?",
            "options": [
                "a. Impulse invariant transformation",
                "b. Fourier transformation",
                "c. Rectangular windowing",
                "d. Bilinear transformation"
            ],
            "answer": "d. Bilinear transformation",
            "feedback":""
        }
    ]
 
    
def post_ans6():
    st.markdown('<div class="my-custom-text">Design of FIR and IIR Filters and Demonstrate the Filtering Operation</div>',unsafe_allow_html=True)
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

def post_warning6():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"