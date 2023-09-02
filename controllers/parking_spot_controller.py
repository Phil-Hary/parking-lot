from services import ParkingSpotService

class ParkingSpotController:
    parking_spot_service = ParkingSpotService()

    def update_parking_spot_status(self, parking_spot, status):
        self.parking_spot_service.update_parking_spot_status(parking_spot, status)
    
    def toggle_parking_status(self, parking_spot):
        self.parking_spot_service.toggle_parking_status(parking_spot)
