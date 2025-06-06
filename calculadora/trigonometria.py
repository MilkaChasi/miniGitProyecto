"""Módulo trigonometría: contiene funciones para seno y coseno usando el módulo math."""

import math


def seno(grados):
    """Devuelve el seno de un ángulo en grados."""
    radianes = math.radians(grados)
    return math.sin(radianes)


def coseno(grados):
    """Devuelve el coseno de un ángulo en grados."""
    radianes = math.radians(grados)
    return math.cos(radianes)
