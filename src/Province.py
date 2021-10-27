import tkinter as tk
from tkinter import font
from functools import partial


class Province(tk.Frame):
    def __init__(self, parent, controller, province):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        # Left frame
        frame_province = tk.Frame(
            self, bg='#f0f0f0')
        frame_province.pack(fill=tk.BOTH, expand=True)

        # Right frame
        frame_turism = tk.Frame(
            self, bg='#f0f0f0')
        frame_turism.pack(fill=tk.X, expand=True)

        # Province name
        tk.Label(frame_province, text=province["name"], font=(
            60), pady=20).pack()

        # image
        img = tk.PhotoImage(file=province["image"]).zoom(2, 2)
        province_image = tk.Label(frame_province, image=img)
        province_image.image = img
        province_image.pack()

        # description
        tk.Label(frame_province,
                 text=province["description"], wraplength=500, justify=tk.LEFT).pack()

        # turistic places
        if len(province["turisticPlaces"]) <= 0:
            tk.Label(frame_turism, text="No tiene lugares turísticos").pack()
        else:
            for place in province["turisticPlaces"]:
                turistic_place = partial(self.show_place, place)
                tk.Button(frame_turism, text=place["name"], command=turistic_place, padx=5).pack(
                    side=tk.LEFT, fill=tk.BOTH, expand=True)

        from TuristicAgency import TuristicAgency
        tk.Button(self, text="volver",
                  command=lambda: controller.show_frame(TuristicAgency)).pack()

    def show_place(self, place):
        from Place import Place
        frame = Place(self.parent, self.controller, place)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
