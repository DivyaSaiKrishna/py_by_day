class spottype(enum):
    SMALL   = 1
    COMPACT = 2
    LARGE   = 3
    
class ParkingSpot:
    def __init__(self, type, price, spotnum, vehicle):
        self.type = type
        self.price = price
        self.spotnum = spotnum
        self.vehicle = vehicle

    
    def can_fit(self, vehicle ) -> bool :
        return self.type == vehicle.size

    def is_free(self):
        return self.vehicle is None

    def park(self, vehicle) -> bool :
        if self.is_free() and self.can_fit(vehicle):
            self.vehicle = vehicle
            return true
        return false

    def make_free(self):
        self.vehicle = None
