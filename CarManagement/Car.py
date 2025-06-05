class car:
    def __init__(self, price, milage, model, makeyear, bodytype, transmission):
        self.price = price
        self.milage = milage
        self.model = model
        self.makeyear = makeyear
        self.bodytype = bodytype
        self.transmission = transmission
    
    def __str__(self):
        return f"Car Model: {self.model} -  Car Make Year: {self.makeyear} - Price: {self.price} "

class ElectricCar(car):
     def __init__(self, price, milage, model, makeyear, bodytype, transmission, Autopilot, Supercharging, Battery, Warranty):
        super().__init__(price, milage, model, makeyear, bodytype, transmission)
        self.Autopilot = Autopilot
        self.Supercharging = Supercharging
        self.Battery = Battery
        self.Warranty = Warranty

class SportsCar(car):
    def __init__(self, price, milage, model, makeyear, bodytype, transmission, Horsepower, Torque, CoolingSystem, CO2Emissions, FuelCapacity, BrakeType):
        super().__init__(price, milage, model, makeyear, bodytype, transmission)
        self.Horsepower = Horsepower
        self.Torque = Torque
        self.CoolingSystem = CoolingSystem
        self.CO2Emissions = CO2Emissions
        self.FuelCapacity = FuelCapacity
        self.BrakeType = BrakeType

