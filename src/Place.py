import tkinter as tk
from tkinter import font
from functools import partial


class Place(tk.Frame):
    def __init__(self, parent, controller, place):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        tk.Label(self, text=place["name"], font=font.Font(size=20)).pack()

        #image
        img = tk.PhotoImage(file=place["image"]).zoom(2, 2)
        place_image = tk.Label(self, image=img)
        place_image.image = img
        place_image.pack()

        # Conexion con la reservacion
        tk.Button(self, text="Reservar",
                  command=lambda: self.show_reservation_window(place)).pack()

    def show_reservation_window(self, place):
        from Reservation import Reservation
        frame = Reservation(self.parent, self.controller, place)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
