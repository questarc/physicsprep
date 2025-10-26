import streamlit as st
import random

st.title("🧠 Quiz Generator")

questions = {
    "Kinematics": [
        {"q": "What is the formula for final velocity?", "a": "v = u + at"},
        {"q": "What does 's' represent in kinematics?", "a": "Displacement"},
    ],
    "Electricity": [
        {"q": "What is Ohm's Law?", "a": "V = IR"},
        {"q": "Unit of resistance?", "a": "Ohm"},
    ]
}

topic = st.selectbox("Choose a topic", list(questions.keys()))
if st.button("Generate Quiz"):
    q = random.choice(questions[topic])
    st.write(f"**Question:** {q['q']}")
    st.write(f"**Answer:** ||{q['a']}||")  # Use markdown tricks or expand with input validation later
