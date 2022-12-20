class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year


class Truck(Car):
	pass


car1  = Car("Chevy", "Blazer", 2021)

truck1 = Truck("Chevy", "Colorado", 2021)

truck2 = Truck("Ford", "Ranger", 2009)

print(car1.make, " " , car1.model, " " , car1.year)

print(truck1.make, " ", truck1.model, " ", truck1.year)

print(truck2.make, " ", truck2.model, " ", truck2.year)