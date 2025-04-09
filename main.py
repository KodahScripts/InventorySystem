import tkinter as tk

from utils.pages import HomePage, AddVehiclePage, EditVehiclePage


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Inventory")
        self.geometry("600x400")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, AddVehiclePage, EditVehiclePage):
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()