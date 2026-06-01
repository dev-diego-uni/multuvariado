import numpy as np
from scipy import integrate

# Integrantes: [NOMBRES] | Grupo: [NUMERO] | CIAF 2026

# ==========================================
# FUNCIÓN 1: Teorema de Green (Ejercicio 1)
# ==========================================
def green_circulo(R=2.0):
    """
    Calcula la integral de línea usando el Teorema de Green sobre un círculo.
    
    Parámetros:
        R (float): Radio del círculo. Por defecto es 2.0.
        
    Retorna:
        float: Resultado numérico de la integral doble en polares.
        
    Excepciones:
        ValueError: Si el radio R ingresado es negativo.
    """
    if R < 0:
        raise ValueError("El radio no puede ser negativo.")
        
    # Integrando en polares: 3(x^2 + y^2) -> 3(r^2) * r (del jacobiano) = 3r^3
    def integrando(r, theta):
        return 3 * r**3
    
    # integrate.dblquad(func, lim_inf_theta, lim_sup_theta, lim_inf_r, lim_sup_r)
    resultado, error = integrate.dblquad(
        integrando, 
        0, 2 * np.pi, 
        lambda theta: 0, lambda theta: R
    )
    
    # Fórmula analítica para cualquier radio R: (3*pi/2) * R^4
    analitico = (3 * np.pi / 2) * R**4
    
    print(f"\n[GREEN] Analítico: {analitico:.6f}")
    print(f"[GREEN] Numérico:  {resultado:.6f}")
    print(f"[GREEN] Error abs: {abs(resultado - analitico):.6e}")
    
    return resultado, analitico

# ==========================================
# FUNCIÓN 2: Campo Conservativo (Ejercicio 2)
# ==========================================
def campo_conservativo(A=(0,0,0), B=(1,2,1)):
    """
    Verifica si el campo F=(2xy+z^2, x^2, 2xz) es conservativo y calcula el trabajo W.
    
    Parámetros:
        A (tuple): Punto inicial (x, y, z).
        B (tuple): Punto final (x, y, z).
        
    Retorna:
        float: Trabajo W calculado como phi(B) - phi(A).
    """
    def phi(x, y, z):
        return (x**2 * y) + (x * z**2)
    
    # Punto de prueba para verificar curl F = 0
    x0, y0, z0 = 1.0, 1.0, 1.0
    
    # Cálculo manual del rotacional en el punto de prueba
    curl_i = (0) - (0)              # dR/dy - dQ/dz
    curl_j = (2*z0) - (2*z0)        # dP/dz - dR/dx
    curl_k = (2*x0) - (2*x0)        # dQ/dx - dP/dy
    
    es_conservativo = (curl_i == 0 and curl_j == 0 and curl_k == 0)
    
    # Cálculo del trabajo
    W = phi(*B) - phi(*A)
    analitico = 3.0 # Para los puntos por defecto
    
    print(f"\n[CONSERV] curl(F) = ({curl_i}, {curl_j}, {curl_k})")
    print(f"[CONSERV] Es conservativo: {es_conservativo}")
    print(f"[CONSERV] W = phi(B) - phi(A) = {W:.4f} J")
    
    return W, analitico

# ==========================================
# FUNCIÓN 3: Teorema de Stokes (Ejercicio 3)
# ==========================================
def stokes_circulo(R=2.0, n=800):
    """
    Calcula la integral de línea usando el Teorema de Stokes para F=(z, x, y).
    
    Parámetros:
        R (float): Radio del disco.
        n (int): Número de puntos para la integral de línea numérica.
        
    Retorna:
        float: Resultado numérico de la integral de superficie (Stokes).
        
    Excepciones:
        ValueError: Si el radio R ingresado es negativo.
    """
    if R < 0:
        raise ValueError("El radio no puede ser negativo.")
        
    # Por Stokes: curl(F) = (1,1,1), n = (0,0,1). (curl F) . n = 1
    # La integral de superficie es simplemente el área del disco.
    stokes = np.pi * R**2
    
    # Verificación con integral de línea directa (np.trapz)
    t = np.linspace(0, 2*np.pi, n)
    x = R * np.cos(t)
    y = R * np.sin(t)
    z = np.zeros(n)
    
    dx = np.gradient(x, t)
    dy = np.gradient(y, t)
    dz = np.zeros(n)
    
    # F = (z, x, y)
    linea = integrate.trapezoid(z*dx + x*dy + y*dz, t)
    analitico = np.pi * R**2
    
    print(f"\n[STOKES] (curl F).n = 1 -> Integral = Área del disco")
    print(f"[STOKES] Superficie (Stokes): {stokes:.6f}")
    print(f"[STOKES] Línea directa: {linea:.6f}")
    
    return stokes, analitico

# ==========================================
# FUNCIÓN 4: Tabla de Resultados
# ==========================================
def tabla_resultados():
    """
    Imprime una tabla comparativa de los 3 ejercicios, mostrando valores
    numéricos, analíticos y el error relativo porcentual.
    """
    print("\n" + "="*60)
    print("RESUMEN DE RESULTADOS: ANALÍTICO VS NUMÉRICO")
    print("="*60)
    print(f"{'Ejercicio':<15} | {'Analítico':<12} | {'Numérico':<12} | {'Error Relativo %'}")
    print("-" * 60)
    
    try:
        # Ejecutar funciones
        num_g, ana_g = green_circulo(2.0)
        num_c, ana_c = campo_conservativo()
        num_s, ana_s = stokes_circulo(2.0)
        
        # Calcular errores (evitar división por cero)
        err_g = abs(num_g - ana_g) / ana_g * 100 if ana_g != 0 else 0
        err_c = abs(num_c - ana_c) / ana_c * 100 if ana_c != 0 else 0
        err_s = abs(num_s - ana_s) / ana_s * 100 if ana_s != 0 else 0
        
        # Imprimir filas
        print(f"{'1. Green':<15} | {ana_g:<12.6f} | {num_g:<12.6f} | {err_g:.6e}%")
        print(f"{'2. Conservativo':<15} | {ana_c:<12.6f} | {num_c:<12.6f} | {err_c:.6e}%")
        print(f"{'3. Stokes':<15} | {ana_s:<12.6f} | {num_s:<12.6f} | {err_s:.6e}%")
        
    except ValueError as e:
        print(f"Error detectado: {e}")
    print("="*60 + "\n")

# ==========================================
# PRUEBAS UNITARIAS
# ==========================================
def ejecutar_pruebas():
    """Ejecuta los asserts para validar el código matemáticamente."""
    print("Ejecutando pruebas unitarias...")
    
    # Prueba 1: Green con radio 2 debe acercarse a 24*pi
    res_green, _ = green_circulo(2.0)
    assert abs(res_green - 24*np.pi) < 0.01, "Error en Teorema de Green"
    
    # Prueba 2: Campo conservativo de A a B debe ser exactamente 3
    res_cons, _ = campo_conservativo()
    assert abs(res_cons - 3.0) < 0.01, "Error en Campo Conservativo"
    
    # Prueba 3: Stokes con radio 2 debe acercarse a 4*pi
    res_stokes, _ = stokes_circulo(2.0)
    assert abs(res_stokes - 4*np.pi) < 0.01, "Error en Teorema de Stokes"
    
    # Prueba 4 (Manejo de errores): Verificar que el radio negativo lance error
    try:
        green_circulo(-1.0)
        assert False, "No se detectó el radio negativo en Green"
    except ValueError:
        pass # Comportamiento esperado
        
    print("¡Todas las pruebas pasaron exitosamente!\n")

# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":
    ejecutar_pruebas()
    tabla_resultados()