"""
Clase Cliente con validaciones y encapsulación.
"""

from modelo.entidad import Entidad
from excepciones.errores import ClienteInvalidoError


class Cliente(Entidad):
    def __init__(self, id, nombre, documento):
        super().__init__(id)

        # Validación de datos
        if not nombre or not documento:
            raise ClienteInvalidoError("Datos de cliente inválidos")

        # Atributos privados
        self.__nombre = nombre
        self.__documento = documento

    def get_nombre(self):
        """Retorna el nombre del cliente"""
        return self.__nombre