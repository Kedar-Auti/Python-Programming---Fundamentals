


# Importing Individual classes from module
from car import Car, ElectricCar
my_beetle = Car("Volkswagon","beetle",2016)
my_beetle.fill_tank()
my_beetle.drive() 

#importing entire module
import car
my_beetle = car.Car('Volkswagon','beetle',2016)
my_beetle.fill_tank()
my_beetle.drive()

##################################################################################

# Storing objects in a list
	# List can hold large number of objects from a class.
from car import Car, ElectricCar

# Make lists to hold a fleet of cars.
gas_fleet = []
electric_fleet = []

# Make 500 gas_cars and 250 electric_cars. 
for a in range(500):
	car = Car('ford','focus',2016)
	gas_fleet.append(car)
for b in range(250):
	ecar = ElectricCar('nissan','Leaf',2016)
	electric_fleet.append(ecar)

# Fill the gas_cars & Charge the electric cars
for car in gas_fleet:
	car.fill_tank()
for ecar in electric_fleet:
	ecar.charge()

print("gas_cars:",len(gas_fleet))
print("electric_cars:",len(electric_fleet))

# It is seen that this trick is used many time in Software Devlopement programing as well as in Data-Science projects

