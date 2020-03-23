class Car(): 
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
        self.fuel_capacity=15
        self.fuel_level=0
        
    def fill_tank(self): #This is called as methods
        self.fuel_level=self.fuel_capacity
        print("Fuel tank is full")
    
    def drive(self):print("The Car is moving")


def update_fuel_level(self,new_level):
    if new_level <= self.fuel_capacity:
        self.fuel_level = new_level     
    #if I want to access attributr with are not from parenthesis i need to write self.attribute_name
    else:
        print("The tank can't hold that much!")

def add_fuel(self,amount):
    if self.fuel_level + amount <= self.fuel_capacity:
        self.fuel_level += amount
        print("Added Fuel")
    else:
        print("It can't hold that much")

class ElectricCar(Car):
    #parenthesis madhe parent class ch nav lihych ast
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        # Exibit that 3-4 no. of code lines
        #__init__() of the superclass ( Square ) will be called automatically.
        #super() returns a delegate object to a parent class
        
        #Now we add attributes specific to ElectricCar
        #Battery capacity in KWH
        self.battery_size = 70
        #Charge level in %
        self.chaerge_level = 0

class ElectricCar(Car):
    def charge(self):
        #Fully charge the vehicle
        self.charge_level = 100
        print("The Vehicle is fuuly charged")



class Battery():
    def __init__(self,size=70):
        #we initialized battery attributes
        self.size = size
        self.charge_level = 0
        
    def get_range(self):
        #returns a battery's range
        if self.size ==70:
            return 240
        elif self.size == 85:
            return 70

class ElectricCar(Car):
    def __init__(self,make,model,year):
        #Initialise an electric car
        super().__init__(make,model,year)
        
        # Attribute specific to lectric cars
        self.battery = Battery()
 # Here, battery is actually an instance created,where this instance acquire all attributes of Battery Class
        
    def charge(self):
        #Fully charge the vehicle
        
        self.battery.charge_level = 100
        # Battery class madhla attribute change kela.
        print("Vehicle is fully charged")

