import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🧲 Interactive Simulations")
st.subheader("Spring Oscillation")

k = st.slider("Spring constant (k)", 1, 100, 20)
m = st.slider("Mass (m)", 1, 10, 5)
t = np.linspace(0, 10, 500)
omega = np.sqrt(k / m)
x = np.cos(omega * t)

fig, ax = plt.subplots()
ax.plot(t, x)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Displacement (m)")
ax.set_title("Simple Harmonic Motion")
st.pyplot(fig)
