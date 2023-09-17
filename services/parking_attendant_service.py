from models import ParkingAttendant

class ParkingAttendantService:
    def create_parking_attendant(self, name):
        return ParkingAttendant(name)
