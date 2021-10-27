import tkinter as tk
from tkinter import messagebox
import requests
from constants import URL


class Invoice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        tk.Label(self, text="Factura", font=(
            "Arial", 20)).pack(pady=10, padx=10)

        self.invoice = []
        self.user_id = tk.StringVar()
        self.subtotal = 0
        self.total = 0

        # User labels
        self.username = tk.Label(self, text="")
        self.username.place(x=10, y=10)
        self.useremail = tk.Label(self, text="")
        self.useremail.place(x=10, y=30)
        self.userphone = tk.Label(self, text="")
        self.userphone.place(x=10, y=50)
        self.usergenre = tk.Label(self, text="")
        self.usergenre.place(x=10, y=70)
        self.usernationality = tk.Label(self, text="")
        self.usernationality.place(x=10, y=90)

        # Invoice frame
        self.invoice_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.invoice_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.bookings = tk.Listbox(self.invoice_frame,
                                   yscrollcommand=self.scrollbar.set)

        self.bookings.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.bookings.yview)

        self.invoice_frame.place(x=10, y=150, width=900, height=400)

        # Input labels
        tk.Label(self, text="Cédula:").pack()
        tk.Entry(self, textvariable=self.user_id).pack()

        tk.Button(self, text="Cargar factura",
                  command=self.cargar_factura).pack()

        # Total labels
        self.subtotal_label = tk.Label(
            self, text="Subtotal:")
        self.subtotal_label.place(x=10, y=550)
        self.total_label = tk.Label(self, text="Total:")
        self.total_label.place(x=10, y=565)

        # Pay button
        tk.Button(self, text="Pagar", command=self.payment).place(x=400, y=560)

    def cargar_factura(self):
        print("Cargando factura...")
        print("ID:", self.user_id.get())

        response = requests.get(URL + "/bookings/" + self.user_id.get())

        try:
            print(response.json())
            if len(response.json()) > 0:
                self.invoice = response.json()
                print("Factura cargada")
            else:
                messagebox.showerror(
                    "Factura", "No se encontraron datos para este id")
        except:
            messagebox.showerror("Factura", "Error al obtener factura")
            return

        self.list_bookings()
        self.username["text"] = f"Usuario: {self.invoice[0]['name']}"
        self.useremail["text"] = f"Email: {self.invoice[0]['email']}"
        self.userphone["text"] = f"Teléfono: {self.invoice[0]['phone']}"
        self.usergenre["text"] = f"Género: {self.invoice[0]['genre']}"
        self.usernationality["text"] = f"Nacionalidad: {self.invoice[0]['nationality']}"

    def list_bookings(self):
        self.bookings.delete(0, tk.END)
        self.subtotal = 0
        self.total = 0
        for booking in self.invoice:
            self.subtotal += booking["totalCost"]
            self.total += booking["currentDebt"]
            self.bookings.insert(
                tk.END, booking['placeName'], f"Cantidad de personas: {booking['peopleQty']}", f"Subtotal: {booking['totalCost']:.2f}", f"Abonado: {booking['payment']:.2f}", f"Total a pagar: {booking['currentDebt']:.2f}", "----------------------------------------------------------------------------------------"
            )

        self.total_label["text"] = f"Total: {self.total}"
        self.subtotal_label["text"] = f"Subtotal: {self.subtotal}"

    def payment(self):
        messagebox.showinfo(
            "Pago", "Pago realizado con éxito\nHasta la próxima")
        from TuristicAgency import TuristicAgency
        self.controller.show_frame(TuristicAgency)
