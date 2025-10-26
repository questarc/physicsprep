import streamlit as st

st.title("🎯 Progress Tracker")

topics = ["Kinematics", "Newton's Laws", "Electricity", "Waves", "Optics"]
completed = st.multiselect("Mark topics you've completed:", topics)

progress = len(completed) / len(topics) * 100
st.progress(progress / 100)
st.success(f"You've completed {len(completed)} of {len(topics)} topics ({progress:.0f}%)")
