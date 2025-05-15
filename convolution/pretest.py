import streamlit as st

questions = [
    {
      "question": "Q1. What is the primary purpose of convolution in DSP?",
      "options": [
        "a. To find the frequency components of a signal",
        "b. To remove noise from a signal",
        "c. To determine the output of a system given an input and impulse response",
        "d. To convert a signal from the time domain to the frequency domain"
      ],
      "answer": "c. To determine the output of a system given an input and impulse response",
      "explanation": "Convolution is used to analyze linear time-invariant (LTI) systems, where the output is the convolution of the input signal with the system’s impulse response."
    },
    {
      "question": "Q2. What is the mathematical formula for continuous-time convolution?",
      "options": [
        "a. $y(t) = x(t).h(t)$",
        "b. $y(t) = x(t) + h(t)$",
        "c. $y(t) = \\int_{-\\infty}^{\\infty} x(t) h(t - \\tau) d\\tau$",
        "d. $y(t) = \sum_{k=-\infty}^\infty x[k]h[n-k]$"
      ],
      "answer": "c. $y(t) = \\int_{-\\infty}^{\\infty} x(t) h(t - \\tau) d\\tau$",
      "explanation": "Continuous-time convolution is defined as the integral of one function flipped and shifted over another function."
    },
    {
      "question": "Q3. What does the convolution operation represent in the time domain?",
      "options": [
        "a. Multiplication of signals",
        "b. Addition of signals",
        "c. Weighted sum of past inputs",
        "d. Frequency shifting"
      ],
      "answer": "c. Weighted sum of past inputs",
      "explanation": "Convolution sums weighted past values of the input signal to determine the system's response."
    },
    {
      "question": "Q4. How can convolution be implemented using hardware?",
      "options": [
        "a. Using an operational amplifier",
        "b. Using a shift register and adder",
        "c. Using a capacitor and resistor",
        "d. Using a digital-to-analog converter"
      ],
      "answer": "b. Using a shift register and adder",
      "explanation": "In digital hardware, convolution can be implemented using a shift register to store past values and an adder to sum weighted contributions."
    },
    {
      "question": "Q5. What is the impulse response of an LTI system?",
      "options": [
        "a. The system's response to a unit step input",
        "b. The system's response to an impulse input",
        "c. The system’s response in the frequency domain",
        "d. The sum of all past inputs"
      ],
      "answer": "b. The system's response to an impulse input",
      "explanation": "The impulse response characterizes an LTI system completely, as it determines how the system reacts to any input."
    }

  ]


# Initialize the user answers if not already initialized
def test4():
    # Check if 'user_answers' exists in session_state, otherwise initialize it
    if 'user_answers' not in st.session_state:
        # Initialize user_answers with 'None' for each question (based on number of questions)
        st.session_state.user_answers = [None] * 5  # Adjust the number '5' to match the number of questions

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
    
    st.markdown('<div class="my-custom-text">Study the Linear and Circular Convolution of Two Signals</div>',unsafe_allow_html=True)
    st.divider()
    st.markdown('<div class="my-custom-h3-text">Pretest</div>',unsafe_allow_html=True)

    
    # Loop over the questions and create radio buttons for each one
    for idx, question in enumerate(questions):
        # Check if the selected answer already exists in session_state
        if st.session_state.user_answers[idx] is not None:
            selected_answer = st.session_state.user_answers[idx]
        else:
            selected_answer = None
        
        # Display the question and options
        user_answer = st.radio(
            question["question"],
            question["options"],
            key=f"question_{idx}",
            index=None  # Retain selected answer if available
        )
        
        # Store the user's answer in session state
        st.session_state.user_answers[idx] = user_answer

