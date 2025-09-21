# Smartphone OOP Assignment 📱

**Student:** [Your Name]  
**Course:** Object-Oriented Programming  
**Assignment:** Class Design & Polymorphism

## Overview

Python implementation demonstrating core OOP concepts using smartphone classes. Features inheritance, polymorphism, and encapsulation through a realistic smartphone hierarchy.

## Class Structure

### Base Class: `Smartphone`

```python
class Smartphone:
    # Attributes: brand, model, storage_gb, battery_capacity_mAh, is_on
    # Methods: __init__, power(), phone_info()
```

### Inherited Class: `GamingPhone`

```python
class GamingPhone(Smartphone):
    # Additional attribute: cooling_system
    # Overridden method: phone_info() - demonstrates polymorphism
```

## Key Features Implemented

### ✅ **Inheritance**

- `GamingPhone` inherits from `Smartphone`
- Uses `super().__init__()` to call parent constructor
- Extends base functionality with gaming-specific attributes

### ✅ **Encapsulation**

- Private-like attributes (`self.brand`, `self.model`)
- Methods control access to object state
- Type hints for better code documentation

### ✅ **Polymorphism**

- `phone_info()` method overridden in `GamingPhone`
- Same method call, different behavior
- Demonstrated in Activity 2 with `Vehicle.move()`

### ✅ **Constructor Usage**

- Base class constructor with required parameters
- Child class calls parent constructor using `super()`
- Type hints for parameter validation

## Code Examples

### Creating Objects

```python
# Base smartphone
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 4000)

# Gaming smartphone with additional features
gaming_phone = GamingPhone("ASUS", "ROG Phone 7", 512, 6000, "Advanced Liquid Cooling")
```

### Method Calls

```python
print(phone1.phone_info())     # Base class method
print(gaming_phone.phone_info()) # Overridden method - polymorphism!
```

## Activity 2: Polymorphism Challenge 🚗✈️🚴

### Vehicle Hierarchy

- **Base Class:** `Vehicle` with abstract `move()` method
- **Subclasses:** `Car`, `Bike`, `Plane` each implementing `move()` differently

### Polymorphic Behavior

```python
vehicles = [Car(), Bike(), Plane()]
for vehicle in vehicles:
    vehicle.move()  # Same call, different outputs!
```

**Output:**

- Car: "Driving 🚗"
- Bike: "Pedaling 🚴"
- Plane: "Flying ✈️"

## OOP Principles Demonstrated

| Principle         | Implementation                 | Example                            |
| ----------------- | ------------------------------ | ---------------------------------- |
| **Inheritance**   | GamingPhone extends Smartphone | `class GamingPhone(Smartphone):`   |
| **Polymorphism**  | Method overriding              | `phone_info()` behaves differently |
| **Encapsulation** | Data hiding with methods       | Attributes accessed via methods    |
| **Abstraction**   | Simple interfaces              | `power()` toggles state simply     |

## Technical Implementation

### Type Hints Used

```python
def __init__(self, brand: str, model: str, storage_gb: int, battery_capacity_mAh: int)
def power(self) -> None
def phone_info(self) -> str
```

### Method Overriding

```python
# Base class
def phone_info(self) -> str:
    return f"Brand: {self.brand}, Model: {self.model}..."

# Child class - polymorphism
def phone_info(self):
    super().phone_info()  # Call parent method
    return f"Cooling System: {self.cooling_system}"  # Add new info
```

## Running the Code

```bash
python answers.py
```

**Expected Output:**

```
Brand: Samsung, Model: Galaxy S23, Storage: 256GB, Battery: 4000mAh
Samsung Galaxy S23 is now ON
Cooling System: Advanced Liquid Cooling
ASUS ROG Phone 7 is now ON
Driving 🚗
Pedaling 🚴
Flying ✈️
```

## Learning Outcomes

- ✅ Created base and derived classes with proper inheritance
- ✅ Implemented method overriding for polymorphic behavior
- ✅ Used constructors with `super()` calls
- ✅ Applied encapsulation principles
- ✅ Demonstrated runtime polymorphism with vehicle examples
- ✅ Used type hints for professional code quality

## Code Structure

```
smartphone_assignment.py
├── class Smartphone (Base class)
├── class GamingPhone(Smartphone) (Inheritance)
├── class Vehicle (Polymorphism demo)
├── class Car(Vehicle)
├── class Bike(Vehicle)
├── class Plane(Vehicle)
└── Example usage & testing
```
