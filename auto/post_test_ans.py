
import streamlit as st

# Define the MCQs and their answers
questions = [
    {
      "question": "Q1. Autocorrelation function of white noise will have?",
      "options": {
        "a. Strong peak",
        "b. Infinite peak",
        "c. Weak peak",
        "d. None of the mentioned"
      },
      "answer": "a. Strong peak"
    },
    {
      "question": "Q2. What does autocorrelation measure in a signal?",
      "options": [
        "a. The similarity between two different signals",
        "b. The similarity of a signal with a time-shifted version of itself",
        "c. The power of the signal",
        "d. The frequency response of a system"
      ],
      "answer": "b. The similarity of a signal with a time-shifted version of itself"
    },
    {
      "question": "Q3. Which of the following is always true for an autocorrelation function?",
      "options": [
        "a. It is always negative",
        "b. It is maximum at τ=0",
        "c. It is always periodic",
        "d. It is always zero for all τ"
      ],
      "answer": "b. It is maximum at τ=0"
    },
    {
      "question": "Q4. The autocorrelation function of a real-valued signal is always:",
      "options": [
        "a. Complex",
        "b. Anti-symmetric",
        "c. Symmetric",
        "d. Random"
      ],
      "answer": "c. Symmetric"
    },
    {
      "question": "Q5. The area under the autocorrelation function of an energy signal gives:",
      "options": [
        "a. Power of the signal",
        "b. Total energy of the signal",
        "c. Frequency response of the signal",
        "d. Phase information of the signal"
      ],
      "answer": "b. Total energy of the signal"
    }
  ]

def post_ans3():
    st.markdown('<div class="my-custom-text">Study the Autocorrelation Analysis</div>',unsafe_allow_html=True)
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

def post_warning3():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"

       
