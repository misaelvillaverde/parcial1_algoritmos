import tkinter as tk
from tkinter.constants import TRUE


class Reservation(tk.Frame):
    def __init__(self, parent, controller, place):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Reservation", font=("Helvetica", 16)).pack()
# Variables
        genre = tk.StringVar
        userId = tk.StringVar
        nationality = tk.StringVar
        name = tk.StringVar
        amount = tk.StringVar
        phone = tk.StringVar
# Texto y Barra
        tk.Label(self, text="Genero:",pady=20).pack()
        tk.Entry(self, textvariable=genre).pack()

        tk.Label(self, text="Cedula:",pady=20).pack()
        tk.Entry(self, textvariable=userId).pack()

        tk.Label(self, text="Nacionalidad:",pady=20).pack()
        tk.Entry(self, textvariable=nationality).pack()

        tk.Label(self, text="Nombre:",pady=20).pack()
        tk.Entry(self, textvariable=name).pack()

        tk.Label(self, text="Cantidad:",pady=20).pack()
        tk.Entry(self, textvariable=amount).pack()

        tk.Label(self, text="Numero celular:",pady=20).pack()
        tk.Entry(self, textvariable=phone).pack()
# Botones
        tk.Button(self, text="Pagar").pack(
                    side=tk.LEFT,expand=TRUE)
        tk.Button(self, text="Abono").pack(
                    side=tk.LEFT,expand=TRUE)
#aki