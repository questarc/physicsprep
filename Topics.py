import streamlit as st

st.title("📚 Physics Topics")
topic = st.selectbox("Choose a topic", ["Kinematics", "Newton's Laws", "Electricity", "Waves", "Optics"])

if topic == "Kinematics":
    st.subheader("Kinematics")
    st.latex(r"v = u + at")
    st.latex(r"s = ut + \frac{1}{2}at^2")
    st.markdown("**Real-world example**: Car acceleration on a highway.")

elif topic == "Electricity":
    st.subheader("Electricity")
    st.latex(r"V = IR")
    st.markdown("**Real-world example**: Calculating voltage across a resistor.")
