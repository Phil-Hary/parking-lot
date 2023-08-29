from enums import VehicleType
from exceptions import InvalidVehicleTypeException

class Vehicle:
    def __init__(self, registration_number, type):
        self.registration_number = registration_number
        self.type = type
    
    def create_vehicle(self, registration_number, type):
        if type not in [el.name for el in VehicleType]:
            raise InvalidVehicleTypeException()

        self.__init__(registration_number, type)
