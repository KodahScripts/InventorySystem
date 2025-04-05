import tkinter as tk
import sqlite3

class InventoryGUI:
    def __init__(self, master):
        self.master = master
        master.title("Inventory")
        master.geometry("600x400")
        
        self.label = tk.Label(master, text="Hello")
        self.label.pack()
        

if __name__ == "__main__":
    root = tk.Tk()
    inv = InventoryGUI(root)
    root.mainloop()
    
    db = sqlite3.connect("./test.db")
    db.close()