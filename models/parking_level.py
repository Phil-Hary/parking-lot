class ParkingLevel:
    name = None
    parking_spots = {}
    gates = {}

    def __init__(self, name, gates):
        self.name = name
        self.gates = gates
    
    def add_parking_spots(self, parking_spots):
        self.parking_spots.append(parking_spots)
    
