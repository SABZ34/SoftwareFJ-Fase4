"""
Clase abstracta base del sistema.
Representa cualquier entidad con ID.
"""

from abc import ABC

class Entidad(ABC):
    def __init__(self, id):
        self.id = id