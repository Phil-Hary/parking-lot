from services import ParkingFeeService

class ParkingFeeController:
    parking_fee_service = ParkingFeeService()

    def is_parking_fee_valid(self, parking_fee_details):
        return self.parking_fee_service.is_parking_fee_valid(parking_fee_details)

    def set_parking_fee(self, vehicle_type, day_type, category, fee):
        print(vehicle_type, day_type, category, fee)
        return self.parking_fee_service.set_parking_fee(vehicle_type, day_type, category, fee)

    def get_all_parking_fees(self):
        return self.parking_fee_service.get_all_parking_fees()