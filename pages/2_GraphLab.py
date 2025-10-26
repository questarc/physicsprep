import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📈 Formula Visualizer")
st.subheader("Projectile Motion: Range vs Angle")

velocity = st.slider("Initial Velocity (m/s)", 10, 100, 50)
angles = np.linspace(0, 90, 100)
g = 9.8
ranges = (velocity**2) * np.sin(np.radians(2 * angles)) / g

fig, ax = plt.subplots()
ax.plot(angles, ranges)
ax.set_xlabel("Angle (degrees)")
ax.set_ylabel("Range (meters)")
ax.set_title("Projectile Range vs Launch Angle")
st.pyplot(fig)
