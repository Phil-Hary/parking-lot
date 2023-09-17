from services import ParkingAttendantService

class ParkingAttendantController:
    parking_attendant_service = ParkingAttendantService()

    def create_parking_attendant(self, name):
        return self.parking_attendant_service.create_parking_attendant(name)
