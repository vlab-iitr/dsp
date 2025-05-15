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


# Initialize the user answers if not already initialized
def test1():
    # Check if 'user_answers' exists in session_state, otherwise initialize it
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = [None] * 5  # Adjust this number based on the number of questions   
    
    st.markdown(
    """
    <style>
        p {
            font-family: Georgia, serif;
        }
    </style>
    """, 
    unsafe_allow_html=True
    )

    st.markdown('<div class="my-custom-text">Generation of Standard Signals and their Statistical Analysis</div>',unsafe_allow_html=True)
    st.divider()
    st.markdown('<div class="my-custom-h3-text">Pretest</div>',unsafe_allow_html=True)

    # Display MCQs
    for idx, question in enumerate(questions):
        # Display the question and options
        user_answer = st.radio(
            question["question"],
            question["options"],
            key=f"question_{idx}",
            index=None 
        )
        # Store the user's answer in session state
        st.session_state.user_answers[idx] = user_answer
    


        


