# Campos Vectoriales Vivos: Proyecto Integrador Final

**Universidad CIAF - Ingeniería en Desarrollo de Software (2026)**
**Asignatura:** Cálculo Multivariado
**Profesor:** Aimer A. Rivas Montoya
**Integrantes:** [Tu Nombre 1], [Tu Nombre 2]

## Descripción del Proyecto
Este repositorio contiene un motor de cálculo vectorial desarrollado en Python. Su objetivo es calcular, validar numéricamente y visualizar tres conceptos fundamentales del cálculo multivariado: el Teorema de Green, Campos Conservativos (Trabajo y Función Potencial) y el Teorema de Stokes en 3D. 

## Instrucciones de Instalación y Uso

1. **Clonar el repositorio y entrar en la carpeta:**
   ```bash
   git clone [URL_DE_TU_REPO]
   cd campos-vectoriales-ciaf

2. **Instalar las dependencias:**
    pip install -r requirements.txt

3. **Ejecutar el motor de cálculo matemático:**
    python src/vector_engine.py

4. **Generar las visualizaciones (se guardarán en /output):**
   python src/visualizacion.py

5.  **Correr las pruebas unitarias con pytest:**
    python -m pytest tests/test_engine.py

**Ejercicio,Analítico,Numérico,Error Relativo (%)**
1. Green,75.398224,75.398224,0.000000e+00%
2. Conservativo,3.000000,3.000000,0.000000e+00%
3. Stokes,12.566371,12.566371,0.000000e+00%

---