import streamlit as st

questions = [
      {
      "question": "Q1. Why is the Nyquist rate important in digital signal processing?",
      "options": [
        "a. It determines the resolution of an image",
        "b. It ensures that signals are not distorted due to aliasing",
        "c. It reduces the number of samples required to store a signal",
        "d. It eliminates all high-frequency components"
      ],
      "answer": "b. It ensures that signals are not distorted due to aliasing",
      "explanation": "According to the Nyquist-Shannon sampling theorem, a signal must be sampled at at least twice its highest frequency component to prevent aliasing."
    },
    {
      "question": "Q2. If a sinusoidal signal is sampled below the Nyquist rate, what phenomenon occurs?",
      "options": [
        "a. Oversampling",
        "b. Aliasing",
        "c. Quantization error",
        "d. Clipping"
      ],
      "answer": "b) Aliasing",
      "explanation": "Aliasing occurs when the sampling frequency is less than twice the highest frequency component of the signal, leading to distortion and incorrect frequency reconstruction."
    },
    {
      "question": "Q3. What is the primary advantage of using a triangular wave instead of a sinusoidal wave in some applications?",
      "options": [
        "a. It has a single frequency component",
        "b. It is easier to generate using a capacitor and resistor",
        "c. It has lower harmonic distortion",
        "d. It is more robust to noise"
      ],
      "answer": "d. It is more robust to noise",
      "explanation": "Triangular waves are often used in modulation schemes and signal testing because they are less affected by high-frequency noise compared to square waves."
    },
    {
      "question": "Q4. If a sinusoidal signal has an amplitude of 5V and frequency of 10Hz, what is its peak-to-peak voltage?",
      "options": [
        "a. 2.5V",
        "b. 5V",
        "c. 10V",
        "d. 20V"
      ],
      "answer": "c. 10V",
      "explanation": "The peak amplitude of a sinusoidal signal is A = 5V. Peak-to-peak voltage is twice the amplitude."
    },
    {
      "question": "Q5. Which signal among the following has the highest bandwidth?",
      "options": [
        "a. Sine wave",
        "b. Square wave",
        "c. Unit step",
        "d. Ramp function"
      ],
      "answer": "b. Square wave",
      "explanation": "A square wave has sharp transitions, which means it contains higher-frequency harmonics, leading to a higher bandwidth. A sine wave has only one frequency component, so it has the lowest bandwidth. Unit step and ramp functions have broad frequency components but are not periodic."
    }
]


def post_ans1():
    st.markdown('<div class="my-custom-text">Generation of Standard Signals and their Statistical Analysis</div>',unsafe_allow_html=True)
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

def post_warning1():
    st.warning("Please answer all questions before submitting.")


# Function to check answers and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct!"
    else:
        return f"Incorrect. Correct answer: {correct_answer}"
