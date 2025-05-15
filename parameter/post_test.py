import streamlit as st

# Define the MCQs and their answers
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


# Initialize the user answers if not already initialized
def post1():
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
    st.markdown('<div class="my-custom-h3-text">Posttest</div>',unsafe_allow_html=True)
    
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

