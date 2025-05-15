import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy.stats import kurtosis, skew, mode
from scipy.signal import welch

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

# Compute Power Spectral Density (PSD)
def compute_psd(signal, fs):
    f, Pxx = welch(signal, fs, nperseg=1024)
    Pxx_norm = Pxx / np.max(Pxx)  # Normalize the PSD
    return f, Pxx_norm

# Default values
default_signal = "Unit Impulse"
default_duration = 1.0
default_fs = 1000
default_phase = 0.0
default_amp = 1.0


def reset():
    st.session_state.dur_2 = default_duration
    st.session_state.fs_2 = default_fs
    st.session_state.selectbox_2 = default_signal
    st.session_state.phase_2 = default_phase
    st.session_state.amp_2 = default_amp

# Main Streamlit Interface
def dsp_simulator2():
    st.sidebar.markdown('<p style="border-top: 2px solid  #035F8A;"></p>',unsafe_allow_html=True)
    st.markdown('<div class="my-custom-text">Study the Power Spectrum Analysis</div>',unsafe_allow_html=True)
    st.divider()
    st.sidebar.title("Signal Generation Options")

    signal_type = st.sidebar.selectbox("Select Signal Type", 
        ["Unit Impulse", "Unit Step", "Ramp", "Sinusoidal", "Square Wave", "Triangular Wave"], key="selectbox_2")

    duration = st.sidebar.number_input("Duration (seconds)", min_value=0.1, value=default_duration, key="dur_2")
    fs = st.sidebar.number_input("Sampling Rate (Hz)", min_value=100, value=default_fs,key="fs_2")
    phase_deg = st.sidebar.number_input("Phase (degrees)", min_value=-180.0, max_value=180.0, value=default_phase,key="phase_2")
    phase = np.radians(phase_deg)  # Convert degrees to radians for computation
    amplitude = st.sidebar.number_input("Amplitude", min_value=0.1, value=default_amp,key="amp_2")  

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

    # Compute Power Spectral Density (PSD)
    f, Pxx_norm = compute_psd(signal, fs)

    # Plot PSD
    st.markdown(f'<div class="custom-subheader">Power Spectral Density (PSD)</div>', unsafe_allow_html=True)
    fig_psd = go.Figure()
    fig_psd.add_trace(go.Scatter(x=f, y=Pxx_norm, mode="lines", name="PSD"))
    fig_psd.update_layout(
        title=f"Power Spectral Density of {signal_type} Signal",
        title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4',

        ),
        title_x=0.4,
        xaxis_title="Frequency [Hz]",
        yaxis_title="Normalized Amplitude",
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
    st.plotly_chart(fig_psd)

    st.sidebar.divider()
    st.sidebar.button('Reset', on_click=reset)

