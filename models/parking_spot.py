from enums import SpotType, SpotStatus
from exceptions import InvalidSpotTypeException

class ParkingSpot():
    spot_id = 0

    def __init__(self, type):
        ParkingSpot.spot_id += 1
        self.spot_number = ParkingSpot.spot_id
        self.type = type
        self.status = SpotStatus.AVAILABLE
        
    def create_parking_spot(self, type):
        if type not in [el.name for el in SpotType]:
            raise InvalidSpotTypeException()

        self.__init__(type)