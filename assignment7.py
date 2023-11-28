import tkinter as tk

class VehicleError(Exception):
    pass

class FlatTireError(VehicleError):
    pass

class EngineFailureError(VehicleError):
    pass

class Vehicle:
    def __init__(self, model):
        self.model = model

    def display_info(self):
        print(f"Vehicle Model: {self.model}")

class Car(Vehicle):
    def __init__(self, model):
        super().__init__(model)

class Truck(Vehicle):
    def __init__(self, model):
        super().__init__(model)

"""GUI class is commented out for later implementation."""
# class CreateGui:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.canvas = tk.Canvas(self.root, height=400, width=400, bg="lightgray")
#         """Create a text box"""
#         self.textbox = tk.Entry(self.root)
#         self.textbox.pack()
#         #a sets the lable with its name
#         self.label = tk.Label(self.root, text="This is label")
#         #Using pack as supposed to grind to set size of widget
#         self.label.pack(pady =50)
#         button = tk.Button(self.root, text= "Useful name TBD", command=self.copy_text)

#     """Take text from text box"""
#     def copy_text(self):
#     #.config is used to create a setting that can be called to.
#     #The text entered will added to our label using textbox.get()
#         self.label.config(text=self.textbox.get())

#     """Method for creating buttons"""
#     def create_button(self, name, action="no action selected"):
#         if action == "no action selected":
#             button = tk.Button(self.root, text=name, command=self.copy_text)
#         else:
#             button = tk.Button(self.root, text=name, command=action)
#         self.buttons[name] = button
#         button.pack()

# Simulating a scenario
try:
    car = Car("Sedan")
    truck = Truck("Pickup")

    # Displaying valid information
    car.display_info()
    truck.display_info()

    # Simulating an exception (Flat tire)
    raise FlatTireError("Flat tire detected")

except VehicleError as ve:
    print(f"Handling Vehicle Error: {ve}")

except FlatTireError as fte:
    print(f"Handling Flat Tire Error: {fte}")

except Exception as e:
    print(f"Unhandled Exception: {e}")
