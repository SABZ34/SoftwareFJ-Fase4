"""
Clase Reserva con manejo completo de errores.
"""

from excepciones.errores import ReservaError, ServicioNoDisponibleError
from util.logger import registrar_log


class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            if not self.servicio:
                raise ServicioNoDisponibleError("Servicio no disponible")

            costo = self.servicio.calcular_costo(0.19, 0.05)  # con impuesto y descuento
            self.estado = "Confirmada"

        except Exception as e:
            registrar_log(f"Error en confirmación: {e}")
            raise ReservaError("Fallo en reserva") from e

        else:
            return costo

        finally:
            registrar_log("Intento de confirmación ejecutado")

    def cancelar(self):
        try:
            if self.estado != "Confirmada":
                raise ReservaError("No se puede cancelar")

            self.estado = "Cancelada"

        except Exception as e:
            registrar_log(f"Error al cancelar: {e}")
            raise