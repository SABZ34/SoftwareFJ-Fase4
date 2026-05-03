"""
Archivo principal del sistema.
Aquí se inicia la aplicación gráfica.
"""

import tkinter as tk
from interfaz.app import App  # Importa la interfaz principal

# Crear ventana principal
root = tk.Tk()

# Inicializar aplicación
app = App(root)

# Ejecutar programa
root.mainloop()