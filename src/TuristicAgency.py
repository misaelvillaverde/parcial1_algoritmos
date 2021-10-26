import tkinter as tk
from constants import URL, LOCAL
import requests
from functools import partial


class TuristicAgency(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        menubar = tk.Menu(controller, tearoff=0)

        controller.config(menu=menubar)

        province_menu = tk.Menu(menubar)
        comarca_menu = tk.Menu(menubar)

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
