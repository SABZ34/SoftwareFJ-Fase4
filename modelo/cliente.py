"""
Clase Cliente con encapsulación y validación.
"""

from excepciones.errores import ClienteInvalidoError
from modelo.entidad import Entidad


class Cliente(Entidad):
    def __init__(self, id, nombre, documento):
        super().__init__(id)

        if not nombre or not documento:
            raise ClienteInvalidoError("Datos inválidos del cliente")

        self.__nombre = nombre
        self.__documento = documento

    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento