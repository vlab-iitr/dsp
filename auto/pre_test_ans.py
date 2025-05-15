import streamlit as st

questions = [
    {
      "question": "Q1. Autocorrelation is a function which matches?",
      "options": {
        "a. Two same signals",
        "b. Two different signals",
        "c. One signal with its delayed version",
        "d. None of the mentioned"
      },
      "answer": "c. One signal with its delayed version"
    },
    {
      "question": "Q2. Autocorrelation is a function of?",
      "options": {
        "a. Time",
        "b. Frequency",
        "c. Time difference",
        "d. Frequency difference"
      },
      "answer": "c. Time difference"
    },
    {
      "question": "Q3. Autocorrelation is maximum at _______.",
      "options": {
        "a. Unity",
        "b. Origin",
        "c. Infinite point",
        "d. None of the mentioned"
      },
      "answer": "b. Origin"
    },
    {
      "question": "Q4. Autocorrelation function of periodic signal is equal to _______.",
      "options": {
        "a. Energy of the signal",
        "b. Power of the signal",
        "c. Its area in frequency domain",
        "d. None of the mentioned"
      },
      "answer": "b. Power of the signal"
    },
    {
      "question": "Q5. Autocorrelation is a _______ function.",
      "options": {
        "a. Real and even",
        "b. Real and odd",
        "c. Complex and even",
        "d. Complex and odd"
      },
      "answer": "a. Real and even"
    }
    
  ]
  
    
def pre_ans3():
    st.markdown('<div class="my-custom-text">Study the Autocorrelation Analysis</div>',unsafe_allow_html=True)
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

def pre_warning3():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"
    
 