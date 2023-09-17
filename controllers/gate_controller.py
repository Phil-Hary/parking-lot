from services import GateService

class GateController:
    gate_service = GateService()

    def create_gate(self, type):
        return GateController.gate_service.create_gate(type)
    
    def get_gate_attendant(self, gate):
        return self.gate_service.get_gate_attendant(gate)

    def assign_parking_attendant_to_gate(self, parking_attendant, gate):
        return self.gate_service.assign_parking_attendant_to_gate(parking_attendant, gate)
