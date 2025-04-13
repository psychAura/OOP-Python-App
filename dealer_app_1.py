import customtkinter as ctk
from tkinter import messagebox

class Car:

    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.sold = False

    def get_info(self):
        return f"{self.year} {self.make} {self.model} - ${self.price}"

    def sell(self):
        if not self.sold:
            self.sold = True
            return f"{self.get_info()} has been sold!"
        else:
            return f"{self.get_info()} is already sold."


class Dealership:
    def __init__(self):
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)

    def show_inventory(self):
        if not self.inventory:
            return "No cars available."
        return ",".join(car.get_info() for car in self.inventory if not car.sold)

    def sell_car(self, make, model):
        for car in self.inventory:
            if car.make == make and car.model == model and not car.sold:
                return car.sell()
        return "Car not found or already sold."


class CarSalesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KAKLyM Dealership App")
        self.root.geometry("500x450")
        self.root.configure(bg="white")

        # Initialize dealership
        self.dealership = Dealership()
        self.selected_car = None  # To store selected car information

        # CustomTkinter style configuration
        self.header = ctk.CTkLabel(root, text="🚗 KAKLyM Dealership App", font=("Arial", 14, "bold"))
        self.header.pack(fill="x", pady=10)

        # Input frame for adding cars
        self.input_frame = ctk.CTkFrame(root)
        self.input_frame.pack(pady=10, fill="x", padx=10)

        self.make_label = ctk.CTkLabel(self.input_frame, text="Car Make:")
        self.make_label.grid(row=0, column=0, sticky="w")
        self.model_label = ctk.CTkLabel(self.input_frame, text="Car Model:")
        self.model_label.grid(row=1, column=0, sticky="w")
        self.year_label = ctk.CTkLabel(self.input_frame, text="Car Year:")
        self.year_label.grid(row=2, column=0, sticky="w")
        self.price_label = ctk.CTkLabel(self.input_frame, text="Car Price ($):")
        self.price_label.grid(row=3, column=0, sticky="w")

        self.make_entry = ctk.CTkEntry(self.input_frame)
        self.model_entry = ctk.CTkEntry(self.input_frame)
        self.year_entry = ctk.CTkEntry(self.input_frame)
        self.price_entry = ctk.CTkEntry(self.input_frame)

        self.make_entry.grid(row=0, column=1, padx=5, pady=2)
        self.model_entry.grid(row=1, column=1, padx=5, pady=2)
        self.year_entry.grid(row=2, column=1, padx=5, pady=2)
        self.price_entry.grid(row=3, column=1, padx=5, pady=2)

        # Add and Sell Buttons
        self.add_button = ctk.CTkButton(self.input_frame, text="Add Car", command=self.add_car, fg_color="green", font=("Arial", 10, "bold"))
        self.add_button.grid(row=4, column=0, pady=5)

        self.sell_button = ctk.CTkButton(self.input_frame, text="Sell Car", command=self.sell_car, fg_color="red", font=("Arial", 10, "bold"))
        self.sell_button.grid(row=4, column=1, pady=5)

        # Inventory frame
        self.inventory_frame = ctk.CTkFrame(root)
        self.inventory_frame.pack(pady=10, fill="both", expand=True, padx=10)

        # Inventory Textbox
        self.inventory_textbox = ctk.CTkTextbox(self.inventory_frame, height=8, state="normal", fg_color="white", font=("Arial", 10))
        self.inventory_textbox.pack(side="left", fill="both", expand=True)

        # Scrollbar for inventory list
        self.scrollbar = ctk.CTkScrollbar(self.inventory_frame, command=self.inventory_textbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.inventory_textbox.configure(yscrollcommand=self.scrollbar.set)

        # Bind the Textbox selection to enable selling the selected car
        self.inventory_textbox.bind("<ButtonRelease-1>", self.select_car)

    def add_car(self):
        make = self.make_entry.get()
        model = self.model_entry.get()
        year = self.year_entry.get()
        price = self.price_entry.get()

        if make and model and year.isdigit() and price.isdigit():
            car = Car(make, model, int(year), int(price))
            self.dealership.add_car(car)
            self.update_inventory_textbox()
            messagebox.showinfo("Success", "Car added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter valid details.")

    def sell_car(self):
        if self.selected_car:
            make, model = self.selected_car
            sale_message = self.dealership.sell_car(make, model)
            messagebox.showinfo("Sale", sale_message)
            self.selected_car = None  # Reset the selected car after selling
            self.update_inventory_textbox()
        else:
            messagebox.showerror("Error", "Please select a car to sell.")

    def update_inventory_textbox(self):
        self.inventory_textbox.delete("1.0", "end")
        for car in self.dealership.inventory:
            if not car.sold:
                self.inventory_textbox.insert("end", car.get_info() + "\n")

    def select_car(self, event):
        """Handle selecting a car in the inventory textbox."""
        car_info = self.inventory_textbox.get("1.0", "end-1c").split("\n")
        for idx, car in enumerate(car_info):
            if car.strip():
                # Check if the click position is within the selected line
                if event.y >= (idx * 20) and event.y <= ((idx + 1) * 20):
                    self.selected_car = car.split(" ")[1:3]  # Extract make and model
                    break
        self.sell_button.configure(state="normal" if self.selected_car else "disabled")

    def clear_entries(self):
        self.make_entry.delete(0, "end")
        self.model_entry.delete(0, "end")
        self.year_entry.delete(0, "end")
        self.price_entry.delete(0, "end")


if __name__ == "__main__":
    root = ctk.CTk()
    app = CarSalesApp(root)
    root.mainloop()
