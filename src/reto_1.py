import numpy as np
from scipy import integrate

def area_green(x_func, y_func, t_range, n_points=1000):
    """
    Calcula el área encerrada por una curva paramétrica usando el Teorema de Green.
    """
    t = np.linspace(t_range[0], t_range[1], n_points)
    x = x_func(t)
    y = y_func(t)
    
    # Derivadas numéricas
    dx = np.gradient(x, t)
    dy = np.gradient(y, t)
    
    # Fórmula: A = 1/2 * integral(-y*dx + x*dy)
    integrando = -y * dx + x * dy
    area = 0.5 * integrate.trapezoid(integrando, t)
    return area

# --- PRUEBAS DEL RETO 1 ---
print("=== RETO 1: ÁREA CON GREEN ===")

# a) Círculo r=2: x = 2cos(t), y = 2sin(t)
area_circ_num = area_green(lambda t: 2*np.cos(t), lambda t: 2*np.sin(t), [0, 2*np.pi])
area_circ_ana = np.pi * 2**2

print(f"Círculo r=2 -> Analítico: {area_circ_ana:.4f} | Numérico: {area_circ_num:.4f}")
print(f"Error relativo: {abs(area_circ_num - area_circ_ana)/area_circ_ana * 100:.2e}%\n")

# b) Elipse x=3cos(t), y=2sin(t)
area_elip_num = area_green(lambda t: 3*np.cos(t), lambda t: 2*np.sin(t), [0, 2*np.pi])
area_elip_ana = np.pi * 3 * 2

print(f"Elipse 3x2 -> Analítico: {area_elip_ana:.4f} | Numérico: {area_elip_num:.4f}")
print(f"Error relativo: {abs(area_elip_num - area_elip_ana)/area_elip_ana * 100:.2e}%\n")