import streamlit as st

def content3():

    st.markdown('<div class="my-custom-text">Study the Autocorrelation Analysis</div>',unsafe_allow_html=True)
    st.divider()

    st.markdown('<div class="my-custom-h5-text">Autocorrelation of a Signal </div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">Autocorrelation is a fundamental concept in signal processing that measures the similarity \
             between a signal and a time-shifted version of itself. \
             It provides information about the periodicity and structure of the signal. </p>',unsafe_allow_html=True)
    
    #-------------------------------#
       
    #-------------------------------#
    st.markdown('<div class="my-custom-h5-text">1. Mathematical Form</div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text" style="margin-left:20px">a. For a continuous-time signal x(t), the autocorrelation function is defined as: </p>',unsafe_allow_html=True)

    st.latex(r'''
        R_x(\tau) = \int_{-\infty}^\infty x(t) x (t+\tau) d\tau
       
        ''')
    
    st.write('<p class="my-custom-sub-text" style="margin-left:40px">where, τ is the time shift (lag).</p>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text" style="margin-left:20px">b. For a discrete-time signal x[n], the autocorrelation function is given by: </p>',unsafe_allow_html=True)

    st.latex(r'''
        R_x(k) = \sum_{n=-\infty}^\infty x[n]x[n+k]
      
        ''')
    
   

    #----------------------------------#
    st.markdown('<div class="my-custom-h5-text">2. Properties of Autocorrelation</div>',unsafe_allow_html=True)

    st.markdown('<ol class="my-custom-sub-text" style="margin-left:20px">\
            <li><b>Even Function:</b> R<sub>x</sub>(τ)=R<sub>x</sub>(−τ), meaning the function is symmetric about τ=0.</li>\
            <li><b>Maximum at Zero Lag:</b> The autocorrelation function has its highest value at τ=0, meaning the signal has maximum similarity with itself.</li>\
            <li><b>Periodic for Periodic Signals:</b> If x(t) is periodic with period T, then R<sub>x</sub>​(τ) is also periodic with the same period T. </li>\
            <li><b>Related to Power Spectrum:</b> The power spectral density (PSD) of a signal is the Fourier transform of its autocorrelation function (Wiener-Khinchin theorem).</li>\
                </ol>', unsafe_allow_html=True)

    #----------------------------------#
    st.markdown('<div class="my-custom-h5-text">3. Applications of Autocorrelation </div>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-text" style="margin-left:20px">\
            <li>Detection of periodicity in signals. </li>\
            <li>Feature extraction in speech and image processing.</li>\
            <li>Noise reduction and signal estimation in communication systems. </li>\
            <li>Time-delay estimation in radar and sonar applications.</li>\
                </ul>', unsafe_allow_html=True)