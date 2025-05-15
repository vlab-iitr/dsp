import streamlit as st

# Default values
default_duration = 10
default_fs = 1000
# default_signal = "Sinusoidal"
# default_phase = 0
# default_amp = 1.0

# # Initialize session state if not set
# if 'durations' not in st.session_state:
#     st.session_state.durations = default_duration
# if 'fs' not in st.session_state:
#     st.session_state.fs = default_fs
# if 'signal' not in st.session_state:
#     st.session_state.signal = default_signal
# if 'phase' not in st.session_state:
#     st.session_state.phase = default_phase
# if 'amp' not in st.session_state:
#     st.session_state.amp = default_amp

# Sidebar inputs with unique keys
st.sidebar.header("Signal Parameters")
durations = st.sidebar.number_input("Duration (s)", value=default_duration, key="durations")
fs = st.sidebar.number_input("Sampling Frequency (Hz)", value=default_fs, key="fs")
# signal = st.sidebar.selectbox("Signal Type", ["Sinusoidal", "Square", "Triangle"], index=["Sinusoidal", "Square", "Triangle"].index(st.session_state.signal), key="signal1")
# phase = st.sidebar.slider("Phase (°)", min_value=0, max_value=360, value=st.session_state.phase, key="phase1")
# amp = st.sidebar.slider("Amplitude", min_value=0.1, max_value=10.0, value=st.session_state.amp, key="amp1")

# Update session state with current values
# st.session_state.durations = durations
# st.session_state.fs = fs
# st.session_state.signal = signal
# st.session_state.phase = phase
# st.session_state.amp = amp

def reset():
    st.session_state.durations = 10
    st.session_state.fs = 1000

st.button('Reset', on_click=reset)

# Reset button
# if st.sidebar.button("Reset"):
#     print('entry1')
    # Reset session state values to defaults
    # st.session_state.durations = default_duration
    # st.session_state.fs = default_fs
    # st.session_state.signal = default_signal
    # st.session_state.phase = default_phase
    # st.session_state.amp = default_amp
    # # print(st.session_state.fs)

    # Clear widget states by deleting keys (forces a reset)
    # for key in ["durations1", "fs1", "signal1", "phase1", "amp1"]:
    #         if key in st.session_state:
    #             del st.session_state[key]

    # print('entry2')
    # # Force a rerun to apply changes
    # st.rerun()
    




# Display current values
st.write("### Current Signal Parameters:")
st.write(f"Duration: {st.session_state.durations} s")
st.write(f"Sampling Frequency: {st.session_state.fs} Hz")
# st.write(f"Signal Type: {st.session_state.signal}")
# st.write(f"Phase: {st.session_state.phase}°")
# st.write(f"Amplitude: {st.session_state.amp}")
