from models import Gate

class GateService:
    def create_gate(self, type):
        return Gate(type)

    def get_gate_attendant(self, gate):
        return gate.parking_attendant
    
    def assign_parking_attendant_to_gate(self, parking_attendant, gate):
        gate.parking_attendant = parking_attendant
            
