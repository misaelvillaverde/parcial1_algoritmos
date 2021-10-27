import tkinter as tk
import requests
from constants import URL
from tkinter import messagebox


class Reservation(tk.Frame):
    def __init__(self, parent, controller, place):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Reservación", font=(
            "Arial", 20)).place(x=375, y=40)

        self.place_name = place["name"]
        self.place_cost = place["cost"]

        self.totalCost = 0
        self.deductedCost = 0
        self.currentDebt = 0

        # Totals
        self.total = tk.Label(
            self, text=f"Total: {self.totalCost}", font=("Arial", 12))
        self.reduced_total = tk.Label(
            self, text=f"Total a pagar: {self.deductedCost}", font=("Arial", 12))
        self.debt_label = tk.Label(
            self, text=f"Deuda restante: {self.currentDebt}", font=("Arial", 12))

        # Variables
        self.genre = tk.StringVar()
        self.userId = tk.StringVar()
        self.email = tk.StringVar()
        self.age = tk.IntVar()
        self.nationality = tk.StringVar()
        self.name = tk.StringVar()
        self.people_qty = tk.IntVar()
        self.phone = tk.StringVar()
        self.abono = tk.DoubleVar()
        self.retired = tk.IntVar()

        # Labels and entries
        tk.Label(self, text="Genero:", font=("Arial", 12)).place(x=260, y=110)
        tk.Entry(self, textvariable=self.genre).place(x=230, y=140)

        tk.Label(self, text="Cedula:", font=("Arial", 12)).place(x=260, y=170)
        tk.Entry(self, textvariable=self.userId).place(x=230, y=200)

        tk.Label(self, text="Nacionalidad:", font=(
            "Arial", 12)).place(x=240, y=230)
        tk.Entry(self, textvariable=self.nationality).place(x=230, y=260)

        tk.Label(self, text="Nombre:", font=("Arial", 12)).place(x=260, y=290)
        tk.Entry(self, textvariable=self.name).place(x=230, y=320)

        tk.Label(self, text="Edad:", font=("Arial", 12)).place(x=260, y=350)
        tk.Entry(self, textvariable=self.age).place(x=230, y=380)

        tk.Label(self, text="Email:", font=("Arial", 12)).place(x=580, y=110)
        tk.Entry(self, textvariable=self.email).place(x=540, y=140)

        tk.Label(self, text="Cantidad de personas:",
                 font=("Arial", 12)).place(x=530, y=170)
        tk.Entry(self, textvariable=self.people_qty).place(x=540, y=200)

        tk.Label(self, text="Numero celular:", font=(
            "Arial", 12)).place(x=550, y=230)
        tk.Entry(self, textvariable=self.phone).place(x=540, y=260)

        tk.Label(self, text="Abono", font=("Arial", 12)).place(x=575, y=290)
        tk.Entry(self, textvariable=self.abono).place(x=540, y=320)

        tk.Checkbutton(self, text='Jubilado?', variable=self.retired,
                       onvalue=1, offvalue=0, command=self.calculate_cost, font=(
                           "Arial", 12)).place(x=540, y=350)

        self.total.place(x=230, y=420)
        self.reduced_total.place(x=230, y=445)
        self.debt_label.place(x=230, y=470)

        # Images
        palmera = tk.PhotoImage(
            file="../assets/factura/palmeras.png").subsample(2)
        palm1 = tk.Label(self, image=palmera)
        palm1.place(x=-225, y=0)
        palm1.image = palmera
        palm2 = tk.Label(self, image=palmera)
        palm2.place(x=720, y=0)
        palm2.image = palmera

        # Botones
        tk.Button(self, text="Calcular Precio",
                  command=self.calculate_cost, width=15, height=2).place(x=290, y=520)
        tk.Button(self, text="Agregar a factura", command=self.submit,
                  width=15, height=2).place(x=490, y=520)

        from TuristicAgency import TuristicAgency
        tk.Button(self, text="Regresar",
                  command=lambda: controller.show_frame(TuristicAgency)).place(x=790, y=520)

    def calculate_cost(self):
        self.totalCost = self.people_qty.get() * self.place_cost
        self.deductedCost = self.totalCost

        if self.retired.get() == 1:
            self.deductedCost -= (self.totalCost * 0.1)
        if self.people_qty.get() >= 3:
            self.deductedCost -= (self.totalCost * 0.15)
        if self.totalCost > 2000:
            self.deductedCost -= (self.totalCost * 0.05)

        self.currentDebt = self.deductedCost - self.abono.get()

        self.total["text"] = f"Total sin deducciones: ${self.totalCost:.2f}"
        self.reduced_total["text"] = f"Total a pagar: ${self.deductedCost:.2f}"
        self.debt_label["text"] = f"Deuda restante: ${self.currentDebt:.2f}"

        print(f"Total: {self.totalCost}")
        print(f"Total a pagar: {self.deductedCost}")
        print(f"Deuda restante: {self.currentDebt}")

    def submit(self):
        print("Agregando a factura...")
        payload = {
            "userId": self.userId.get(),
            "name": self.name.get(),
            "genre": self.genre.get(),
            "phone": self.phone.get(),
            "email": self.email.get(),
            "nationality": self.nationality.get(),
            "peopleQty": self.people_qty.get(),
            "currentDebt": self.currentDebt,
            "placeName": self.place_name,
            "totalCost": self.totalCost
        }
        headers = {"Content-Type": "application/json"}

        response = requests.request(
            "POST", URL+"/bookings", json=payload, headers=headers)

        print(response.json())

        try:
            if response.json()["_id"] != None:
                messagebox.showinfo(
                    title="Reserva", message=f"Reserva realizada con exito\nid: {response.json()['_id']}")
        except:
            messagebox.showerror(
                title="Reserva", message="Error al realizar la reserva")
