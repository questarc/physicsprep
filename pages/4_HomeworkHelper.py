import streamlit as st

st.title("🧠 Homework Helper")
problem = st.selectbox("Problem Type", ["Find Final Velocity", "Find Voltage"])

if problem == "Find Final Velocity":
    st.subheader("Step-by-Step: Final Velocity")
    u = st.number_input("Initial Velocity (u)", value=0.0, key="u_hw")
    a = st.number_input("Acceleration (a)", value=9.8, key="a_hw")
    t = st.number_input("Time (t)", value=1.0, key="t_hw")
    st.markdown("**Formula**: v = u + at")
    v = u + a * t
    st.success(f"Final Velocity (v) = {v:.2f} m/s")

elif problem == "Find Voltage":
    st.subheader("Step-by-Step: Voltage")
    i = st.number_input("Current (I)", value=1.0, key="i_hw")
    r = st.number_input("Resistance (R)", value=1.0, key="r_hw")
    st.markdown("**Formula**: V = IR")
    v = i * r
    st.success(f"Voltage (V) = {v:.2f} Volts")
