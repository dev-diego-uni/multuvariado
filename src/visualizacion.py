import numpy as np
import matplotlib.pyplot as plt

# Configuración general para gráficos limpios
plt.rcParams['figure.dpi'] = 150

# =====================================================================
# FIGURA 1: Campo Vectorial + Curva (Teorema de Green - Ejercicio 1)
# =====================================================================
def generar_figura_green():
    print("[VISUALIZACION] Generando Figura 1: Teorema de Green...")
    
    # 1. Definir la rejilla para el campo vectorial
    x = np.linspace(-2.5, 2.5, 20)
    y = np.linspace(-2.5, 2.5, 20)
    X, Y = np.meshgrid(x, y)
    
    # Componentes del campo F = (x^2 - y^3, x^3 + y^2)
    U = X**2 - Y**3
    V = X**3 + Y**2
    
    # Calcular la magnitud para colorear los vectores
    Magnitud = np.sqrt(U**2 + V**2)
    
    plt.figure(figsize=(7, 6))
    
    # 2. Graficar el campo vectorial con plt.quiver coloreado por magnitud
    rango_vectores = plt.quiver(X, Y, U, V, Magnitud, cmap='viridis', alpha=0.9)
    plt.colorbar(rango_vectores, label='Magnitud del Campo $|F|$')
    
    # 3. Superponer el círculo x^2 + y^2 = 4 en rojo (Radio = 2)
    t = np.linspace(0, 2 * np.pi, 200)
    plt.plot(2 * np.cos(t), 2 * np.sin(t), 'r-', linewidth=2.5, label='Círculo $C$ ($x^2+y^2=4$)')
    
    # 4. Añadir flecha indicando la dirección antihoraria en el tope del círculo
    plt.annotate('', xy=(-0.2, 2.0), xytext=(0.2, 2.0),
                 arrowprops=dict(arrowstyle="->", color="red", lw=3, mutation_scale=20))
    
    # Configuración de ejes y textos
    plt.title('Figura 1: Campo Vectorial y Teorema de Green', fontsize=12, fontweight='bold')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.xlim(-2.8, 2.8)
    plt.ylim(-2.8, 2.8)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(loc='upper right')
    plt.gca().set_aspect('equal')
    
    # Guardar imagen con las especificaciones del parcial
    plt.savefig('output/fig_green.png', dpi=150, bbox_inches='tight')
    plt.close()


# =====================================================================
# FIGURA 2: Curvas de Nivel y Gradiente (Campo Conservativo - Ejercicio 2)
# =====================================================================
def generar_figura_potencial():
    print("[VISUALIZACION] Generando Figura 2: Función Potencial...")
    
    # 1. Rejilla densa para las curvas de nivel de phi(x,y) = x^2 * y
    x = np.linspace(-0.5, 1.5, 100)
    y = np.linspace(-0.5, 2.5, 100)
    X, Y = np.meshgrid(x, y)
    Z = (X**2) * Y
    
    plt.figure(figsize=(7, 6))
    
    # 2. Graficar curvas de nivel rellenas y líneas de contorno
    mapa_contorno = plt.contourf(X, Y, Z, levels=25, cmap='coolwarm', alpha=0.85)
    plt.colorbar(mapa_contorno, label='Potencial $\\varphi(x, y) = x^2y$')
    
    lineas_contorno = plt.contour(X, Y, Z, levels=15, colors='black', linewidths=0.5)
    plt.clabel(lineas_contorno, inline=True, fontsize=8, fmt='%.1f')
    
    # 3. Rejilla más espaciada para el campo gradiente con plt.quiver
    x_g = np.linspace(-0.5, 1.5, 12)
    y_g = np.linspace(-0.5, 2.5, 15)
    X_G, Y_G = np.meshgrid(x_g, y_g)
    U_G = 2 * X_G * Y_G  # d_phi/dx
    V_G = X_G**2         # d_phi/dy
    
    plt.quiver(X_G, Y_G, U_G, V_G, color='white', edgecolors='black', 
               linewidth=0.3, alpha=0.9, label='Gradiente $\\nabla\\varphi$')
    
    # 4. Marcar los puntos A=(0,0) y B=(1,2) con estrellas grandes
    plt.plot(0, 0, marker='*', color='gold', markersize=14, markeredgecolor='black', label='Origen A (0,0)')
    plt.plot(1, 2, marker='*', color='magenta', markersize=14, markeredgecolor='black', label='Destino B (1,2)')
    
    # Configuración de ejes y textos
    plt.title('Figura 2: Curvas de Nivel y Campo Gradiente', fontsize=12, fontweight='bold')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.xlim(-0.5, 1.5)
    plt.ylim(-0.5, 2.5)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend(loc='lower right')
    
    # Guardar imagen
    plt.savefig('output/fig_potencial.png', dpi=150, bbox_inches='tight')
    plt.close()


# =====================================================================
# FIGURA 3: Superficie 3D + Borde (Teorema de Stokes - Ejercicio 3)
# =====================================================================
def generar_figura_stokes():
    print("[VISUALIZACION] Generando Figura 3: Teorema de Stokes 3D...")
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # 1. Definir el disco z = 0, x^2 + y^2 <= 4 usando coordenadas polares
    r = np.linspace(0, 2, 40)
    theta = np.linspace(0, 2 * np.pi, 40)
    R_mesh, Theta_mesh = np.meshgrid(r, theta)
    
    X_surf = R_mesh * np.cos(Theta_mesh)
    Y_surf = R_mesh * np.sin(Theta_mesh)
    Z_surf = np.zeros_like(X_surf)  # Plano z = 0
    
    # Graficar superficie semitransparente (alpha=0.4)
    ax.plot_surface(X_surf, Y_surf, Z_surf, alpha=0.4, color='cyan', edgecolor='none')
    
    # Fake plot para que la superficie aparezca de forma correcta en la leyenda
    ax.plot_background = plt.Rectangle((0, 0), 1, 1, fc="cyan", alpha=0.4)
    
    # 2. Graficar el borde C como un círculo rojo en z = 0
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(2 * np.cos(t), 2 * np.sin(t), 0, 'r-', linewidth=3, label='Borde $C$ ($x^2+y^2=4, z=0$)')
    
    # 3. Vector normal n = k = (0, 0, 1) saliendo desde el centro (0, 0, 0)
    ax.quiver(0, 0, 0, 0, 0, 1.5, color='blue', linewidth=3, arrow_length_ratio=0.15, label='Normal $\\mathbf{n} = \\mathbf{k}$')
    
    # Configuración de perspectiva y límites en 3D
    ax.set_title('Figura 3: Superficie y Borde (Teorema de Stokes 3D)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_zlim(-0.2, 1.8)
    
    # Forzar vista isométrica y ajustar ángulo inicial para apreciarlo mejor
    ax.view_init(elev=25, azim=45)
    
    # Manejo manual de leyenda para incluir la superficie semitransparente
    handles, labels = ax.get_legend_handles_labels()
    handles.append(ax.plot_background)
    labels.append('Disco Plano $S$ ($z=0$)')
    ax.legend(handles=handles, labels=labels, loc='upper left')
    
    # Guardar imagen
    plt.savefig('output/fig_stokes.png', dpi=150, bbox_inches='tight')
    plt.close()


# =====================================================================
# EJECUCIÓN PRINCIPAL
# =====================================================================
if __name__ == "__main__":
    print("Iniciando motor de visualización matemática...")
    generar_figura_green()
    generar_figura_potencial()
    generar_figura_stokes()
    print("¡Proceso completado con éxito! Las 3 imágenes PNG se han guardado.")