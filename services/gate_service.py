from models import Gate

class GateService:
    def create_gate(self, type):
        return Gate(type)