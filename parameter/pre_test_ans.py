import streamlit as st


# Define the MCQs and their answers
questions = [
    {
      "question": "Q1. What is the main characteristic of a unit impulse signal?",
      "options": [
        "a. It is zero everywhere except at t=0, where it is infinite",
        "b. It is a constant signal with an amplitude of 1",
        "c. It increases linearly with time",
        "d. It oscillates between +1 and -1"
      ],
      "answer": "a. It is zero everywhere except at t=0, where it is infinite",
      "explanation": "The unit impulse signal δ(t) is zero for all values of t except at t=0, where it has an infinite amplitude and an area of 1. In discrete time, it is represented as δ[n], which is 1 at n=0 and 0 elsewhere."
    },
    {
      "question": "Q2. Which of the following signals has a constant amplitude but an increasing frequency over time?",
      "options": [
        "a. Square wave",
        "b. Triangular wave",
        "c. Chirp signal",
        "d. Ramp signal"
      ],
      "answer": "c. Chirp signal",
      "explanation": "A chirp signal is a sinusoidal signal whose frequency increases or decreases over time. It is widely used in radar, sonar, and communication systems."
    },
    {
      "question": "Q3. What is the primary characteristic of a square wave?",
      "options": [
        "a. It contains only even harmonics",
        "b. It contains only odd harmonics",
        "c. It has a single frequency component",
        "d. It has an exponential decay"
      ],
      "answer": "b. It contains only odd harmonics",
      "explanation": "A square wave consists of the fundamental frequency and an infinite series of odd harmonics (3rd, 5th, 7th, etc.)."
    },
    {
      "question": "Q4. In a sinusoidal signal, what does the phase angle represent?",
      "options": [
        "a. The starting point of the wave",
        "b. The amplitude of the wave",
        "c. The frequency of the wave",
        "d. The sampling rate"
      ],
      "answer": "a. The starting point of the wave",
      "explanation": "The phase of a sinusoidal signal determines where it starts relative to time t=0. A phase shift of 90° (π/2 radians) means the sine wave starts at its maximum instead of zero."
    },
    {
      "question": "Q5. What is the fundamental difference between a unit step and a unit impulse signal?",
      "options": [
        "a. A unit step is the integral of a unit impulse",
        "b. A unit impulse is the integral of a unit step",
        "c. Both signals are identical",
        "d. A unit step is a periodic function, whereas a unit impulse is not"
      ],
      "answer": "a. A unit step is the integral of a unit impulse",
      "explanation": "A unit impulse is a derivative of the unit step function. A unit step function is the integral of a unit impulse, meaning if you integrate an impulse signal, you get a step function."
    },
]

def pre_ans1():
    st.markdown('<div class="my-custom-text">Generation of Standard Signals and their Statistical Analysis</div>',unsafe_allow_html=True)
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

def pre_warning1():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"

