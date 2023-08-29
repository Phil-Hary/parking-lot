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
        return parking_lot.parking_levels

    def add_parking_levels(self, parking_level):
        parking_lot = self.get_parking_lot()
        parking_lot.parking_levels.append(parking_level)

        



