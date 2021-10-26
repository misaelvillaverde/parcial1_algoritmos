import tkinter as tk

from TuristicAgency import TuristicAgency
from main import FrameController


class Presentation(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: FrameController):

        tk.Frame.__init__(self, parent)
        tk.Label(self, text="UNIVERSIDAD TECNOLÓGICA DE PANAMÁ").place(
            x=325, y=20)
        tk.Label(self, text="FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES").place(
            x=275, y=40)
        tk.Label(self, text="DEPARTAMENTO DE INGENIERÍA DE SOFTWARE").place(
            x=310, y=60)
        tk.Label(self, text="CARRERA DE LICENCIATURA EN INGENIERÍA DE SOFTWARE").place(
            x=285, y=80)

        tk.Label(self, text="PARCIAL #1").place(x=415, y=140)

        tk.Label(self, text="Integrantes:").place(x=415, y=200)
        tk.Label(self, text="-Diego Burgos").place(x=408, y=220)
        tk.Label(self, text="-Luis Carreyó").place(x=410, y=240)
        tk.Label(self, text="-Misael Villaverde").place(x=400, y=260)
        tk.Label(self, text="-Ricky Pan").place(x=415, y=280)
        tk.Label(self, text="-Bernardo Espinosa").place(x=395, y=300)

        tk.Label(self, text="Profesor:").place(x=420, y=360)
        tk.Label(self, text="Ing. Samuel Jiménez").place(x=390, y=380)

        tk.Label(self, text="II SEMESTRE").place(x=410, y=440)

        tk.Label(self, text="Panamá, 2021").place(x=405, y=500)

        tk.Button(self, text="Siguiente",
                  command=lambda: controller.show_frame(TuristicAgency)).place(x=775, y=545)
