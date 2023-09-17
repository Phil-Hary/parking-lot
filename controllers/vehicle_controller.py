from services import VehicleService

class VehicleController:
    vehicle_service = VehicleService()

    def create_vehicle(self, registration_number, type):
        return self.vehicle_service.create_vehicle(registration_number, type)
