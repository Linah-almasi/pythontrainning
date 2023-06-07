class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

class CarShop:
    def __init__(self):
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)

    def display_inventory(self):
        if len(self.inventory) == 0:
            print("No cars in inventory.")
        else:
            print("Car Inventory:")
            for car in self.inventory:
                print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}, Price: ${car.price}")

    def sell_car(self, make, model):
        for car in self.inventory:
            if car.make == make and car.model == model:
                self.inventory.remove(car)
                print(f"Sold {car.make} {car.model} successfully.")
                return
        print(f"Car {make} {model} not found in inventory.")

# Create a car shop
shop = CarShop()

# Add cars to inventory
car1 = Car("Toyota", "Camry", 2021, 25000)
car2 = Car("Honda", "Civic", 2022, 22000)
car3 = Car("Ford", "Mustang", 2020, 40000)

shop.add_car(car1)
shop.add_car(car2)
shop.add_car(car3)

# Display the inventory
shop.display_inventory()

# Sell a car
shop.sell_car("Toyota", "Camry")

# Display the updated inventory
shop.display_inventory()
