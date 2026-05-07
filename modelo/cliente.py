"""
Clase Cliente con validaciones robustas y encapsulación de datos personales.
Hereda de Entidad e implementa el método abstracto describir().
"""

from modelo.entidad import Entidad
from excepciones.errores import ClienteInvalidoError


class Cliente(Entidad):
    """
    Representa un cliente registrado en el sistema Software FJ.
    Aplica encapsulación: los atributos son privados y solo
    accesibles mediante métodos get.
    """

    def __init__(self, id, nombre, documento):
        super().__init__(id)

        if not nombre or not nombre.strip():
            raise ClienteInvalidoError(
                f"El nombre del cliente no puede estar vacío. (ID intentado: {id})"
            )

        if not documento or not documento.strip():
            raise ClienteInvalidoError(
                f"El documento del cliente no puede estar vacío. (Nombre: {nombre})"
            )

        if not documento.strip().isdigit():
            raise ClienteInvalidoError(
                f"El documento debe contener solo números. Se recibió: '{documento}'"
            )

        if any(c.isdigit() for c in nombre):
            raise ClienteInvalidoError(
                f"El nombre no puede contener números. Se recibió: '{nombre}'"
            )

        self.__nombre = nombre.strip()
        self.__documento = documento.strip()

    def get_nombre(self):
        """Retorna el nombre completo del cliente."""
        return self.__nombre

    def get_documento(self):
        """Retorna el número de documento del cliente."""
        return self.__documento

    def describir(self):
        """
        Implementación del método abstracto de Entidad.
        Devuelve una descripción textual del cliente.
        """
        return f"Cliente #{self._id} | Nombre: {self.__nombre} | Doc: {self.__documento}"
