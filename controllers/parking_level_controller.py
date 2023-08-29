from services import ParkingLevelService

class ParkingLevelController:
    parking_level_service = ParkingLevelService()

    def create_parking_level(self, name, gates):
        return ParkingLevelController.parking_level_service.create_parking_level(name, gates)