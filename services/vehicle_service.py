from models import Vehicle

class VehicleService:
    def create_vehicle(self, registration_number, type):
        return Vehicle(registration_number, type)

        
