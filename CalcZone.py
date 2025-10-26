import streamlit as st

st.title("🧮 Physics Calculator")
calc_type = st.selectbox("Choose calculator", ["Ohm's Law", "Kinematics Solver"])

if calc_type == "Ohm's Law":
    st.subheader("Ohm's Law Calculator")
    current = st.number_input("Current (I) in Amps", value=1.0)
    resistance = st.number_input("Resistance (R) in Ohms", value=1.0)
    voltage = current * resistance
    st.success(f"Voltage (V) = {voltage:.2f} Volts")

elif calc_type == "Kinematics Solver":
    st.subheader("Final Velocity Calculator")
    u = st.number_input("Initial Velocity (u)", value=0.0)
    a = st.number_input("Acceleration (a)", value=9.8)
    t = st.number_input("Time (t)", value=1.0)
    v = u + a * t
    st.success(f"Final Velocity (v) = {v:.2f} m/s")
