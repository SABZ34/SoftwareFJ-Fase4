"""
Clase abstracta base para todas las entidades del sistema Software FJ.

Software FJ es una empresa que gestiona clientes, servicios y reservas.
Esta clase define la estructura mínima que deben tener TODOS los objetos
del sistema, aplicando el principio de ABSTRACCIÓN del enunciado.

Archivo  : modelo/entidad.py


# Importamos ABC para crear clases abstractas (ABSTRACCIÓN)
# Importamos abstractmethod para obligar a las subclases a implementar métodos
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa cualquier entidad general del sistema
    Software FJ, tal como lo exige el enunciado del ejercicio.

    De esta clase heredan:
        - Cliente   : representa a los clientes de Software FJ
        - Servicio  : representa los servicios que ofrece Software FJ
                      (ReservaSala, AlquilerEquipo, Asesoria)

    Principios de POO que aplica esta clase:
        - ABSTRACCIÓN    : Es una clase abstracta, no se puede instanciar sola
        - ENCAPSULACIÓN  : El atributo _id es protegido (solo accesible por hijos)
        - POLIMORFISMO   : El método describir() se comporta diferente en cada hijo
        - HERENCIA       : Cliente y Servicio heredan de esta clase
    """

    def __init__(self, id):
        """
        Constructor de la entidad base.

        Parámetro:
            id (int): Identificador único de la entidad en el sistema.

        El guion bajo en _id indica que es un atributo PROTEGIDO:
        - Los hijos (Cliente, Servicio) sí pueden usarlo con self._id
        - Desde afuera del objeto NO se debe acceder directamente
        - Esto aplica ENCAPSULACIÓN según el enunciado
        """
        # Atributo protegido - ENCAPSULACIÓN
        self._id = id

    def get_id(self):
        """
        Método público para obtener el ID de cualquier entidad.

        Retorna:
            int: El identificador único de la entidad.

        Ejemplo de uso:
            cliente = Cliente(1, "Juan", "123456")
            print(cliente.get_id())  # imprime: 1
        """
        return self._id

    @abstractmethod
    def describir(self):
        """
        Método abstracto obligatorio para todas las entidades del sistema.

        Al marcarlo con @abstractmethod, Python OBLIGA a que cada clase
        hija implemente su propia versión de describir().
        Esto es POLIMORFISMO: mismo método, comportamiento diferente.

        En el sistema Software FJ:
            - Cliente.describir()      → muestra nombre y documento
            - ReservaSala.describir()  → muestra horas y precio de sala
            - AlquilerEquipo.describir()→ muestra equipos y precio
            - Asesoria.describir()     → muestra horas y precio de asesoría

        Si una clase hija NO implementa describir(), Python lanzará
        un TypeError al intentar crear un objeto de esa clase.

        Retorna:
            str: Descripción textual de la entidad.
        """
        pass  # Las clases hijas implementan este método

    def __str__(self):
        """
        Método especial de Python que se llama automáticamente
        cuando se usa print() sobre un objeto.

        Llama a describir() internamente, lo que significa que
        print(cliente) mostrará la descripción completa del cliente.

        Ejemplo:
            cliente = Cliente(1, "Juan", "123456")
            print(cliente)
            # Salida: Cliente #1 | Nombre: Juan | Doc: 123456

        Retorna:
            str: Llama a describir() para obtener la representación.
        """
        return self.describir()
