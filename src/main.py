import tkinter as tk


class FrameController(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Agencias de viajes DMLR")
        self.geometry("900x600")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        from Presentation import Presentation
        from TuristicAgency import TuristicAgency
        for Frame in (Presentation, TuristicAgency):
            frame = Frame(container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[Frame] = frame

        self.show_frame(Presentation)

    def show_frame(self, frame):
        """
        Show a frame for the given page name

        Parameters
        ----------
        frame : Frame 
        """
        self.frames[frame].tkraise()


def main():
    app = FrameController()
    app.mainloop()


if __name__ == "__main__":
    main()
