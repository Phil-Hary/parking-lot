from models import ParkingLevel, ParkingSpot
from enums import SpotType

class ParkingLevelService:
    def create_parking_level(self, name, gates):
        return ParkingLevel(name, gates)

    def add_spots(self, parking_level, spot_details):
        PARKING_SPOT_MAPPING = {
            "number_of_bike_spots": SpotType.BIKE,
            "number_of_car_spots": SpotType.CAR,
            "number_of_truck_spots": SpotType.TRUCK
        }
        
        spots = []

        for spot_type, count in spot_details.items():
            parking_spot = ParkingSpot(
                type=PARKING_SPOT_MAPPING.get(spot_type)
            )

            spots.append(parking_spot)
        
        parking_level.spots = spots
    
    def display_parking_level(self, parking_level):
        parking_spots = parking_level.parking_spots
        idx = 0

        for parking_spot in parking_spots:
            if idx < 10:
                print(parking_spot.spot_number)
            
            if idx == 10:
                print()
                idx = 0




