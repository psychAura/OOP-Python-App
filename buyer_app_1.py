#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import customtkinter as ctk
from tkinter import messagebox

# Set theme and appearance
ctk.set_appearance_mode("light")  # or "dark"
ctk.set_default_color_theme("blue")  # Can be "dark-blue", "green", etc.

# Car class to represent a car
class Car:
    def __init__(self, brand, model, year, style, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.style = style
        self.price = price

    def get_info(self):
        return f"{self.year} {self.brand} {self.model} ({self.style}) - ${self.price}"

# Dealership class
class Dealership:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)

    def show_inventory(self):
        return [car.get_info() for car in self.inventory]

    def sell_car(self, car_index, buyer):
        if 0 <= car_index < len(self.inventory):
            car = self.inventory.pop(car_index)
            return buyer.purchase_car(car, self.location)
        return "Invalid car selection."

# Buyer class
class Buyer:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def purchase_car(self, car, dealership_location):
        return (f"{self.name} purchased {car.get_info()} from {dealership_location}.\n"
                f"Car will be delivered to {self.location}.")

# Create dealerships
dealerships = [
    Dealership("AutoNation LA", "Los Angeles"),
    Dealership("CarMax NY", "New York"),
    Dealership("Texas Auto", "Houston"),
    Dealership("Florida Wheels", "Miami"),
    Dealership("Chicago Motors", "Chicago"),
    Dealership("Seattle Cars", "Seattle"),
    Dealership("Vegas Rides", "Las Vegas")
]

# Cars list
cars = [
    Car("Toyota", "Camry", 2022, "Sedan", 25000),
    Car("Cadillac", "Escalade", 2021, "SUV", 60000),
    Car("Chevrolet", "Malibu", 2020, "Sedan", 23000),
    Car("Honda", "Civic", 2023, "Hatchback", 27000),
    Car("Hyundai", "Elantra", 2019, "Sedan", 20000),
    Car("Ford", "Mustang", 2022, "Coupe", 45000),
    Car("Tesla", "Model 3", 2023, "Sedan", 55000),
    Car("BMW", "X5", 2021, "SUV", 62000),
    Car("Audi", "A4", 2022, "Sedan", 40000),
    Car("Mercedes-Benz", "C-Class", 2021, "Sedan", 45000),
    Car("Jeep", "Wrangler", 2023, "SUV", 52000),
    Car("Nissan", "Altima", 2022, "Sedan", 27000),
    Car("Kia", "Sorento", 2023, "SUV", 35000),
    Car("Volkswagen", "Passat", 2020, "Sedan", 28000),
    Car("Mazda", "CX-5", 2023, "SUV", 33000),
    Car("Subaru", "Outback", 2021, "SUV", 32000),
    Car("Dodge", "Charger", 2022, "Sedan", 39000),
    Car("Lexus", "RX 350", 2023, "SUV", 48000),
    Car("Infiniti", "QX60", 2021, "SUV", 47000),
    Car("Porsche", "911", 2023, "Coupe", 100000),
    Car("Genesis", "G80", 2022, "Sedan", 56000),
    Car("Lincoln", "Navigator", 2023, "SUV", 85000),
    Car("Buick", "Encore", 2021, "SUV", 28000),
    Car("Chevrolet", "Tahoe", 2022, "SUV", 64000),
    Car("Honda", "Accord", 2023, "Sedan", 31000),
    Car("Toyota", "RAV4", 2022, "SUV", 35000),
    Car("BMW", "M3", 2023, "Sedan", 75000),
    Car("Audi", "Q5", 2021, "SUV", 55000),
    Car("Mercedes-Benz", "E-Class", 2022, "Sedan", 62000),
    Car("Hyundai", "Sonata", 2023, "Sedan", 29000),
    Car("Ford", "Explorer", 2021, "SUV", 45000),
    Car("Jeep", "Grand Cherokee", 2023, "SUV", 51000),
    Car("Mazda", "Mazda3", 2022, "Hatchback", 27000),
    Car("Nissan", "Rogue", 2021, "SUV", 33000),
    Car("Lexus", "ES 350", 2023, "Sedan", 44000),
    Car("Porsche", "Macan", 2023, "SUV", 65000),
    Car("Tesla", "Model Y", 2022, "SUV", 58000),
    Car("Honda", "Pilot", 2023, "SUV", 42000),
    Car("Toyota", "Corolla", 2021, "Sedan", 24000),
    Car("Chevrolet", "Equinox", 2022, "SUV", 29000),
    Car("Ford", "F-150", 2023, "Truck", 50000),
    Car("Dodge", "Durango", 2021, "SUV", 48000),
    Car("Subaru", "Forester", 2023, "SUV", 34000),
    Car("Volkswagen", "Tiguan", 2021, "SUV", 36000),
    Car("GMC", "Yukon", 2022, "SUV", 68000),
    Car("Ram", "1500", 2023, "Truck", 57000),
    Car("Tesla", "Model S", 2023, "Sedan", 90000),
    Car("BMW", "X7", 2022, "SUV", 85000),
    Car("Acura", "MDX", 2023, "SUV", 51000),
    Car("Cadillac", "CT5", 2021, "Sedan", 47000),
    Car("Lincoln", "Aviator", 2022, "SUV", 72000),
    Car("Mazda", "CX-30", 2023, "SUV", 30000),
    Car("Honda", "HR-V", 2022, "SUV", 27000),
    Car("Toyota", "Highlander", 2021, "SUV", 43000),
    Car("Chevrolet", "Blazer", 2022, "SUV", 34000),
    Car("Nissan", "Pathfinder", 2023, "SUV", 42000),
    Car("Ford", "Bronco", 2023, "SUV", 50000),
    Car("Hyundai", "Tucson", 2022, "SUV", 31000),
    Car("Dodge", "Challenger", 2023, "Coupe", 60000),
    Car("Lexus", "GX 460", 2023, "SUV", 64000),
    Car("Volkswagen", "Jetta", 2021, "Sedan", 26000),
    Car("Kia", "Sportage", 2023, "SUV", 29000),
    Car("Tesla", "Cybertruck", 2024, "Truck", 70000),
    Car("GMC", "Sierra", 2023, "Truck", 62000),
    Car("Jeep", "Gladiator", 2023, "Truck", 53000),
    Car("Audi", "RS7", 2023, "Sedan", 120000),
    Car("Porsche", "Cayenne", 2023, "SUV", 86000),
    Car("Ram", "2500", 2023, "Truck", 65000)
]

# Distribute cars to dealerships
for i, car in enumerate(cars):
    dealerships[i % len(dealerships)].add_car(car)

# Buyers list
buyers = [
    Buyer("John Doe", "San Francisco"),
    Buyer("Koby Adisenu", "Accra"),
    Buyer("Jane Smith", "New York"),
    Buyer("Alice Johnson", "Los Angeles"),
    Buyer("Bob Williams", "Houston"),
    Buyer("Charlie Brown", "Chicago"),
    Buyer("Daniel Martinez", "Miami"),
    Buyer("Sophia Wilson", "Seattle"),
    Buyer("Michael Anderson", "Denver"),
    Buyer("Emma Thomas", "Boston"),
    Buyer("Olivia Davis", "Philadelphia"),
    Buyer("Liam Roberts", "Phoenix"),
    Buyer("Noah Harris", "Atlanta"),
    Buyer("Ethan Lewis", "Dallas"),
    Buyer("Ava White", "San Diego"),
    Buyer("James Walker", "Las Vegas"),
    Buyer("Isabella Scott", "Minneapolis"),
    Buyer("Lucas King", "San Antonio"),
    Buyer("Mason Hall", "Detroit"),
    Buyer("Charlotte Allen", "Washington D.C."),
    Buyer("Precious Darkwa", "Pokuase"),
    Buyer("Selorm Yao", "Tema"),
    Buyer("Ibrahim Gyimah", ""),
    Buyer("Seth Agyeman", "East Legon"),
    Buyer("Charlotte Allen", "Washington D.C."),
    Buyer("Elijah Young", "Baltimore")
]

class CarSalesModernApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("880x720")
        self.root.title("🚗 KAKLyM Car Customer System")

        # --- Header ---
        self.header = ctk.CTkLabel(
            master=root,
            text="🚘 KAKLyM Car Customer System",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#1f2937"
        )
        self.header.pack(pady=20)

        # --- Card Frame ---
        self.card_frame = ctk.CTkFrame(master=root, corner_radius=15)
        self.card_frame.pack(pady=10, padx=30, fill="x")

        # Buyer Dropdown
        self.buyer_var = ctk.StringVar()
        self._create_labeled_dropdown(self.card_frame, "Select Buyer:", self.buyer_var, [b.name for b in buyers])

        # Dealership Dropdown
        self.dealership_var = ctk.StringVar()
        self._create_labeled_dropdown(self.card_frame, "Select Dealership:", self.dealership_var, [d.name for d in dealerships])

        # Show Inventory Button
        self.show_button = ctk.CTkButton(
            master=self.card_frame,
            text="🔍 Show Inventory",
            command=self.show_inventory
        )
        self.show_button.pack(pady=12)

        # --- Car Listbox ---
        self.car_listbox = ctk.CTkTextbox(root, height=200, width=760, corner_radius=10)
        self.car_listbox.pack(pady=20)

        # --- Purchase Section ---
        self.purchase_frame = ctk.CTkFrame(master=root, fg_color="transparent")
        self.purchase_frame.pack(pady=10)

        self.index_label = ctk.CTkLabel(master=self.purchase_frame, text="Car Index:", font=("Poppins", 13))
        self.index_label.grid(row=0, column=0, padx=5)

        self.car_index_entry = ctk.CTkEntry(master=self.purchase_frame, width=80)
        self.car_index_entry.grid(row=0, column=1, padx=5)

        self.buy_btn = ctk.CTkButton(master=self.purchase_frame, text="🛒 Buy Car", command=self.purchase_car)
        self.buy_btn.grid(row=0, column=2, padx=5)

    def _create_labeled_dropdown(self, parent, label, var, values):
        ctk.CTkLabel(master=parent, text=label, font=("Poppins", 13)).pack(pady=(15, 5))
        dropdown = ctk.CTkOptionMenu(master=parent, variable=var, values=values)
        dropdown.pack(pady=5)

    def show_inventory(self):
        name = self.dealership_var.get()
        self.selected_dealership = next((d for d in dealerships if d.name == name), None)

        if not self.selected_dealership:
            messagebox.showerror("Error", "Please select a dealership.")
            return

        self.car_listbox.delete("0.0", "end")
        for i, car in enumerate(self.selected_dealership.show_inventory()):
            self.car_listbox.insert("end", f"{i}. {car}\n")

    def purchase_car(self):
        buyer_name = self.buyer_var.get()
        selected_buyer = next((b for b in buyers if b.name == buyer_name), None)

        if not selected_buyer:
            messagebox.showerror("Error", "Please select a buyer.")
            return

        if not self.selected_dealership:
            messagebox.showerror("Error", "Select dealership first.")
            return

        try:
            car_index = int(self.car_index_entry.get())
            result = self.selected_dealership.sell_car(car_index, selected_buyer)
            messagebox.showinfo("Purchase Status", result)
            self.show_inventory()
        except ValueError:
            messagebox.showerror("Error", "Enter valid car index.")

# --- Launch App ---
if __name__ == "__main__":
    app = ctk.CTk()
    CarSalesModernApp(app)
    app.mainloop()


# In[ ]:




