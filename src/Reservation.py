import tkinter as tk
import requests
from constants import URL


class Reservation(tk.Frame):
    def __init__(self, parent, controller, place):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Reservation", font=("Helvetica", 16)).pack()
        self.place_name = place["name"]
        self.place_cost = place["cost"]
# Variables
        self.genre = tk.StringVar()
        self.userId = tk.StringVar()
        self.email = tk.StringVar()
        self.nationality = tk.StringVar()
        self.name = tk.StringVar()
        self.people_qty = tk.IntVar()
        self.phone = tk.StringVar()
        self.abono = tk.DoubleVar()

# Texto y Barra
        tk.Label(self, text="Genero:", pady=20).pack()
        tk.Entry(self, textvariable=self.genre).pack()

        tk.Label(self, text="Cedula:", pady=20).pack()
        tk.Entry(self, textvariable=self.userId).pack()

        tk.Label(self, text="Nacionalidad:", pady=20).pack()
        tk.Entry(self, textvariable=self.nationality).pack()

        tk.Label(self, text="Nombre:", pady=20).pack()
        tk.Entry(self, textvariable=self.name).pack()

        tk.Label(self, text="Email:", pady=20).pack()
        tk.Entry(self, textvariable=self.email).pack()

        tk.Label(self, text="Cantidad de personas:", pady=20).pack()
        tk.Entry(self, textvariable=self.people_qty).pack()

        tk.Label(self, text="Numero celular:", pady=20).pack()
        tk.Entry(self, textvariable=self.phone).pack()

        tk.Label(self, text="Abono", pady=20).pack()
        tk.Entry(self, textvariable=self.abono).pack()
# Botones
        tk.Button(self, text="Agregar a factura", command=self.submit).pack(
            side=tk.LEFT, expand=True)

    def submit(self):
        totalCost = self.people_qty.get() * self.place_cost
        currentDebt = totalCost - self.abono.get()

        print("Agregando a factura...")
        payload = {
            "userId": self.userId.get(),
            "name": self.name.get(),
            "genre": self.genre.get(),
            "phone": self.phone.get(),
            "email": self.email.get(),
            "nationality": self.nationality.get(),
            "peopleQty": self.people_qty.get(),
            "currentDebt": currentDebt,
            "placeName": self.place_name,
            "totalCost": totalCost
        }
        headers = {"Content-Type": "application/json"}

        response = requests.request(
            "POST", URL+"/bookings", json=payload, headers=headers)

        print(response.text)
