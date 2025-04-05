import os
import sqlite3 as sq
from classes import *


PATH = f"{os.getcwd()}/InventorySystem/storage/.db"


def connect():
    db = sq.connect(PATH)
    return (db, db.cursor())

def disconnect(db):
    db.commit()
    db.close()

def add_vehicle(vehicle):
    db, cur = connect()
    cur.execute(f"INSERT INTO vehicles VALUES {vehicle.getData()}")
    disconnect(db)

def all_vehicles():
    db, cur = connect()
    cur.execute("SELECT * FROM vehicles")
    data = cur.fetchall()
    disconnect(db)
    return data  

def get_vehicle(id):
    db, cur = connect()
    cur.execute(f"SELECT * FROM vehicles WHERE stock_number='{id}'")
    data = cur.fetchone()
    disconnect(db)
    return data

def get_all_vehicles_by_status(status):
    db, cur = connect()
    cur.execute(f"SELECT * FROM vehicles WHERE status='{status}'")
    data = cur.fetchall()
    disconnect(db)
    return data

def del_vehicle(id):
    pass


def add_customer():
    pass

def get_customer(id):
    pass

def edit_customer(id):
    pass

def del_customer(id):
    pass

   
if __name__ == "__main__":
    # CREATE .db file and open it
    db = sq.connect(PATH)
    
    # CREATE Vehicles Table
    cur = db.cursor()
    # cur.execute("CREATE TABLE vehicles (stock_number, vin, make, model, year, odometer, purchase_cost, repair_cost, total_cost, status)")
    
    # # CREATE Customers Table
    # cur.execute("CREATE TABLE customers (first_name, last_name, address, phone, stock_number)")
    
    
    test_vehicles = [
        Vehicle("SAK5634LA78954023","PORSCHE", "911", 2023, 2013, 85054.00),
        Vehicle("SAK5634LA12348646","BMW", "M4", 2016, 30244, 67323.00),
        Vehicle("SAK5634LA76S46586","TOYOTA", "TACOMA", 2007, 250321, 2340.00),
        Vehicle("SAK5634LA71323468","MAZDA", "MIATA", 2014, 120325, 2567.00),
        Vehicle("SAK5634LA86363255","VOLKSWAGEN", "BEETLE", 2016, 56238, 6532.00),
        Vehicle("SAK5634LA78788543","VOLKSWAGEN", "GTI", 2003, 150065, 6524.00),
    ]
    
    test_customers = [
        Customer("Testie", "McTesterson", "1234 Who GAF Ln", 8135558565, "A123475"),
        Customer("Bessie", "McTesterson Jr", "1236 Who GAF Ln", 8135558566, "A123475"),
        Customer("Lessie", "McTesterson III", "1238 Who GAF Ln", 8135558567, "A123475"),
        Customer("Dressie", "McTesterson IV", "1242 Who GAF Ln", 8135558568, "A123475"),
        Customer("Frank", "McTesterson-Whichowski", "5647 Oddball Way", 7276668569, "L123455"),
    ]
    
    # db_veh = []
    
    # for vehicle in test_vehicles:
    #     db_veh.append(vehicle.get_data())
        
    # # print(db_veh)
    # cur.executemany("INSERT INTO vehicles VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", db_veh)
    # db.commit()
    # db.close()
    

    db_all_veh = all_vehicles()
    
    for vehicle in db_all_veh:
        print(vehicle)
    # veh = get_vehicle('1323468')
    # print(vehs)