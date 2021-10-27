import tkinter as tk
from constants import URL, LOCAL
import requests
from functools import partial


class TuristicAgency(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        # Styles

        logo = tk.PhotoImage(
            file="../assets/portada/Logo Borokotroko.png").subsample(2)
        label_logo = tk.Label(self, image=logo)
        label_logo.place(x=105, y=1)
        label_logo.image = logo

        promo = tk.PhotoImage(file="../assets/portada/promo1.png").subsample(5)
        label_promo = tk.Label(self, image=promo)
        label_promo.place(x=20, y=300)
        label_promo.image = promo

        promo2 = tk.PhotoImage(
            file="../assets/portada/Promo2.png").subsample(5)
        label_promo2 = tk.Label(self, image=promo2)
        label_promo2.place(x=315, y=300)
        label_promo2.image = promo2

        promo3 = tk.PhotoImage(
            file="../assets/portada/Promo3.png").subsample(5)
        label_promo3 = tk.Label(self, image=promo3)
        label_promo3.place(x=605, y=300)
        label_promo3.image = promo3

        tk.Label(self, text="Selecciona el lugar en la barra de menu").place(
            x=350, y=500)

        from Invoice import Invoice
        tk.Button(self, text="Ver Factura", command=lambda: self.controller.show_frame(
            Invoice)).place(x=700, y=500)

        # Province controller
        menubar = tk.Menu(controller, tearoff=0)

        controller.config(menu=menubar)

        province_menu = tk.Menu(menubar, tearoff=0)
        comarca_menu = tk.Menu(menubar, tearoff=0)

        provinces = self.getProvinces()
        for province in provinces:
            actual_province = partial(self.show_province, province)

            if not province["indigenousRegion"]:
                province_menu.add_command(
                    label=province["name"], command=actual_province)
            else:
                comarca_menu.add_command(
                    label=province["name"], command=actual_province)

        menubar.add_cascade(label='Provincias', menu=province_menu)
        menubar.add_cascade(label='Comarcas', menu=comarca_menu)

    def show_province(self, province):
        from Province import Province
        frame = Province(self.parent, self.controller, province)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def getProvinces(self):
        return requests.get(f"{URL}/provinces").json()
