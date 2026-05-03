"""
Clase Reserva que gestiona el proceso de reservas.
"""

from excepciones.errores import ReservaError
from util.logger import registrar_log


class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            if not self.servicio:
                raise ReservaError("Servicio inválido")

            costo = self.servicio.calcular_costo()
            self.estado = "Confirmada"

        except Exception as e:
            registrar_log(str(e))
            raise

        finally:
            registrar_log("Intento de reserva ejecutado")

        return costo