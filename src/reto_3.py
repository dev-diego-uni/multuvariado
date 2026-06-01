import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Teorema de Green - CIAF", layout="centered")

st.title("Cálculo Multivariado: Teorema de Green Interactivo")
st.markdown("**Universidad CIAF 2026**")

# Slider interactivo para el radio R
R = st.slider("Selecciona el radio del círculo (R):", min_value=0.5, max_value=5.0, value=2.0, step=0.1)

# Cálculo matemático del PDF: 24*pi*(R^4)/16 simplifica a (3/2)*pi*R^4
resultado = (3/2) * np.pi * (R**4)

st.success(f"### Resultado de la integral: {resultado:.4f}")

# Generar la figura actualizada
fig, ax = plt.subplots(figsize=(6, 6))

# Rejilla del campo vectorial
x = np.linspace(-R-1, R+1, 20)
y = np.linspace(-R-1, R+1, 20)
X, Y = np.meshgrid(x, y)
U = X**2 - Y**3
V = X**3 + Y**2
Magnitud = np.sqrt(U**2 + V**2)

# Campo y círculo
ax.quiver(X, Y, U, V, Magnitud, cmap='viridis', alpha=0.8)
t = np.linspace(0, 2 * np.pi, 100)
ax.plot(R * np.cos(t), R * np.sin(t), 'r-', linewidth=3, label=f'Círculo r={R}')

ax.set_aspect('equal')
ax.set_xlim(-R-1, R+1)
ax.set_ylim(-R-1, R+1)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()
ax.set_title(f"Campo F y Círculo C (Radio = {R})")

# Mostrar gráfica en la web
st.pyplot(fig)