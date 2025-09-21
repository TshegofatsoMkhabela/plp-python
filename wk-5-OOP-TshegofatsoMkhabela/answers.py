class Smartphone:
    """Base Smartphone class with common attributes and methods"""
    
    def __init__(
        self, 
        brand: str, 
        model: str,
        storage_gb: int,
        battery_capacity_mAh: int
    ):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_capacity_mAh = battery_capacity_mAh
        self.is_on = False
    
     # Method to turn the phone on/off
    def power(self) -> None:
        self.is_on = not self.is_on
        state = "ON" if self.is_on else "OFF"
        print(f"{self.brand} {self.model} is now {state}")
        
    # Method to display phone info
    def phone_info(self) -> str:
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage_gb}GB, Battery: {self.battery_capacity_mAh}mAh"

# Inherited class
class GamingPhone(Smartphone):
    def __init__(
        self, 
        brand: str, 
        model: str, 
        storage_gb: int, 
        battery_capacity_mAh: int, 
        cooling_system: str
    ):
        super().__init__(brand, model, storage_gb, battery_capacity_mAh)
        
        # Unique attribute
        self.cooling_system = cooling_system  

    # Polymorphism: override phone_info method
    def phone_info(self):
        super().phone_info()
        return f"Cooling System: {self.cooling_system}"

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 4000)
print(phone1.phone_info())
phone1.power()

gaming_phone = GamingPhone("ASUS", "ROG Phone 7", 512, 6000, "Advanced Liquid Cooling")
print(gaming_phone.phone_info())
gaming_phone.power()
     
# ============================ Activity 2: Polymorphism Challenge! ====================== #

class Vehicle:
    def move(self):
        pass 

# Subclasses
class Car(Vehicle):
    def move(self) -> None:
        print("Driving 🚗")

class Bike(Vehicle):
    def move(self) -> None:
        print("Pedaling 🚴")

class Plane(Vehicle):
    def move(self)-> None:
        print("Flying ✈️")

# Example usage
vehicles = [Car(), Bike(), Plane()]

for vehicle in vehicles:
    vehicle.move()  
