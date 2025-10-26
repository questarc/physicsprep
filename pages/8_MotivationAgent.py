import streamlit as st
import random

st.title("💬 Motivation Agent")

messages = [
    "You're doing amazing! Keep pushing forward 💪",
    "Physics is tough, but so are you!",
    "Every formula you learn is a superpower 🔬",
    "Mistakes mean you're learning. Keep going!",
    "You're one step closer to mastering physics 🚀"
]

if st.button("Get Motivation"):
    st.success(random.choice(messages))
