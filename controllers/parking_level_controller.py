from services import ParkingLevelService

class ParkingLevelController:
    parking_level_service = ParkingLevelService()

    def create_parking_level(self, name, gates):
        return ParkingLevelController.parking_level_service.create_parking_level(name, gates)

    def add_spots(self, parking_level, spot_details):
        ParkingLevelController.parking_level_service.add_spots(parking_level, spot_details)
    
    def display_parking_level_details(self, parking_level):
        ParkingLevelController.parking_level_service.display_parking_level(parking_level)
    
