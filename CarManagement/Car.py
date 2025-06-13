class car:
    def __init__(self, price, milage, model, makeyear, bodytype, transmission):
        self.price = price
        self.milage = milage
        self.model = model
        self.makeyear = makeyear
        self.bodytype = bodytype
        self.transmission = transmission

    def get_age(self):
        return self.makeyear
    
    def resale_value(self, depricatedValue):
        return self.price * (1 - depricatedValue)
    
    def __str__(self):
        return f"Car Model: {self.model} -  Car Make Year: {self.makeyear} - Price: {self.price} "

class ElectricCar(car):
    def __init__(self, price, milage, model, makeyear, bodytype, transmission, Autopilot, Supercharging, Battery, Warranty):
        super().__init__(price, milage, model, makeyear, bodytype, transmission)
        self.Autopilot = Autopilot
        self.Supercharging = Supercharging
        self.Battery = Battery
        self.Warranty = Warranty

    def battery_health(self):
        return self.Battery * 0.4
    
    def charging_time(self):
        return ( self.Battery * 60 )/ 10

    def resale_value(self, depricatedValue, batteryLife):
        return self.price * (1 - depricatedValue)

    def get_age(self):
        return self.makeyear / self.Battery


class SportsCar(car):
    def __init__(self, price, milage, model, makeyear, bodytype, transmission, Horsepower, Torque, CoolingSystem, CO2Emissions, FuelCapacity, BrakeType):
        super().__init__(price, milage, model, makeyear, bodytype, transmission)
        self.Horsepower = Horsepower
        self.Torque = Torque
        self.CoolingSystem = CoolingSystem
        self.CO2Emissions = CO2Emissions
        self.FuelCapacity = FuelCapacity
        self.BrakeType = BrakeType

    def performance_summary(self):
        return self.Torque / self.Horsepower

    def get_age(self):
        return self.makeyear / self.Torque

if __name__ == "__main__":
    # 🚗 Basic Cars
    car1 = car(900000, 18, "Maruti Swift", 2019, "Hatchback", "Manual")
    car2 = car(1200000, 22, "Hyundai i20", 2020, "Hatchback", "Automatic")

    # ⚡ Electric Cars
    ec1 = ElectricCar(4000000, 0, "Tesla Model 3", 2022, "Sedan", "Automatic", True, True, 75, 8)
    ec2 = ElectricCar(3500000, 0, "Nexon EV", 2021, "SUV", "Automatic", False, False, 40, 5)

    # 🏎️ Sports Cars
    sc1 = SportsCar(15000000, 8, "Porsche 911", 2018, "Coupe", "Manual", 450, 530, "Liquid", 220, 64, "Ceramic")
    sc2 = SportsCar(18000000, 6, "Lamborghini Huracan", 2020, "Coupe", "Automatic", 640, 600, "Liquid", 320, 85, "Carbon Ceramic")

    # 📊 Displaying Results
    print(car1)
    print(f"Age: {car1.get_age()}, Resale: ₹{car1.resale_value(0.25)}\n")

    print(ec1)
    print(f"Battery Health: {ec1.battery_health()}%, Charging Time: {ec1.charging_time()} mins, Age: {ec1.get_age()}\n")

    print(sc1)
    print(f"Performance Ratio: {sc1.performance_summary():.2f}, Age Factor: {sc1.get_age():.2f}\n")