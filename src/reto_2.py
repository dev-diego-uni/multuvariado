import matplotlib.pyplot as plt
import numpy as np

print("=== RETO 2: CAMPO GRAVITACIONAL ===")

# Definimos los puntos
A = np.array([0, 0, 10])
B = np.array([5, 3, 0])

# Función potencial phi = -9.8z
def phi(z): return -9.8 * z

# Trabajo con función potencial: W = phi(B) - phi(A)
W_potencial = phi(B[2]) - phi(A[2])
print(f"Trabajo usando potencial: phi(B) - phi(A) = {W_potencial} J")

# Parámetro t de 0 a 1
t = np.linspace(0, 1, 100)

# Camino 1: Recta (r(t) = A + t(B-A))
x1 = 0 + 5*t
y1 = 0 + 3*t
z1 = 10 - 10*t

# Camino 2: Parábola 3D (inventamos una curva que pase por A y B)
# Usaremos z = 10(1-t^2) para que haga una curva parabólica cayendo
x2 = 5*t
y2 = 3*t
z2 = 10 * (1 - t**2)

# --- Gráfica 3D del Reto 2 ---
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x1, y1, z1, 'b-', linewidth=2, label='Camino 1 (Recta)')
ax.plot(x2, y2, z2, 'r--', linewidth=2, label='Camino 2 (Parábola)')
ax.scatter(*A, color='green', s=100, label='A (0,0,10)')
ax.scatter(*B, color='purple', s=100, label='B (5,3,0)')

ax.set_title("Reto 2: Caminos en Campo Gravitacional Conservativo")
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.legend()

plt.savefig('output/reto2_caminos.png', dpi=150)
print("Gráfica de los dos caminos guardada como 'output/reto2_caminos.png'")