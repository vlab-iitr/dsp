import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.signal import correlate, square, sawtooth

# Function to compute autocorrelation
def compute_autocorrelation(signal):
    autocorr = correlate(signal, signal, mode='full')
    lags = np.arange(-len(signal) + 1, len(signal))
    return lags, autocorr

# Function to generate different signals
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
    return t, amplitude * square(2 * np.pi * frequency * t + phase)

def triangular_wave(amplitude, frequency, duration, fs, phase):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return t, amplitude * sawtooth(2 * np.pi * frequency * t + phase, 0.5)

# Default values
default_signal = "Unit Impulse"
default_duration = 1.0
default_fs = 1000
default_phase = 0
default_amp = 1.0
default_checkbox_value = False

def reset():
    st.session_state.dur_3 = default_duration
    st.session_state.fs_3 = default_fs
    st.session_state.selectbox_3 = default_signal
    st.session_state.phase_3 = default_phase
    st.session_state.amp_3 = default_amp
    st.session_state.checkbox = default_checkbox_value 

# Main Streamlit Interface
def dsp_simulator3():
    st.sidebar.markdown('<p style="border-top: 2px solid  #035F8A;"></p>',unsafe_allow_html=True)
    st.markdown('<div class="my-custom-text">Study the Autocorrelation Analysis</div>',unsafe_allow_html=True)
    st.divider()
    st.sidebar.title("Signal Options")


    signal_type = st.sidebar.selectbox("Select Signal Type", 
        ["Unit Impulse", "Unit Step", "Ramp", "Sinusoidal", "Square Wave", "Triangular Wave"], key = "selectbox_3")
    duration = st.sidebar.number_input("Duration (s)", 0.1, 10.0, value=default_duration,key="dur_3")
    fs = st.sidebar.number_input("Sampling Rate (Hz)", 100, 10000, value=default_fs,key="fs_3")
    amplitude = st.sidebar.number_input("Amplitude", 0.1, 10.0, value=default_amp, key="amp_3")
    phase = np.radians(st.sidebar.number_input("Phase (°)", -180, 180, value=default_phase,key="phase_3"))
    
    frequency = None
    if signal_type in ["Sinusoidal", "Square Wave", "Triangular Wave"]:
        frequency = st.sidebar.number_input("Frequency (Hz)", 1, 500, 10)
    
    # Generate signal
    if signal_type == "Unit Impulse":
        t, signal = unit_impulse(duration, fs)
    elif signal_type == "Unit Step":
        t, signal = unit_step(duration, fs)
    elif signal_type == "Ramp":
        t, signal = ramp(duration, fs)
    elif signal_type == "Sinusoidal":
        t, signal = sinusoidal(amplitude, frequency, duration, fs, phase)
    elif signal_type == "Square Wave":
        t, signal = square_wave(amplitude, frequency, duration, fs, phase)
    elif signal_type == "Triangular Wave":
        t, signal = triangular_wave(amplitude, frequency, duration, fs, phase)
    
    # Plot Signal
    fig_signal = go.Figure()
    fig_signal.add_trace(go.Scatter(x=t, y=signal, mode="lines", name="Signal"))
    fig_signal.update_layout(title=f"{signal_type} Signal",
            title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ), xaxis_title="Time [s]",
        xaxis_title_font=dict(  # Set font properties for x-axis title
            family="Georgia",  # Set the font family for x-axis title
            size=16,  # Set font size for x-axis title
            color='#1f77b4',  # Set the color for x-axis title
            
        ),
            title_x=0.5,
          yaxis_title="Amplitude",
          yaxis_title_font=dict(  # Set font properties for x-axis title
            family="Georgia",  # Set the font family for x-axis title
            size=16,  # Set font size for x-axis title
            color='#1f77b4'  # Set the color for x-axis title
        ),)
    st.plotly_chart(fig_signal)

    # Enable autocorrelation
    if st.sidebar.checkbox("Show Autocorrelation", value=default_checkbox_value, key='checkbox'):
        lags, autocorr = compute_autocorrelation(signal)
        fig_autocorr = go.Figure()
        fig_autocorr.add_trace(go.Scatter(x=lags, y=autocorr, mode="lines", name="Autocorrelation"))
        fig_autocorr.update_layout(title=f"Autocorrelation of {signal_type}",
            title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ),
          title_x=0.4,
          xaxis_title="Lag", 
          xaxis_title_font=dict(  # Set font properties for x-axis title
            family="Georgia",  # Set the font family for x-axis title
            size=16,  # Set font size for x-axis title
            color='#1f77b4'  # Set the color for x-axis title
        ),
        yaxis_title="Correlation",
        yaxis_title_font=dict(  # Set font properties for x-axis title
            family="Georgia",  # Set the font family for x-axis title
            size=16,  # Set font size for x-axis title
            color='#1f77b4'  # Set the color for x-axis title
        ),)
        st.plotly_chart(fig_autocorr)

    st.sidebar.divider()
    st.sidebar.button('Reset', on_click=reset)





