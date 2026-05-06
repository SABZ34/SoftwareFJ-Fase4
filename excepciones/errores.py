"""
Excepciones personalizadas del sistema Software FJ.
Cada excepción representa un tipo específico de error
que puede ocurrir durante la operación del sistema.

Archivo  : excepciones/errores.py
Curso    : Programación 213023 - UNAD
"""


# ─────────────────────────────────────────────────────────
# CLASE BASE — todas las excepciones del sistema heredan de esta
# ─────────────────────────────────────────────────────────

class SoftwareFJError(Exception):
    """
    Excepción base del sistema Software FJ.
    Al heredar de Exception, permite capturar cualquier
    error del sistema con un solo 'except SoftwareFJError'.
    Aplica HERENCIA de excepciones.
    """
    pass


# ─────────────────────────────────────────────────────────
# EXCEPCIONES DE CLIENTE
# ─────────────────────────────────────────────────────────

class ClienteInvalidoError(SoftwareFJError):
    """
    Se lanza cuando los datos de un cliente no son válidos.
    Ejemplos:
        - Nombre vacío o solo espacios
        - Documento con letras en vez de números
        - Nombre que contiene números
        - Campos faltantes o nulos
    """
    pass


class ClienteDuplicadoError(SoftwareFJError):
    """
    Se lanza cuando se intenta registrar un cliente
    con un documento que ya existe en el sistema.
    Ejemplo: registrar dos veces la misma cédula.
    """
    pass


# ─────────────────────────────────────────────────────────
# EXCEPCIONES DE SERVICIO
# ─────────────────────────────────────────────────────────

class ServicioNoDisponibleError(SoftwareFJError):
    """
    Se lanza cuando un servicio no puede crearse o procesarse.
    Ejemplos:
        - Cantidad negativa o cero
        - Cantidad superior al máximo permitido
        - Servicio fuera de horario de atención
    """
    pass


class ParametroInvalidoError(SoftwareFJError):
    """
    Se lanza cuando un parámetro tiene tipo o valor incorrecto.
    Ejemplos:
        - Texto donde se espera un número entero
        - Impuesto fuera del rango 0 a 1
        - Descuento negativo
        - Cantidad no entera
    """
    pass


class CostoInvalidoError(SoftwareFJError):
    """
    Se lanza cuando el cálculo de costo produce un resultado inválido.
    Ejemplos:
        - El descuento supera el costo total
        - El costo calculado es negativo
        - Parámetros de cálculo inconsistentes
    """
    pass


# ─────────────────────────────────────────────────────────
# EXCEPCIONES DE RESERVA
# ─────────────────────────────────────────────────────────

class ReservaError(SoftwareFJError):
    """
    Se lanza cuando hay un problema al crear o procesar una reserva.
    Ejemplos:
        - Cliente nulo al crear la reserva
        - Servicio nulo al crear la reserva
        - Estado de reserva inválido
    """
    pass


class ReservaYaConfirmadaError(SoftwareFJError):
    """
    Se lanza cuando se intenta confirmar una reserva
    que ya fue previamente confirmada o cancelada.
    Ejemplo: llamar a confirmar() dos veces sobre la misma reserva.
    """
    pass


class ReservaYaCanceladaError(SoftwareFJError):
    """
    Se lanza cuando se intenta cancelar una reserva
    que ya estaba cancelada anteriormente.
    Ejemplo: llamar a cancelar() dos veces sobre la misma reserva.
    """
    pass


# ─────────────────────────────────────────────────────────
# EXCEPCIONES DEL SISTEMA
# ─────────────────────────────────────────────────────────

class LogError(SoftwareFJError):
    """
    Se lanza cuando el sistema no puede escribir en el archivo de logs.
    Ejemplo: sin permisos de escritura en el sistema de archivos.
    """
    pass
