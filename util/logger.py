"""
Módulo para registrar logs del sistema.
"""

from datetime import datetime


def registrar_log(mensaje):
    try:
        with open("logs.txt", "a") as archivo:
            archivo.write(f"{datetime.now()} - {mensaje}\n")
    except:
        print("Error al guardar log")