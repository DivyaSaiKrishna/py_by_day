class VehicleSize(Enum):
    MOTORCYCLE = 1
    COMPACT    = 2
    LARGE      = 3

class Vehicle:
    def __init__(self, license_no, entery_gate_no, entery_time, size):
        self.license_no = license_no
        self.entery_gate_no = entery_gate_no
        self.entery_time = entery_time
        self.size = size

class car(Vehicle):
    def __init__(self,license_no, entery_gate_no, entery_time, size):
        super().__init__(license_no, entery_gate_no, entery_time)
        self.size = 

class truck(Vehicle):
    def __init(self,license_no, entery_gate_no, entery_time):
        super().__init__(license_no, entery_gate_no, entery_time)

class bike(Vehicle):
    def __init(self,license_no, entery_gate_no, entery_time):
        super().__init__(license_no, entery_gate_no, entery_time)

class van(Vehicle):
    def __init(self,license_no, entery_gate_no, entery_time):
        super().__init__(license_no, entery_gate_no, entery_time)





    