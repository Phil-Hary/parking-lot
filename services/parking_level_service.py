from models import ParkingLevel

class ParkingLevelService:
    def create_parking_level(self, name, gates):
        return ParkingLevel(name, gates)

