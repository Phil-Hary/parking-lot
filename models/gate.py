from enums import GateType
from exceptions import *

class Gate:
    gate_id = 0

    def __init__(self, type):
        self.gate_number = Gate.gate_id
        self.type = type
        self.parking_attendant = None
    
    def create_gate(self, type, parking_attendant):
        if type not in [el.name for el in GateType]:
            raise InvalidGateTypeException()

        self.__init__(type, parking_attendant)
