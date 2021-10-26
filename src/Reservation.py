import tkinter as tk


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
        tk.Label(self, text="Genero:").pack()
        tk.Entry(self, textvariable=genre).pack()

        tk.Label(self, text="Cedula:").pack()
        tk.Entry(self, textvariable=userId).pack()

        tk.Label(self, text="Nacionalidad:").pack()
        tk.Entry(self, textvariable=nationality).pack()

        tk.Label(self, text="Nombre:").pack()
        tk.Entry(self, textvariable=name).pack()

        tk.Label(self, text="Cantidad:").pack()
        tk.Entry(self, textvariable=amount).pack()

        tk.Label(self, text="Numero celular:").pack()
        tk.Entry(self, textvariable=phone).pack()
# Botones
        tk.Button(self, text="Pagar").pack(side="left")
        tk.Button(self, text="Abono").pack(side="right")
