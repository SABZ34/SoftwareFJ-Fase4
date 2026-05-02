"""
Clases de servicios con herencia y polimorfismo.
"""

from abc import ABC, abstractmethod
from excepciones.errores import ServicioNoDisponibleError


class Servicio(ABC):
    def __init__(self, cantidad):
        # Validación
        if cantidad <= 0:
            raise ServicioNoDisponibleError("Cantidad inválida")

        self.cantidad = cantidad
        self.nombre = "Servicio"

    @abstractmethod
    def calcular_costo(self, impuesto=0, descuento=0):
        pass


class ReservaSala(Servicio):
    def __init__(self, cantidad):
        super().__init__(cantidad)
        self.nombre = "Sala"

    def calcular_costo(self, impuesto=0.19, descuento=0):
        return (self.cantidad * 50000) * (1 + impuesto) - descuento


class AlquilerEquipo(Servicio):
    def __init__(self, cantidad):
        super().__init__(cantidad)
        self.nombre = "Equipo"

    def calcular_costo(self, impuesto=0.1, descuento=0):
        return (self.cantidad * 30000) * (1 + impuesto) - descuento


class Asesoria(Servicio):
    def __init__(self, cantidad):
        super().__init__(cantidad)
        self.nombre = "Asesoria"

    def calcular_costo(self, impuesto=0.15, descuento=0):
        return (self.cantidad * 80000) * (1 + impuesto) - descuento