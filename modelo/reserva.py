"""
Clase Reserva que gestiona el proceso completo de una reserva en Software FJ.
Integra cliente, servicio, duración y estado.
Implementa confirmación, cancelación y procesamiento con manejo completo de excepciones.
"""

from excepciones.errores import ReservaError, ParametroInvalidoError
from util.logger import registrar_log, registrar_info, registrar_advertencia


class Reserva:
    ESTADOS = ["Pendiente", "Confirmada", "Cancelada"]

    def __init__(self, cliente, servicio):
        if cliente is None:
            raise ReservaError("No se puede crear una reserva sin un cliente.")
        if servicio is None:
            raise ReservaError("No se puede crear una reserva sin un servicio.")
        self.cliente  = cliente
        self.servicio = servicio
        self.estado   = "Pendiente"
        self.costo    = 0

    def confirmar(self, impuesto=None, descuento=0):
        """
        try/except/else/finally + encadenamiento de excepciones.
        """
        try:
            if self.estado != "Pendiente":
                raise ReservaError(
                    f"La reserva ya fue procesada con estado: '{self.estado}'."
                )
            if impuesto is not None:
                self.costo = self.servicio.calcular_costo(impuesto=impuesto, descuento=descuento)
            elif descuento > 0:
                self.costo = self.servicio.calcular_costo(descuento=descuento)
            else:
                self.costo = self.servicio.calcular_costo()
            self.estado = "Confirmada"

        except ReservaError:
            registrar_advertencia(
                f"Reserva rechazada para '{self.cliente.get_nombre()}'"
            )
            raise

        except Exception as e:
            registrar_log(
                f"Error inesperado al confirmar reserva de '{self.cliente.get_nombre()}': {e}"
            )
            raise ReservaError(
                f"Error al procesar la reserva: {e}"
            ) from e  # Encadenamiento de excepciones

        else:
            # Solo se ejecuta si NO hubo excepción (try/except/else)
            registrar_info(
                f"Reserva CONFIRMADA | Cliente: {self.cliente.get_nombre()} | "
                f"Servicio: {self.servicio.nombre} | Costo: ${int(self.costo):,}"
            )

        finally:
            # Siempre se ejecuta (try/except/finally)
            registrar_log(
                f"Intento de confirmación ejecutado | "
                f"Cliente: {self.cliente.get_nombre()} | Estado final: {self.estado}",
                nivel="INFO"
            )

        return self.costo

    def cancelar(self):
        """try/except/else/finally para cancelación."""
        try:
            if self.estado == "Cancelada":
                raise ReservaError(
                    f"La reserva del cliente '{self.cliente.get_nombre()}' ya estaba cancelada."
                )
            estado_anterior = self.estado
            self.estado = "Cancelada"

        except ReservaError:
            registrar_advertencia(
                f"Intento de cancelar reserva ya cancelada: {self.cliente.get_nombre()}"
            )
            raise

        else:
            registrar_info(
                f"Reserva CANCELADA | Cliente: {self.cliente.get_nombre()} | "
                f"Estado anterior: {estado_anterior}"
            )

        finally:
            registrar_log(
                f"Intento de cancelación ejecutado para: {self.cliente.get_nombre()}",
                nivel="INFO"
            )

    def describir(self):
        return (
            f"Reserva | {self.cliente.describir()} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado} | "
            f"Costo: ${int(self.costo):,}"
        )
