import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy.stats import kurtosis, skew, mode
from scipy.fft import fft, ifft
from scipy.fftpack import dct, idct, dst, idst
from scipy.signal import hilbert, chirp
import pywt  # For wavelet transform
from scipy.signal import czt


# Rest of the code


# Function to generate signals
def unit_impulse(duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    impulse = np.zeros_like(t)
    impulse[len(t) // 2] = 1
    return t, impulse

def unit_step(duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return t, np.ones_like(t)

def ramp(duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return t, t

def sinusoidal(amplitude, frequency, duration, fs, phase):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return t, amplitude * np.sin(2 * np.pi * frequency * t + phase)

def square_wave(amplitude, frequency, duration, fs, phase):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return t, amplitude * np.sign(np.sin(2 * np.pi * frequency * t + phase))

def triangular_wave(amplitude, frequency, duration, fs, phase):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return t, amplitude * (2 * np.abs(2 * ((t * frequency + phase) % 1) - 1) - 1)

# Check for under-sampling
def check_undersampling(frequency, fs, duration, signal, t, is_frequency_required=True):
    if is_frequency_required and fs < 2 * frequency:
        undersampled_fs = 2 * frequency - 1
        t_undersampled = np.linspace(0, duration, int(undersampled_fs * duration), endpoint=False)
        undersampled_signal = np.interp(t_undersampled, t, signal)
        return True, undersampled_signal, t_undersampled
    return False, signal, t

# Default values
default_signal = "Unit Impulse"
default_duration = 1.0
default_fs = 1000
default_phase = 0.0
default_amp = 1.0
default_signal_2 ="None"


def reset():
    st.session_state.dur_5 = default_duration
    st.session_state.fs_5 = default_fs
    st.session_state.selectbox_5 = default_signal
    st.session_state.phase_5 = default_phase
    st.session_state.amp_5 = default_amp
    st.session_state.selectbox_5_2 = default_signal_2

# Main Streamlit Interface
def dsp_simulator5():
    st.sidebar.markdown('<p style="border-top: 2px solid  #035F8A;"></p>',unsafe_allow_html=True)
    st.markdown('<div class="my-custom-text">Spectral Analysis of Signals using Signal Transform Functions</div>',unsafe_allow_html=True)
    st.divider()
    st.sidebar.title("Signal Generation Options")

    signal_type = st.sidebar.selectbox("Select Signal Type", 
        ["Unit Impulse", "Unit Step", "Ramp", "Sinusoidal", "Square Wave", "Triangular Wave"],key="selectbox_5")

    duration = st.sidebar.number_input("Duration (seconds)", min_value=0.1, value=default_duration,key="dur_5")
    fs = st.sidebar.number_input("Sampling Rate (Hz)", min_value=100, value=default_fs,key="fs_5")
    phase_deg = st.sidebar.number_input("Phase (degrees)", min_value=-180.0, max_value=180.0, value=default_phase,key="phase_5")
    phase = np.radians(phase_deg)  # Convert degrees to radians for computation
    amplitude = st.sidebar.number_input("Amplitude", min_value=0.1, value=default_amp, key="amp_5")  

    frequency = None  
    is_frequency_required = False  

    if signal_type in ["Sinusoidal", "Square Wave", "Triangular Wave"]:
        frequency = st.sidebar.number_input("Frequency (Hz)", min_value=1, value=5)
        is_frequency_required = True

    # Generate signal
    generators = {
        "Unit Impulse": unit_impulse,
        "Unit Step": unit_step,
        "Ramp": ramp,
        "Sinusoidal": sinusoidal,
        "Square Wave": square_wave,
        "Triangular Wave": triangular_wave
    }
    
    t, signal = generators[signal_type](amplitude, frequency, duration, fs, phase) if is_frequency_required else generators[signal_type](duration, fs)

    # Check for under-sampling
    undersampled, signal_to_plot, t_to_plot = check_undersampling(frequency, fs, duration, signal, t, is_frequency_required)

    # Plot the signal
    st.markdown(f'<div class="custom-subheader">Generated {signal_type} Signal</div>', unsafe_allow_html=True)
    fig_signal = go.Figure()
    fig_signal.add_trace(go.Scatter(x=t_to_plot, y=signal_to_plot, mode="lines", name="Signal"))
    fig_signal.update_layout(
        title=f"{signal_type} Signal",
        title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ),
        title_x=0.4,
        xaxis_title="Time [μs]", 
        yaxis_title="Amplitude",
        xaxis=dict(showgrid=True),
        xaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),
        yaxis=dict(showgrid=True),
        yaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),
    )
    st.plotly_chart(fig_signal)


    # Transform selection
    #transform_type = st.sidebar.selectbox("Select Transform", ["None", "FFT", "DCT", "DST", "Hilbert", "Wavelet", "Chirp-Z"],key="selectbox_5_2")
    
    transform_type = st.sidebar.selectbox("Select Transform", ["None", "FFT", "DCT", "DST", "Hilbert", "Wavelet"],key="selectbox_5_2")

    if transform_type == "FFT":
        st.subheader("FFT Result")
        fft_signal = fft(signal)
        N = len(signal)
        fft_signal = fft_signal[:N // 2]
        freq = np.fft.fftfreq(N, 1 / fs)[:N // 2]
        fft_amplitude = np.abs(fft_signal) / N
        
        fig_fft = go.Figure()
        fig_fft.add_trace(go.Scatter(x=freq, y=fft_amplitude, mode="lines", name="FFT"))
        fig_fft.update_layout(title="FFT of the Signal", title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ),
        title_x=0.4,
        xaxis_title="Frequency [Hz]", 
        xaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),
        yaxis_title="Amplitude",
        yaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),)
        
        st.plotly_chart(fig_fft)

    elif transform_type == "DCT":
        st.subheader("DCT Result")
        dct_signal = dct(signal)

        fig_dct = go.Figure()
        fig_dct.add_trace(go.Scatter(y=dct_signal, mode="lines", name="DCT"))
        fig_dct.update_layout(title="DCT of the Signal",title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ),
        title_x=0.4, 
        xaxis_title="Samples", 
        xaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),
        yaxis_title="Amplitude",
        yaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),)
        st.plotly_chart(fig_dct)

    elif transform_type == "DST":
        st.subheader("DST Result")
        dst_signal = dst(signal)

        fig_dst = go.Figure()
        fig_dst.add_trace(go.Scatter(y=dst_signal, mode="lines", name="DST"))
        fig_dst.update_layout(title="DST of the Signal", title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ),
        title_x=0.4,
        xaxis_title="Samples", 
        xaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),
        yaxis_title="Amplitude",
        yaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),)
        st.plotly_chart(fig_dst)

    elif transform_type == "Hilbert":
        st.subheader("Hilbert Transform Result")
        hilbert_signal = hilbert(signal)

        fig_hilbert = go.Figure()
        fig_hilbert.add_trace(go.Scatter(x=t, y=np.real(hilbert_signal), mode="lines", name="Real"))
        fig_hilbert.add_trace(go.Scatter(x=t, y=np.imag(hilbert_signal), mode="lines", name="Imaginary"))
        fig_hilbert.update_layout(title="Hilbert Transform", title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ),
        title_x=0.4,
        xaxis_title="Time [s]",
        xaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),
        yaxis_title="Amplitude",
        yaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),)
        st.plotly_chart(fig_hilbert)

    elif transform_type == "Wavelet":
        st.subheader("Wavelet Transform Result")
        coeffs = pywt.wavedec(signal, 'db1')

        fig_wavelet = go.Figure()
        fig_wavelet.add_trace(go.Scatter(y=coeffs[0], mode="lines", name="Approximation"))
        fig_wavelet.add_trace(go.Scatter(y=coeffs[1], mode="lines", name="Detail"))
        fig_wavelet.update_layout(title="Wavelet Transform", title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ),
        title_x=0.4,
        xaxis_title="Samples", 
        xaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),
        yaxis_title="Amplitude",
        yaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),)
        st.plotly_chart(fig_wavelet)

    elif transform_type == "Chirp-Z":
        st.subheader("Chirp-Z Transform Result")
    
        # Define the parameters for Chirp-Z transform
        num_points = st.sidebar.number_input("Number of Points", min_value=2, max_value=1024, value=512)
        W = np.exp(2j * np.pi / num_points)  # Chirp factor, adjust if needed
    
        # Compute Chirp-Z transform
        chirp_z_signal = czt(signal, m=num_points, w=W, a=signal[0])  # Use the a argument to define initial value
    
        # Plot the Chirp-Z Transform result
        fig_chirp_z = go.Figure()
        fig_chirp_z.add_trace(go.Scatter(y=np.abs(chirp_z_signal), mode="lines", name="Chirp-Z"))
        fig_chirp_z.update_layout(title="Chirp-Z Transform", title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ),
        title_x=0.4,
        xaxis_title="Frequency [Hz]", 
        xaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),
        yaxis_title="Amplitude",
        yaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),)
        st.plotly_chart(fig_chirp_z)

    st.sidebar.divider()
    st.sidebar.button('Reset', on_click=reset)

