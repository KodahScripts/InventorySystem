import tkinter as tk
from .db import all_vehicles
from .globals import LARGE_FONT

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        
        vehicles = all_vehicles()

        tk.Label(self, text="Home", font=LARGE_FONT).pack()
        tk.Button(self, text="ADD", command=lambda: self.controller.show_frame(AddVehiclePage)).pack()

        self.all_vehicles_list = tk.Listbox(self)
        for index, vehicle in enumerate(vehicles):
            self.all_vehicles_list.insert(index, vehicle)

        self.all_vehicles_list.pack(fill="both", expand=True, padx=5, pady=5)
        self.all_vehicles_list.bind("<Double-Button-1>", self.select_vehicle)

    def select_vehicle(self, event):
        # print(self.all_vehicles_list.get(self.all_vehicles_list.curselection()))
        self.controller.show_frame(EditVehiclePage)


class AddVehiclePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        window_header = tk.Frame(self)
        content = tk.Frame(self)
        row_1 = tk.Frame(content)
        row_2 = tk.Frame(content)
        row_3 = tk.Frame(content)
        row_4 = tk.Frame(content)
        row_5 = tk.Frame(content)

        tk.Label(window_header, text="Add Vehicle", font=LARGE_FONT).pack(side=tk.LEFT)
        tk.Button(window_header, text="CANCEL", command=lambda: controller.show_frame(HomePage)).pack(side=tk.RIGHT)
        
        tk.Label(row_1, text="VIN").pack(side=tk.LEFT, padx=10)
        self.vin_number_entry = tk.Entry(row_1)
        self.vin_number_entry.pack(side=tk.RIGHT, padx=10)
        
        tk.Label(row_2, text="MAKE").pack(side=tk.LEFT, padx=10)
        self.veh_make_entry = tk.Entry(row_2)
        self.veh_make_entry.pack(side=tk.RIGHT, padx=10)
        
        tk.Label(row_3, text="MODEL").pack(side=tk.LEFT, padx=10)
        self.veh_model_entry = tk.Entry(row_3)
        self.veh_model_entry.pack(side=tk.RIGHT, padx=10)
        
        tk.Label(row_4, text="ODOMETER").pack(side=tk.LEFT, padx=10)
        self.odo_number_entry = tk.Entry(row_4)
        self.odo_number_entry.pack(side=tk.RIGHT, padx=10)

        tk.Button(row_5, text="SUBMIT", command=self.submit_form).pack(fill=tk.BOTH, padx=10, pady=10)

        row_1.pack(side=tk.TOP, fill=tk.X, pady=2)
        row_2.pack(side=tk.TOP, fill=tk.X, pady=2)
        row_3.pack(side=tk.TOP, fill=tk.X, pady=2)
        row_4.pack(side=tk.TOP, fill=tk.X, pady=2)
        row_5.pack(side=tk.TOP, fill=tk.X)

        window_header.pack(side=tk.TOP, fill=tk.X, pady=10)
        content.pack(fill=tk.BOTH, pady=10)

    def submit_form(self):
        print(self.vin_number_entry.get())
        print(self.veh_make_entry.get())
        print(self.veh_model_entry.get())
        print(self.odo_number_entry.get())


class EditVehiclePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="Edit Vehicle", font=LARGE_FONT).pack()
        tk.Button(self, text="CANCEL", command=lambda: controller.show_frame(HomePage)).pack()
