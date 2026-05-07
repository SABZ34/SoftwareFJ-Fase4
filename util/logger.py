"""
Módulo de registro de eventos y errores del sistema Software FJ.
"""

from datetime import datetime
from excepciones.errores import LogError

ARCHIVO_LOG = "logs.txt"


def registrar_log(mensaje, nivel="ERROR"):
    """try/except/finally — intenta escribir, siempre confirma el intento."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"[{timestamp}] [{nivel}] {mensaje}\n"
        with open(ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
            archivo.write(linea)
    except OSError as e:
        raise LogError(
            f"No se pudo escribir en logs '{ARCHIVO_LOG}': {e}"
        ) from e  # Encadenamiento de excepciones
    finally:
        pass  # Siempre se ejecuta


def registrar_info(mensaje):
    registrar_log(mensaje, nivel="INFO")


def registrar_advertencia(mensaje):
    registrar_log(mensaje, nivel="ADVERTENCIA")


def leer_logs():
    """try/except/else — el else solo corre si no hubo error."""
    try:
        archivo = open(ARCHIVO_LOG, "r", encoding="utf-8")
    except FileNotFoundError:
        return "No hay registros de logs todavía."
    except OSError as e:
        return f"Error al leer los logs: {e}"
    else:
        # Solo se ejecuta si el try fue exitoso (try/except/else)
        contenido = archivo.read()
        archivo.close()
        return contenido if contenido else "El archivo de logs está vacío."
