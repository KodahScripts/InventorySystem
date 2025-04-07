import tkinter as tk
from utils.db import all_vehicles


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inventory")
        self.geometry("1280x720")

        screens = [
            HomeScreen,
            AddCarScreen
        ]

        self.frames = {}
        for F in screens:
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomeScreen)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()


class HomeScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        all_inventory = all_vehicles()
        self.inventory_listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.inventory_listbox.bind("<Double-Button-1>", self.select_vehicle())
        
        for x in all_inventory: self.inventory_listbox.insert(tk.END, x)
        self.inventory_listbox.pack(fill=tk.BOTH, expand=True)
        
        add_car_btn = tk.Button(self, text="ADD", command=lambda: master.show_frame(AddCarScreen))
        add_car_btn.pack()
        
    def select_vehicle(self):
        SelectList = self.inventory_listbox.curselection()
        print([self.inventory_listbox.get(i) for i in SelectList])


class AddCarScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="Add a Vehicle")
        label.pack(pady=10)
        button = tk.Button(self, text="CANCEL", command=lambda: master.show_frame(HomeScreen))
        button.pack()




if __name__ == "__main__":
    app = App()
    app.mainloop()