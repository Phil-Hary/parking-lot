from models import ParkingSpot
from enums import SpotStatus

class ParkingSpotService:
    def update_parking_spot_status(self, parking_spot, status):
        parking_spot.status = status
    
    def toggle_parking_status(self, parking_spot):
        if parking_spot.status == SpotStatus.AVAILABLE:
            self.update_parking_spot_status(parking_spot, SpotStatus.BLOCKED)
        else:
            self.toggle_parking_status(parking_spot, SpotStatus.AVAILABLE)