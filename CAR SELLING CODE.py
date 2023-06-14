class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"
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
                print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}")

    def sell_car(self, make, model):
        for car in self.inventory:
            if car.make == make and car.model == model:
                self.inventory.remove(car)
                print(f"Sold {car.make} {car.model} successfully.")
                return
        print(f"Car {make} {model} not found in inventory.")
 
shop = CarShop()  
     
# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)
car1 = Car("Toyota", "Camry", 2021)
car2 = Car("Honda", "Civic", 2022)
car3 = Car("Ford", "Mustang", 2020)

shop.add_car(my_car)
shop.add_car(car1)
shop.add_car(car2)
shop.add_car(car3)

# Calling the get_info method
print(my_car.get_info()) 
print(car1.get_info())
print(car2.get_info())
print(car3.get_info())

# Display the inventory
shop.display_inventory()

# Sell a car
shop.sell_car("Toyota", "Camry")

# Display the updated inventory
shop.display_inventory()