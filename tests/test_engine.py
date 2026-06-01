import pytest
import numpy as np
import sys
import os

# Asegurar que pytest encuentre la carpeta src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.vector_engine import green_circulo, campo_conservativo, stokes_circulo

def test_green_circulo():
    """Prueba que el Teorema de Green de como resultado aprox 24*pi para R=2"""
    resultado, _ = green_circulo(2.0)
    assert abs(resultado - 24 * np.pi) < 0.01

def test_campo_conservativo():
    """Prueba que el trabajo del campo conservativo sea exactamente 3"""
    resultado, _ = campo_conservativo()
    assert abs(resultado - 3.0) < 0.01

def test_stokes_circulo():
    """Prueba que el Teorema de Stokes de como resultado aprox 4*pi para R=2"""
    resultado, _ = stokes_circulo(2.0)
    assert abs(resultado - 4 * np.pi) < 0.01

def test_radio_negativo():
    """Prueba que el programa levante un ValueError si se pasa un radio negativo"""
    with pytest.raises(ValueError):
        green_circulo(-1.0)