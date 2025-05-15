import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy.stats import kurtosis, skew, mode


# Function to compute signal statistics
def compute_signal_statistics(signal):
    statistics = {
        'Arithmetic Mean': np.mean(signal),
        'RMS': np.sqrt(np.mean(np.square(signal))),
        'Standard Deviation': np.std(signal),
        'Variance': np.var(signal),
        'Kurtosis': kurtosis(signal),
        'Median': np.median(signal),
        'Mode': mode(signal, keepdims=True)[0][0],  # Fix: keepdims=True
        'Skewness': skew(signal),
        'Maximum': np.max(signal),
        'Minimum': np.min(signal)
    }
    
    # Convert the statistics dictionary to a DataFrame
    statistics_df = pd.DataFrame(statistics.items(), columns=['Statistic', 'Value'])
    statistics_df.index = statistics_df.index + 1
    statistics_df.index.name = "S. No."
    
    # Apply styling to the DataFrame
    styled_df = statistics_df.style.set_table_styles(
    [
     {'selector': 'th', 'props': [('background-color', '#035F8A'), ('color', 'white'),('font-weight', 'bold'),('text-align','center'),('border-color','rgb(240, 242, 246)')]},  # Header styling
     {'selector': 'td', 'props': [('background-color', 'rgb(240, 242, 246)'),('border-color','#035F8A')]}]                         # Cell styling         
)
    
    st.table(styled_df)
  
    return statistics

# Function to generate different signals
def unit_impulse(duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    impulse = np.zeros_like(t)
    impulse[len(t) // 2] = 1
    return t, impulse

def unit_step(duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    step = np.ones_like(t)
    return t, step

def ramp(duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return t, t  # Linear ramp

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


def reset():
    st.session_state.dur_1 = default_duration
    st.session_state.fs_1 = default_fs
    st.session_state.selectbox_1 = default_signal
    st.session_state.phase_1 = default_phase
    st.session_state.amp_1 = default_amp


# Main Streamlit Interface
def dsp_simulator1():
    
    st.sidebar.markdown('<p style="border-top: 2px solid  #035F8A;"></p>',unsafe_allow_html=True)
    st.markdown('<div class="my-custom-text">Generation of Standard Signals and their Statistical Analysis</div>',unsafe_allow_html=True)
    st.divider()
    st.sidebar.title("Signal Generation Options")

    
    # Signal type selection
    signal_type= st.sidebar.selectbox("Select Signal Type", 
        ["Unit Impulse", "Unit Step", "Ramp", "Sinusoidal", "Square Wave", "Triangular Wave"],
         key="selectbox_1")

    # Input parameters
    duration = st.sidebar.number_input("Duration (seconds)", min_value=0.1, value=default_duration,key="dur_1")
    fs = st.sidebar.number_input("Sampling Rate (Hz)", min_value=100, value=default_fs,key="fs_1")
    phase_deg = st.sidebar.number_input("Phase (degrees)", min_value=-180.0, max_value=180.0, value=default_phase,key="phase_1")
    phase = np.radians(phase_deg)  # Convert degrees to radians for computation
    amplitude = st.sidebar.number_input("Amplitude", min_value=0.1, value=default_amp, key="amp_1")  
    

    frequency = None  
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

    # Plot the signal
    st.markdown(f'<div class="custom-subheader">Generated {signal_type} Signal</div>', unsafe_allow_html=True)

    if undersampled:
        st.write("⚠️ This signal is **under-sampled**! Nyquist criterion is not satisfied.")

        # Original Signal (Nyquist Rate)
        st.write("📈 Original Signal (Nyquist Rate):")
        fig_original = go.Figure()
        fig_original.add_trace(go.Scatter(x=t, y=signal, mode="lines", name="Original Signal"))
        fig_original.update_layout(
            title=f"Original {signal_type} Signal",
            title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ),
        title_x=0.5,
            xaxis_title="Time [s]",
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
        st.plotly_chart(fig_original)

        # Under-Sampled Signal
        st.write("📉 Under-Sampled Signal:")
        fig_under = go.Figure()
        fig_under.add_trace(go.Scatter(x=t_to_plot, y=signal_to_plot, mode="lines", 
                                       name="Under-Sampled Signal", line=dict(dash="dash")))
        fig_under.update_layout(
            title=f"Under-Sampled {signal_type} Signal",
            title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4'
        ),
            title_x=0.5,
            xaxis_title="Time [s]",
            yaxis_title="Amplitude",
             xaxis=dict(showgrid=True),
            xaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia;",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),  
            yaxis=dict(showgrid=True),
            yaxis_title_font=dict(  # Set font properties for y-axis title
                family="Georgia",  # Set the font family for y-axis title
                size=16,  # Set font size for y-axis title
                color='#1f77b4'  # Set the color for y-axis title
            ), 
        )
        st.plotly_chart(fig_under)

    else:
        fig_signal = go.Figure()
        fig_signal.add_trace(go.Scatter(x=t_to_plot, y=signal_to_plot, mode="lines", name="Signal"))
        fig_signal.update_layout(
            title=f"{signal_type} Signal",
            title_font=dict(
            family="Georgia",  # Set your desired font family
            size=18, 
            color='#1f77b4' 
        ),
            title_x=0.5,
            xaxis_title="Time [μs]",  # Changed label to microseconds
            yaxis_title="Amplitude",
            xaxis=dict(showgrid=True),
            xaxis_title_font=dict(  # Set font properties for x-axis title
                family="Georgia",  # Set the font family for x-axis title
                size=16,  # Set font size for x-axis title
                color='#1f77b4'  # Set the color for x-axis title
            ),  
            yaxis=dict(showgrid=True),
            yaxis_title_font=dict(  # Set font properties for y-axis title
                family="Georgia",  # Set the font family for y-axis title
                size=16,  # Set font size for y-axis title
                color='#1f77b4'  # Set the color for y-axis title
            ), 
        )
        st.plotly_chart(fig_signal)

    # Compute and display signal statistics
    compute_signal_statistics(signal)

    st.sidebar.divider()
    st.sidebar.button('Reset', on_click=reset)
         

    # if st.button("Refresh Page"):
    #     pyautogui.hotkey("ctrl","F5")

    
