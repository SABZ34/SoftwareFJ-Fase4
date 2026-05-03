"""
Clase abstracta base para todas las entidades.
"""

from abc import ABC


class Entidad(ABC):
    """
    Clase abstracta que contiene atributos comunes.
    """

    def __init__(self, id):
        self._id = id  # Encapsulación (protegido)