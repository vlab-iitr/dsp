import streamlit as st
from PIL import Image

def content2():
    st.markdown('<div class="my-custom-text">Study the Power Spectrum Analysis</div>',unsafe_allow_html=True)
    st.divider()
    image_path1 = 'spectrum/power.jpg'  # Replace with your image path
    image = Image.open(image_path1)
    def image_to_base64(image_path):
        import base64
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
        
    st.markdown('<p class="my-custom-sub-text">Power Spectrum shows frequencies containing the signal\'s power, by plotting a \
                distribution of power values as a function of frequency, where "power" is considered to be the average of the signal². \
                For a given signal, the power spectrum gives a plot of the portion of a signal\'s power (energy per unit time) \
                falling within given frequency bins. The most common way of generating a power spectrum is by using a Discrete Fourier Transform, \
                but other techniques such as the maximum entropy method can also be used.\
                <figure style="text-align: center;">\
                <img src="data:image/png;base64,{}" alt="Centered Image"><br>\
                <figcaption style="font-size:18px;font-weight:bold;font-family: Georgia, serif;">Fig.1 Power Spectrum</figcaption>\
                </figure>\
                </p>'.format(image_to_base64(image_path1)),unsafe_allow_html=True)
    
    
    
        