# Campos Vectoriales Proyecto Final

**Universidad CIAF - Ingeniería en Desarrollo de Software (2026)**

**Asignatura:** Cálculo Multivariado

**Profesor:** Aimer A. Rivas Montoya

**Integrante:** Diego Alejandro Monrroy García

## Descripción del Proyecto
Este repositorio contiene un motor de cálculo vectorial desarrollado en Python. Su objetivo es calcular, validar numéricamente y visualizar tres conceptos fundamentales del cálculo multivariado: el Teorema de Green, Campos Conservativos (Trabajo y Función Potencial) y el Teorema de Stokes en 3D. 

## Instrucciones de Instalación y Uso

1. **Clonar el repositorio y entrar en la carpeta:**
   ```bash
   git clone https://github.com/dev-diego-uni/multuvariado.git
   cd campos-vectoriales-ciaf

2. **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt

3. **Ejecutar el motor de cálculo matemático:**
    ```bash
    python src/vector_engine.py

4. **Generar las visualizaciones (se guardarán en /output):**
    ```bash
    python src/visualizacion.py

5.  **Correr las pruebas unitarias con pytest:**
    ```bash
    python -m pytest tests/test_engine.py

6. **Ejecutar los Retos Matemáticos Extra (Área y Gravedad):**
    ```bash
    python src/reto_1.py
    python stc/reto_2.py

7. **Desplegar la App Interactiva localmente (Streamlit):**
    ```bash
    streamlit run src/reto_3.py

**Retos Extra Implementados**

**Reto 1 (Área con Green):**

    Se implementó una función para calcular el área de curvas cerradas paramétricas,
    probada exitosamente con un círculo y una elipse con un error relativo de 0.00%.

**Reto 2 (Campo Gravitacional):**

    Se demostró que el trabajo $W$ moviendo una masa de $A=(0,0,10)$ a $B=(5,3,0)$ 
    en $G=(0,0,-9.8)$ es independiente del camino (recto vs. parabólico).

**Reto 3 (App Streamlit):** 

    Simulador web interactivo en tiempo real para el Teorema de Green. 
    Enlace: http://multivariado.streamlit.app/

## Ejercicio, Analítico, Numérico,Error Relativo (%)## 

    1. Green,75.398224,75.398224,0.000000e+00%
    2. Conservativo,3.000000,3.000000,0.000000e+00%
    3. Stokes,12.566371,12.566371,0.000000e+00%
