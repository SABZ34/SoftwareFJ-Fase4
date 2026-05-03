"""
Excepciones personalizadas del sistema.
"""


class ClienteInvalidoError(Exception):
    pass


class ServicioNoDisponibleError(Exception):
    pass


class ReservaError(Exception):
    pass