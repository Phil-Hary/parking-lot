from models import ParkingLot

class ParkingLotService:
    def create_parking_lot(self, parking_lot_details):
        parking_lot = ParkingLot(
            name = parking_lot_details.get("name"),
            address = parking_lot_details.get("address"),
            location = parking_lot_details.get("location")
        )

        ParkingLot.parking_lot = parking_lot
    
    def is_parking_lot_defined(self):
        return ParkingLot.parking_lot

    def get_parking_lot(self):
        return ParkingLot.parking_lot

    def get_parking_levels(self):
        parking_lot = self.get_parking_lot()
        return parking_lot.parking_levels.values()

    def add_parking_levels(self, parking_level):
        parking_lot = self.get_parking_lot()
        parking_lot.parking_levels[parking_level.name] = parking_level
    
    def get_parking_level(self, parking_level_id):
        parking_lot = self.get_parking_lot()
        return parking_lot.parking_levels.get(parking_level_id, None)

    def get_parking_spot(self, parking_level, spot_number):
        parking_spot = parking_level.parking_spots.get(spot_number, None)
        return parking_spot
        



