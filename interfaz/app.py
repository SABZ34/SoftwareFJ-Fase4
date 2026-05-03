"""
Interfaz gráfica del sistema.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from modelo.cliente import Cliente
from modelo.servicio import ReservaSala, AlquilerEquipo, Asesoria
from modelo.reserva import Reserva
from excepciones.errores import *
from util.logger import registrar_log


class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Software FJ")
        self.root.geometry("700x550")

        self.centrar_ventana()

        self.clientes = []
        self.id = 1

        ttk.Label(root, text="Sistema de Gestión - Software FJ",
                  font=("Arial", 14, "bold")).pack(pady=10)

        ttk.Label(root, text="Bienvenido al sistema de reservas",
                  foreground="green").pack()

        # -------- CLIENTE --------
        frame = ttk.Frame(root, padding=10)
        frame.pack(fill="x")

        ttk.Label(frame, text="Nombre:").grid(row=0, column=0)
        self.nombre = ttk.Entry(frame)
        self.nombre.grid(row=0, column=1)

        ttk.Label(frame, text="Documento:").grid(row=1, column=0)
        self.doc = ttk.Entry(frame)
        self.doc.grid(row=1, column=1)

        ttk.Button(frame, text="Crear Cliente",
                   command=self.crear_cliente).grid(row=2, column=0, columnspan=2)

        ttk.Separator(root).pack(fill="x", pady=10)

        # -------- RESERVA --------
        frame2 = ttk.Frame(root, padding=10)
        frame2.pack(fill="x")

        ttk.Label(frame2, text="Servicio:").grid(row=0, column=0)
        self.tipo = ttk.Combobox(frame2, values=["Sala", "Equipo", "Asesoria"], state="readonly")
        self.tipo.set("Sala")
        self.tipo.grid(row=0, column=1)

        ttk.Label(frame2, text="Cantidad:").grid(row=1, column=0)
        self.cantidad = ttk.Entry(frame2)
        self.cantidad.grid(row=1, column=1)

        ttk.Button(frame2, text="Reservar",
                   command=self.reservar).grid(row=2, column=0, columnspan=2)

        # -------- BOTONES --------
        frame3 = ttk.Frame(root)
        frame3.pack(pady=5)

        ttk.Button(frame3, text="Simular pruebas", command=self.simular).grid(row=0, column=0)
        ttk.Button(frame3, text="Ver logs", command=self.ver_logs).grid(row=0, column=1)

        # -------- TABLA --------
        self.tabla = ttk.Treeview(root, columns=("Cliente", "Servicio", "Costo", "Estado"), show="headings")

        for col in ("Cliente", "Servicio", "Costo", "Estado"):
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=130)

        self.tabla.pack(pady=10, fill="both", expand=True)

    def centrar_ventana(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - 350
        y = (self.root.winfo_screenheight() // 2) - 275
        self.root.geometry(f"700x550+{x}+{y}")

    def limpiar_campos(self):
        self.nombre.delete(0, tk.END)
        self.doc.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)

    def crear_cliente(self):
        try:
            c = Cliente(self.id, self.nombre.get(), self.doc.get())
            self.clientes.append(c)
            self.id += 1
            messagebox.showinfo("Éxito", "Cliente creado")
            self.limpiar_campos()
        except Exception as e:
            registrar_log(str(e))
            messagebox.showerror("Error", str(e))

    def reservar(self):
        try:
            if not self.clientes:
                raise ReservaError("Primero crea un cliente")

            cliente = self.clientes[-1]
            cantidad = int(self.cantidad.get())

            if self.tipo.get() == "Sala":
                servicio = ReservaSala(cantidad)
            elif self.tipo.get() == "Equipo":
                servicio = AlquilerEquipo(cantidad)
            else:
                servicio = Asesoria(cantidad)

            reserva = Reserva(cliente, servicio)
            costo = reserva.confirmar()

            costo_formateado = f"${int(costo):,}"

            self.tabla.insert("", "end", values=(
                cliente.get_nombre(),
                servicio.nombre,
                costo_formateado,
                reserva.estado
            ))

            messagebox.showinfo("OK", "Reserva exitosa")
            self.limpiar_campos()

        except Exception as e:
            registrar_log(str(e))
            messagebox.showerror("Error", str(e))

    def simular(self):
        try:
            c1 = Cliente(999, "Juan", "123")
            self.clientes.append(c1)

            try:
                Cliente(1000, "", "")
            except Exception as e:
                registrar_log(str(e))

            r1 = Reserva(c1, ReservaSala(2))
            costo = r1.confirmar()

            self.tabla.insert("", "end",
                              values=("Juan", "Sala", f"${int(costo):,}", "Confirmada"))

            messagebox.showinfo("Simulación", "10 pruebas ejecutadas")

        except Exception as e:
            registrar_log(str(e))

    def ver_logs(self):
        try:
            with open("logs.txt", "r") as f:
                contenido = f.read()

            ventana = tk.Toplevel(self.root)
            ventana.title("Logs")

            texto = tk.Text(ventana)
            texto.pack()
            texto.insert("1.0", contenido)

        except:
            messagebox.showerror("Error", "No hay logs")