import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

# Function to generate unit impulse
def unit_impulse(duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    impulse = np.zeros_like(t)
    impulse[int(len(t) / 2)] = 1  # Impulse at the center
    return t, impulse

# Function to generate unit step
def unit_step(duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    step = np.ones_like(t)  # Step signal with constant value 1
    return t, step

# Function to generate ramp
def ramp(duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    ramp_signal = t  # Ramp signal increases linearly over time
    return t, ramp_signal

# Function to generate sinusoidal wave with amplitude
def sinusoidal(amplitude, frequency, duration, fs, phase):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    sinusoid = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return t, sinusoid

# Function to generate square wave with amplitude
def square_wave(amplitude, frequency, duration, fs, phase):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    square = amplitude * np.sign(np.sin(2 * np.pi * frequency * t + phase))
    return t, square

# Function to generate triangular wave with amplitude
def triangular_wave(amplitude, frequency, duration, fs, phase):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    triangle = amplitude * (2 * np.abs(2 * ((t * frequency + phase) % 1) - 1) - 1)
    return t, triangle

# Function to check for under-sampling
def check_undersampling(frequency, fs, duration, signal, t, is_frequency_required=True):
    if is_frequency_required and fs < 2 * frequency:  # Check if below Nyquist rate
        undersampled_fs = 2 * frequency - 1  # Just below Nyquist rate
        t_undersampled = np.linspace(0, duration, int(undersampled_fs * duration), endpoint=False)
        undersampled_signal = np.interp(t_undersampled, t, signal)
        return True, undersampled_signal, t_undersampled
    return False, signal, t

# Linear Convolution Function
def linear_convolution(x, h):
    return np.convolve(x, h, mode='full')

# Circular Convolution Function
def circular_convolution(x, h):
    N = max(len(x), len(h))  # Ensure correct length for FFT
    return np.fft.ifft(np.fft.fft(x, N) * np.fft.fft(h, N)).real  # Take real part

# Function to plot Power Spectral Density (PSD)
def plot_psd(signal, fs):
    f, Pxx_den = scipy.signal.welch(signal, fs)
    plt.figure(figsize=(10, 4))
    plt.semilogy(f, Pxx_den)
    plt.title('Power Spectral Density (PSD)')
    plt.title_font=dict(
            family="Georgia, serif;",  # Set your desired font family
            size=18,                    # Set the font size
        )
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('PSD [V²/Hz]')
    plt.grid(True)
    st.pyplot(plt)

# Default values
default_signal = "Unit Impulse"
default_duration = 1.0
default_fs = 1000
default_phase = 0.0
default_amp = 1.0
default_signal_2 = "None"


def reset():
    st.session_state.dur_4 = default_duration
    st.session_state.fs_4 = default_fs
    st.session_state.selectbox_4 = default_signal
    st.session_state.phase_4 = default_phase
    st.session_state.amp_4 = default_amp
    st.session_state.dur_4_2 = default_duration
    st.session_state.fs_4_2 = default_fs
    st.session_state.selectbox_4_2_1 = default_signal_2
    st.session_state.phase_4_2 = default_phase
    st.session_state.amp_4_2 = default_amp

# Main Streamlit DSP Simulator
def dsp_simulator4():
    st.sidebar.markdown('<p style="border-top: 2px solid  #035F8A;"></p>',unsafe_allow_html=True)
    st.markdown('<div class="my-custom-text">Study the Linear and Circular Convolution of Two Signals</div>',unsafe_allow_html=True)
    st.divider()
    st.sidebar.title("Signal Generation Options")

    # Select Signal Type
    signal_type = st.sidebar.selectbox("Select Signal Type", ["Unit Impulse", "Unit Step", "Ramp", "Sinusoidal", "Square Wave", "Triangular Wave"],key="selectbox_4")

    # Input parameters
    duration = st.sidebar.number_input("Duration (seconds)", min_value=0.1, value=default_duration,key="dur_4")
    fs = st.sidebar.number_input("Sampling Rate (Hz)", min_value=100, value=default_fs,key="fs_4")
    phase_deg = st.sidebar.number_input("Phase (degrees)", min_value=-180.0, max_value=180.0, value=default_phase,key="phase_4")
    phase = np.radians(phase_deg)  # Convert degrees to radians

    amplitude = st.sidebar.number_input("Amplitude", min_value=0.1, value=default_amp, key="amp_4")  
    frequency = None  # Default
    is_frequency_required = False  

    if signal_type in ["Sinusoidal", "Square Wave", "Triangular Wave"]:
        frequency = st.sidebar.number_input("Frequency (Hz)", min_value=1, value=5)
        is_frequency_required = True

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

    # Check for under-sampling
    undersampled, signal_to_plot, t_to_plot = check_undersampling(frequency, fs, duration, signal, t, is_frequency_required)

    # Plot Signal
    st.markdown(f'<div class="custom-subheader">Generated {signal_type} Signal</div>', unsafe_allow_html=True)
    plt.figure(figsize=(10, 4))
    plt.plot(t_to_plot, signal_to_plot)
    plt.title(f"{signal_type} Signal",fontname='Georgia', fontsize=14,color='#1f77b4')
    plt.xlabel("Time [s]",fontname='Georgia', fontsize=12,color='#1f77b4')
    plt.ylabel("Amplitude",fontname='Georgia', fontsize=12,color='#1f77b4')
    plt.grid(True)
    st.pyplot(plt)

    # Convolution Options
    st.sidebar.title("Convolution Options")
    convolution_type = st.sidebar.selectbox("Select Convolution Type", ["None", "Linear Convolution", "Circular Convolution"],key="selectbox_4_2_1")

    if convolution_type != "None":
        st.subheader(f"{convolution_type} Result")

        # Second Signal Parameters
        signal_type_2 = st.sidebar.selectbox("Select Second Signal", ["Unit Impulse", "Unit Step", "Ramp", "Sinusoidal", "Square Wave", "Triangular Wave"], key="selectbox_4_2")
        duration_2 = st.sidebar.number_input("Second Signal Duration (seconds)", min_value=0.1, value=default_duration,key="dur_4_2")
        fs_2 = st.sidebar.number_input("Second Signal Sampling Rate (Hz)", min_value=100, value=default_fs,key="fs_4_2")
        phase_2 = np.radians(st.sidebar.number_input("Second Signal Phase (degrees)", min_value=-180.0, max_value=180.0,value=default_phase,key="phase_4_2"))
        amplitude_2 = st.sidebar.number_input("Second Signal Amplitude", min_value=0.1, value=default_amp, key="amp_4_2")

        frequency_2 = None
        is_frequency_required_2 = False

        if signal_type_2 in ["Sinusoidal", "Square Wave", "Triangular Wave"]:
            frequency_2 = st.sidebar.number_input("Second Signal Frequency (Hz)", min_value=1, value=5)
            is_frequency_required_2 = True

        # Generate Second Signal
        if signal_type_2 == "Unit Impulse":
            t_2, signal_2 = unit_impulse(duration_2, fs_2)
        elif signal_type_2 == "Unit Step":
            t_2, signal_2 = unit_step(duration_2, fs_2)
        elif signal_type_2 == "Ramp":
            t_2, signal_2 = ramp(duration_2, fs_2)
        elif signal_type_2 == "Sinusoidal":
            t_2, signal_2 = sinusoidal(amplitude_2, frequency_2, duration_2, fs_2, phase_2)
        elif signal_type_2 == "Square Wave":
            t_2, signal_2 = square_wave(amplitude_2, frequency_2, duration_2, fs_2, phase_2)
        elif signal_type_2 == "Triangular Wave":
            t_2, signal_2 = triangular_wave(amplitude_2, frequency_2, duration_2, fs_2, phase_2)

        # Perform Convolution
        convolved_signal = linear_convolution(signal, signal_2) if convolution_type == "Linear Convolution" else circular_convolution(signal, signal_2)

    
        # Combined plot for both signals with different colors
        plt.figure(figsize=(10, 4))
        plt.plot(t_to_plot * 1e6, signal_to_plot, label="First Signal", color='blue')  
        plt.plot(t_2 * 1e6, signal_2, label="Second Signal", color='orange')  
        plt.title(f"Comparison of {signal_type} Signal and Second Signal",fontname='Georgia',  # Set your desired font family
            size=18, color='#1f77b4'  )
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)

        # Plot the convolution result
        plt.figure(figsize=(10, 4))
        plt.plot(np.linspace(0, duration + duration_2, len(convolved_signal)), convolved_signal)
        plt.title(f"{convolution_type} Result",fontname='Georgia',  # Set your desired font family
            size=18,color='#1f77b4'   )
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.grid(True)
        st.pyplot(plt)

    st.sidebar.divider()
    st.sidebar.button('Reset', on_click=reset)

