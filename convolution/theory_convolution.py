import streamlit as st

def content4():

    st.markdown('<div class="my-custom-text">Study the Linear and Circular Convolution of Two Signals</div>',unsafe_allow_html=True)
    st.divider()

    st.markdown('<div class="my-custom-h5-text">Convolution</div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">Convolution is a fundamental operation in Digital Signal Processing (DSP) used to determine the output of a Linear Time-Invariant (LTI) system. It describes how an input signal interacts with a system’s impulse response to produce an output.</p>',unsafe_allow_html=True)
    
    
    #-------------------------------#
    st.markdown('<div class="my-custom-h5-text">1. Definition</div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">Convolution is the process of flipping, shifting, and summing one signal with another. It helps in filtering, system analysis, and signal transformation.</p>',unsafe_allow_html=True)


    #-------------------------------#
    st.markdown('<div class="my-custom-h5-text">2. Mathematical Form</div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text" style="margin-left:20px">a. For continuous-time signals:</p>',unsafe_allow_html=True)

    st.latex(r'''
        y(t) = \int_{-\infty}^\infty x(\tau) h (t-\tau) d\tau
       
        ''')
    
    st.write('<p class="my-custom-sub-text" style="margin-left:20px">b. For discrete-time signals:</p>',unsafe_allow_html=True)

    st.latex(r'''
        y[n] = \sum_{k=-\infty}^\infty x[k]h[n-k]
      
        ''')
    
    st.markdown(
            '<p class="my-custom-sub-text" style="margin-left:20px">Where: <br> \
            <ul class="my-custom-sub-text" style="text-align: justify;font-size: 18px;margin-left:25px">\
            <li>x(t) or x[n] is the input signal,</li>\
            <li>h(t) or h[n] is the system’s impulse response,</li>\
            <li>y(t) or y[n] is the output signal.</li>\
            </ul></p>', unsafe_allow_html=True)


    #----------------------------------#
    st.markdown('<div class="my-custom-h5-text">3. Convolution Theorem</div>', unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-text" style="margin-left:20px">\
            <li><b>In Time Domain:</b> Convolution of two signals</li>\
            <li><b>In Frequency Domain:</b> Equivalent to multiplication</li>\
            </ul>', unsafe_allow_html=True)

    st.latex(r'''
        y(t) = x(t) * h(t)  \space\space \leftrightarrow \space\space Y(f) = X(f).H(f)
       
        ''')

    st.markdown('<div class="my-custom-sub-text">This means convolution is performed more efficiently in the frequency domain using the FFT.</div>', unsafe_allow_html=True)



    #----------------------------------#
    st.markdown('<div class="my-custom-h5-text">4. Applications of Convolution</div>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-text" style="margin-left:20px">\
            <li><b>Digital Filtering:</b> Applies an impulse response to filter unwanted frequencies.</li>\
            <li><b>Image Processing:</b> Used for edge detection, blurring, and sharpening.</li>\
            <li><b>Speech Processing:</b> Enhances speech signals by removing noise.</li>\
            <li><b>Radar & Communication Systems:</b> Improves signal clarity by matching signals with templates.</li>\
                </ul>', unsafe_allow_html=True)

    
