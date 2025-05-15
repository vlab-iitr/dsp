import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.signal import butter, cheby1, ellip, freqz, firwin, lfilter

# Signal generation functions
def unit_impulse(duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    impulse = np.zeros_like(t)
    impulse[int(len(t) / 2)] = 1
    return t, impulse

def unit_step(duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    step = np.ones_like(t)
    return t, step

def ramp(duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    ramp_signal = t
    return t, ramp_signal

def sinusoidal(amplitude, frequency, duration, fs, phase):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    sinusoid = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return t, sinusoid

def square_wave(amplitude, frequency, duration, fs, phase):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    square = amplitude * np.sign(np.sin(2 * np.pi * frequency * t + phase))
    return t, square

def triangular_wave(amplitude, frequency, duration, fs, phase):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    triangle = amplitude * (2 * np.abs(2 * ((t * frequency + phase) % 1) - 1) - 1)
    return t, triangle

# Function to apply filter
def apply_filter(signal, fs, filter_type, design_method, filter_kind, cutoff, order):
    nyquist = 0.5 * fs
    normalized_cutoff = [c / nyquist for c in cutoff]

    # Design the filter
    if design_method == "Butterworth":
        try:
            b, a = butter(order, normalized_cutoff, btype=filter_type, analog=False)
        except ValueError as e:
            st.error("Please specify both the start and stop frequencies for the bandpass or bandstop filter.")
            st.sidebar.divider()
            st.sidebar.button('Reset', on_click=reset)
            st.stop()

    elif design_method == "Chebyshev":
        try:
            b, a = cheby1(order, 1, normalized_cutoff, btype=filter_type, analog=False)
        except ValueError as e:
            st.error("Please specify both the start and stop frequencies for the bandpass or bandstop filter.")
            st.sidebar.divider()
            st.sidebar.button('Reset', on_click=reset)
            st.stop()
       
    elif design_method == "Elliptic":
        try:
            b, a = ellip(order, 1, 40, normalized_cutoff, btype=filter_type, analog=False)
        except ValueError as e:
            st.error("Please specify both the start and stop frequencies for the bandpass or bandstop filter.")
            st.sidebar.divider()
            st.sidebar.button('Reset', on_click=reset)
            st.stop()
        
    elif filter_kind == "FIR":
        try:
            b = firwin(order + 1, normalized_cutoff, pass_zero=filter_type == "lowpass")
            a = 1.0  # FIR filters only use the numerator
        except ValueError as e:
            st.error("Please specify both the start and stop frequencies for the bandpass or bandstop filter.")
            st.sidebar.divider()
            st.sidebar.button('Reset', on_click=reset)
            st.stop()
       

    # Frequency response
    w, h = freqz(b, a, worN=8000, fs=fs)
    return w, h

# Default values
default_signal = "Unit Impulse"
default_duration = 1.0
default_fs = 1000
default_phase = 0.0
default_amp = 1.0
default_filter_kind = "IIR"
default_design = "Butterworth"
default_filter_type = "lowpass"
default_order = 4
default_cutoff = "10"

def reset():
    st.session_state.dur_6 = default_duration
    st.session_state.fs_6 = default_fs
    st.session_state.selectbox_6 = default_signal
    st.session_state.phase_6 = default_phase
    st.session_state.amp_6 = default_amp
    st.session_state.selectbox_6_2 = default_filter_kind
    st.session_state.selectbox_6_3 = default_design
    st.session_state.selectbox_6_4 = default_filter_type
    st.session_state.order_6 = default_order
    st.session_state.cutoff_6 = default_cutoff

# Main Streamlit interface
def dsp_simulator6():
    st.sidebar.markdown('<p style="border-top: 2px solid  #035F8A;"></p>',unsafe_allow_html=True)
    st.markdown('<div class="my-custom-text">Design of FIR and IIR Filters and Demonstrate the Filtering Operation</div>',unsafe_allow_html=True)
    st.divider()

    st.sidebar.title("Signal and Filter Options")

    # Signal selection
    signal_type = st.sidebar.selectbox("Select Signal Type", ["Unit Impulse", "Unit Step", "Ramp", "Sinusoidal", "Square Wave", "Triangular Wave"],key="selectbox_6")
    duration = st.sidebar.number_input("Duration (seconds)", min_value=0.1, value=default_duration,key="dur_6")
    fs = st.sidebar.number_input("Sampling Rate (Hz)", min_value=100, value=default_fs,key="fs_6")
    phase_deg = st.sidebar.number_input("Phase (degrees)", min_value=-180.0, max_value=180.0, value=default_phase,key="phase_6")
    phase = np.radians(phase_deg)  # Convert degrees to radians for computation
    amplitude = st.sidebar.number_input("Amplitude", min_value=0.1, value=default_amp, key="amp_6")

    frequency = None
    if signal_type in ["Sinusoidal", "Square Wave", "Triangular Wave"]:
        frequency = st.sidebar.number_input("Frequency (Hz)", min_value=1, value=5)

    # Generate the signal
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

    st.markdown(f'<div class="custom-subheader">Generated {signal_type} Signal</div>', unsafe_allow_html=True)
    fig_signal = go.Figure()
    fig_signal.add_trace(go.Scatter(x=t, y=signal, mode="lines", name="Signal"))
    fig_signal.update_layout(title=f"{signal_type} Signal",title_font=dict(
            family='Georgia',  # Set your desired font family
            size=18, 
            color='#1f77b4',
        ),
        title_x=0.5,
        xaxis_title="Time [s]", 
        yaxis_title="Amplitude",
        xaxis_title_font=dict(  # Set font properties for x-axis title
            family="Georgia",  # Set the font family for x-axis title
            size=16,  # Set font size for x-axis title
            color='#1f77b4'  # Set the color for x-axis title
        ),  

        yaxis_title_font=dict(  # Set font properties for x-axis title
            family="Georgia",  # Set the font family for x-axis title
            size=16,  # Set font size for x-axis title
            color='#1f77b4'  # Set the color for x-axis title
        ),),
        
    
    st.plotly_chart(fig_signal)

    # Filter options
    st.sidebar.title("Filter Options")
    filter_kind = st.sidebar.selectbox("Filter Type", ["IIR", "FIR"],key="selectbox_6_2")
    design_method = st.sidebar.selectbox("Design Method", ["Butterworth", "Chebyshev", "Elliptic"],key="selectbox_6_3") if filter_kind == "IIR" else None
    filter_type = st.sidebar.selectbox("Filter Category", ["lowpass", "highpass", "bandpass", "bandstop"],key="selectbox_6_4")
    order = st.sidebar.slider("Filter Order", 1, 5, value = default_order,key="order_6")
    cutoff = st.sidebar.text_input("Cutoff Frequency (Hz)", value = default_cutoff, key="cutoff_6")

    # Adding a note for the user based on filter type
    if filter_type in ["lowpass", "highpass"]:
        st.sidebar.caption("For lowpass or highpass filters, enter only one cutoff frequency (e.g., 10).")
    elif filter_type in ["bandpass", "bandstop"]:
        st.sidebar.caption("For bandpass or bandstop filters, enter two cutoff frequencies separated by a comma (e.g., 10,20).")

# Process cutoff frequencies
    cutoff = [float(c) for c in cutoff.split(",")]

    # Frequency response
    w, h = apply_filter(signal, fs, filter_type, design_method, filter_kind, cutoff, order)

    # Magnitude response
    st.markdown(f'<div class="custom-subheader">Magnitude Response</div>', unsafe_allow_html=True)
    fig_magnitude = go.Figure()
    fig_magnitude.add_trace(go.Scatter(x=w, y=20 * np.log10(abs(h)), mode="lines", name="Magnitude"))
    fig_magnitude.update_layout(title="Magnitude Response", title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ),
        title_x=0.5,
        xaxis_title="Frequency [Hz]", 
        yaxis_title="Magnitude [dB]",
        xaxis_title_font=dict(  # Set font properties for x-axis title
            family="Georgia",  # Set the font family for x-axis title
            size=16,  # Set font size for x-axis title
            color='#1f77b4'  # Set the color for x-axis title
        ),  

        yaxis_title_font=dict(  # Set font properties for x-axis title
            family="Georgia",  # Set the font family for x-axis title
            size=16,  # Set font size for x-axis title
            color='#1f77b4'  # Set the color for x-axis title
        ),)
    st.plotly_chart(fig_magnitude)

    # Phase response
    st.markdown(f'<div class="custom-subheader">Phase Response</div>', unsafe_allow_html=True)
    fig_phase = go.Figure()
    fig_phase.add_trace(go.Scatter(x=w, y=np.angle(h), mode="lines", name="Phase"))
    fig_phase.update_layout(title="Phase Response", title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ),
        title_x=0.5,
        xaxis_title="Frequency [Hz]", 
        yaxis_title="Phase [radians]",
        xaxis_title_font=dict(  # Set font properties for x-axis title
            family="Georgia",  # Set the font family for x-axis title
            size=16,  # Set font size for x-axis title
            color='#1f77b4'  # Set the color for x-axis title
        ),  

        yaxis_title_font=dict(  # Set font properties for x-axis title
            family="Georgia",  # Set the font family for x-axis title
            size=16,  # Set font size for x-axis title
            color='#1f77b4'  # Set the color for x-axis title
        ),)
    st.plotly_chart(fig_phase)

    st.sidebar.divider()
    st.sidebar.button('Reset', on_click=reset)

