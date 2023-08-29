class ParkingLot:
    parking_lot = None

    def __init__(self, name, address, location):
        self.name = name
        self.address = address
        self.location = location
        self.parking_levels = []
    
    def add_parking_levels(self, parking_level):
        self.parking_levels.append(parking_level)

    def get_parking_levels(self):
        return self.parking_levels
    
