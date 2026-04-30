"""
Módulo de registro de logs del sistema
"""

from datetime import datetime


def registrar_log(mensaje):
    """
    Guarda mensajes de error o eventos en logs.txt
    """
    try:
        with open("logs.txt", "a") as archivo:
            archivo.write(f"{datetime.now()} - {mensaje}\n")
    except Exception as e:
        print("Error al escribir log:", e)