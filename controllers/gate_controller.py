from services import GateService

class GateController:
    gate_service = GateService()

    def create_gate(self, type):
        return GateController.gate_service.create_gate(type)
