import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, butter, filtfilt, square, sawtooth

# Function to generate message signal
def generate_message(amplitude, frequency, duration, fs, phase, signal_type):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    if signal_type == "Sine Wave":
        return t, amplitude * np.sin(2 * np.pi * frequency * t + phase)
    elif signal_type == "Square Wave":
        return t, amplitude * square(2 * np.pi * frequency * t + phase)
    elif signal_type == "Triangular Wave":
        return t, amplitude * sawtooth(2 * np.pi * frequency * t + phase, 0.5)

# Function to generate carrier signal
def carrier_wave(amplitude, frequency, duration, fs, phase):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return t, amplitude * np.cos(2 * np.pi * frequency * t + phase)

# Function to apply amplitude modulation
def amplitude_modulation(message, carrier, mod_type):
    if mod_type == "DSB-WC":
        modulated = (1 + message) * carrier
    elif mod_type == "DSB-SC":
        modulated = message * carrier
    elif mod_type == "SSB-USB":
        analytic_signal = hilbert(message)
        modulated = np.real((message + 1j * analytic_signal) * carrier)
    elif mod_type == "SSB-LSB":
        analytic_signal = hilbert(message)
        modulated = np.real((message - 1j * analytic_signal) * carrier)
    return modulated

# Function to apply frequency modulation
def frequency_modulation(message, carrier_frequency, fs, modulation_index):
    t = np.linspace(0, len(message) / fs, len(message), endpoint=False)
    integral_message = np.cumsum(message) / fs
    return np.cos(2 * np.pi * carrier_frequency * t + modulation_index * integral_message)

# Function to apply phase modulation
def phase_modulation(message, carrier_frequency, fs, modulation_index):
    t = np.linspace(0, len(message) / fs, len(message), endpoint=False)
    return np.cos(2 * np.pi * carrier_frequency * t + modulation_index * message)

# Low-pass filter for demodulation
def low_pass_filter(signal, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, signal)

# Default values
default_modulation="Amplitude Modulation"
default_msg = "Sine Wave"

default_amp = 1.0
default_frq = 5
default_duration = 1.0
default_cFrq = 100
default_mod="DSB-WC"


def reset():
    st.session_state.selectbox_7_1 = default_modulation
    st.session_state.dur_7 = default_duration
    st.session_state.frq_7 = default_frq
    st.session_state.amp_7 = default_amp
    st.session_state.selectbox_7_2 = default_msg
    st.session_state.amp_7_2 = default_amp
    st.session_state.cFrq_7 = default_cFrq
    st.session_state.selectbox_7_3 = default_mod
    st.session_state.cFrq_7_2 = default_cFrq
    st.session_state.cFrq_7_3 = default_cFrq


# Main Streamlit interface
def dsp_simulator7():
    st.sidebar.markdown('<p style="border-top: 2px solid  #035F8A;"></p>',unsafe_allow_html=True)
    st.markdown('<div class="my-custom-text">Study and Demonstrate the Amplitude, Frequency and Phase Modulation</div>',unsafe_allow_html=True)
    st.divider()
    st.sidebar.title("Signal Generation Options")
    
    modulation_category = st.sidebar.selectbox("Select Modulation Category", ["Amplitude Modulation", "Frequency Modulation", "Phase Modulation"],key="selectbox_7_1")
    
    msg_amplitude = st.sidebar.number_input("Message Amplitude", min_value=0.1, value=default_amp, key="amp_7")
    msg_frequency = st.sidebar.number_input("Message Frequency (Hz)", min_value=1, value=default_frq, key="frq_7")
    duration = st.sidebar.number_input("Duration (seconds)", min_value=0.1, value = default_duration, key="dur_7")
    fs = 10000
    message_type = st.sidebar.selectbox("Select Message Signal Type", ["Sine Wave", "Square Wave", "Triangular Wave"],key="selectbox_7_2")
    
    t, message = generate_message(msg_amplitude, msg_frequency, duration, fs, 0, message_type)
    
    if modulation_category == "Amplitude Modulation":
        carrier_amplitude = st.sidebar.number_input("Carrier Amplitude", min_value=0.1, value=default_amp, key="amp_7_2")
        carrier_frequency = st.sidebar.number_input("Carrier Frequency (Hz)", min_value=10, value=default_cFrq,key="cFrq_7" )
        mod_type = st.sidebar.selectbox("Select AM Type", ["DSB-WC", "DSB-SC", "SSB-USB", "SSB-LSB"],key="selectbox_7_3")
        _, carrier = carrier_wave(carrier_amplitude, carrier_frequency, duration, fs, 0)
        modulated_signal = amplitude_modulation(message, carrier, mod_type)
    
    elif modulation_category == "Frequency Modulation":
        carrier_frequency = st.sidebar.number_input("Carrier Frequency (Hz)", min_value=10, value=default_cFrq, key="cFrq_7_2")
        modulation_index = st.sidebar.number_input("Modulation Index", min_value=0.1, value=1.0)
        modulated_signal = frequency_modulation(message, carrier_frequency, fs, modulation_index)
    
    elif modulation_category == "Phase Modulation":
        carrier_frequency = st.sidebar.number_input("Carrier Frequency (Hz)", min_value=10, value=default_cFrq, key="cFrq_7_3")
        modulation_index = st.sidebar.number_input("Modulation Index", min_value=0.1, value=1.0)
        modulated_signal = phase_modulation(message, carrier_frequency, fs, modulation_index)
    
    before_lpf = modulated_signal * message
    demodulated_signal = low_pass_filter(before_lpf, msg_frequency * 2, fs)
    cross_correlation = np.correlate(modulated_signal, message, mode='same')
    
    fig, axes = plt.subplots(6, 1, figsize=(10, 12))
    axes[0].plot(t, message, label="Message Signal", color='b')
    axes[0].set_title("Message Signal",fontsize=14, family="Georgia",color='b', loc='center')
    axes[0].grid()
    
    axes[1].plot(t, modulated_signal, label=f"{modulation_category} Modulated Signal", color='r')
    axes[1].set_title(f"{modulation_category} Modulated Signal",fontsize=14, family="Georgia",color='r', loc='center')
    axes[1].grid()
    
    axes[2].plot(t, message, label="Carrier Signal", color='g')
    axes[2].set_title("Carrier Signal",fontsize=14, family="Georgia",color='g', loc='center')
    axes[2].grid()
    
    axes[3].plot(t, before_lpf, label="Before LPF", color='c')
    axes[3].set_title("Before Low-Pass Filter",fontsize=14, family="Georgia",color='c', loc='center')
    axes[3].grid()
    
    axes[4].plot(t[:len(cross_correlation)], cross_correlation, label="Cross-Correlation", color='m')
    axes[4].set_title("Cross-Correlation",fontsize=14, family="Georgia",color='m', loc='center')
    axes[4].grid()
    
    axes[5].plot(t, demodulated_signal, label="Demodulated Signal", color='orange')
    axes[5].set_title("Demodulated Signal",fontsize=14, family="Georgia",color='orange', loc='center')
    axes[5].grid()

    if modulation_category == "Amplitude Modulation":
        modulation_index = msg_amplitude / carrier_amplitude
        st.markdown(f'<div class="custom-subheader">Modulation Index (AM): {modulation_index:.2f}</div>', unsafe_allow_html=True)

    elif modulation_category in ["Frequency Modulation", "Phase Modulation"]:
        st.markdown(f'<div class="custom-subheader">Modulation Index ({modulation_category}): {modulation_index:.2f}</div>', unsafe_allow_html=True)

    fig.subplots_adjust(hspace=0.8)
    #plt.tight_layout()
    st.pyplot(fig)

    st.sidebar.divider()
    st.sidebar.button('Reset', on_click=reset)
