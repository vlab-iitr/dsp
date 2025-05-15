import streamlit as st

def content6():
    st.markdown('<div class="my-custom-text">Design of FIR and IIR Filters and Demonstrate the Filtering Operation</div>',unsafe_allow_html=True)
    st.divider()

    st.write('<p class="my-custom-sub-text">Filters are used in DSP to remove or allow specific frequency components in a signal. \
             They help in reducing noise, improving clarity, and extracting useful information from signals.</p>',unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-h5-text">Types of Filters:</div>',unsafe_allow_html=True)
    st.markdown('<ul class="my-custom-sub-text">\
                <li>Lowpass Filter (LPF) – Allows low frequencies to pass and blocks high frequencies (e.g., removing high-frequency noise from audio).</li>\
                <li>Highpass Filter (HPF) – Allows high frequencies and removes low frequencies (e.g., removing background hum from recordings).</li>\
                <li>Bandpass Filter (BPF) – Allows a specific frequency range to pass and blocks everything else (e.g., radio tuning).</li>\
                <li>Bandstop Filter (Notch Filter) – Removes a specific unwanted frequency while allowing others (e.g., removing 50 Hz power-line noise).</li>\
                </ul>',
                unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-h5-text">Types of Filter Designs:</div>',unsafe_allow_html=True)

    st.markdown('<div class="my-custom-h5-text">1. Infinite Impulse Response (IIR) Filter</div>',unsafe_allow_html=True)
    st.markdown('<ul class="my-custom-sub-text">\
                <li>IIR systems have an impulse response function that is non-zero over an infinite length of time, whereas FIR filters have a fixed-duration impulse response.</li>\
                <li>IIR filters use feedback, require fewer computations, but may cause phase distortion (e.g., Butterworth, Chebyshev, Elliptic filters).</li>\
                <li>IIR filters may be implemented as either analog or digital filters.</li>\
                <li>Digital filters are implemented in terms of the difference equation as given below:</li>\
                 </ul>', unsafe_allow_html=True)

    st.latex(r'''
        y[n] = 
        \frac{1}{a_{0}} \left(b_0x[n] + b_1x[n-1]+ \dots+ b_px[n-p] - a_1y[n-1] - a_2y[n-2] - \dots - a_qy[n-q]\right)
       
        ''')

    st.markdown(
                '<p class="my-custom-sub-text"">Where: <br> \
                &emsp; p is the feedforward filter order,<br> \
                &emsp; b<sub>i</sub> is the feedforward filter coefficients,<br> \
                &emsp; q is the feedback filter order,<br> \
                &emsp; a<sub>i</sub> are the feedback filter coefficients, <br> \
                &emsp; x[n] is the input signal and <br> \
                &emsp; y[n] is the output signal.  </p>', unsafe_allow_html=True)

    st.markdown('<div class="my-custom-h5-text">2. Finite Impulse Response (FIR) Filter</div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text"">FIR filters do not use feedback, provide a linear phase response, but need more computations (used in audio and image processing).</p>',unsafe_allow_html=True)
    st.markdown('<p class="my-custom-sub-text"">To study any filter we plot 2 graphs:</p>',unsafe_allow_html=True)
    
    st.markdown('<ul class="my-custom-sub-text"">\
                <li>Magnitude Response Curve (magnitude vs. frequency curve)</li>\
                <li>Phase Response Curve (phase vs. frequency curve)</li>\
                 </ul>', unsafe_allow_html=True)
    

    st.write('<p class="my-custom-sub-text"">The difference equation that defines the output of an FIR filter in terms of its input is:</p>',unsafe_allow_html=True)

    st.latex(r'''
        y[n] = 
        b_0x[n] + b_1x[n-1]+ \dots+ b_Nx[n-N] 
        
        ''')

    st.markdown(
                '<p class="my-custom-sub-text"">Where: <br> \
                &emsp; x[n] is the input signal,<br> \
                &emsp; y[n] is the output signal,<br> \
                &emsp; b<sub>i</sub> are the filter coefficients, also known as tap weights and<br> \
                &emsp; N is the filter order - an N<sup>th</sup> order filter has (N+1) terms on the right-hand side.<br> \
                </p>', unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-h5-text">Key Terms:</div>',unsafe_allow_html=True)
    st.markdown('<ul class="my-custom-sub-text"">\
                <li>Cutoff Frequency – The point where the filter starts blocking frequencies.</li>\
                <li>Order of the Filter – Higher order means a sharper transition but more computation.</li>\
                <li>Anti-aliasing Filter – A lowpass filter used before sampling a signal to prevent distortion.</li>\
                 </ul>', unsafe_allow_html=True)

