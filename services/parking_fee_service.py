from models import ParkingFee
from enums import SpotType, SpotStatus, VehicleType
from utils import CommonUtils

class ParkingFeeService:
    def is_parking_fee_valid(self, parking_fee_details):

        vehicle_type = parking_fee_details.get("vehicle_type", None)
        print([e.value for e in VehicleType])
        if vehicle_type == None or vehicle_type not in [e.name for e in VehicleType]:
            return False, "Invalid vehicle type"
        
        day_type = parking_fee_details.get("day_type", None)
        if day_type == None or day_type not in ["WD", "WE"]:
            return False, "Invalid day type"

        first_hour = parking_fee_details.get("first_hour_fee", None)
        if first_hour == None or not first_hour.isnumeric():
            return False, "Invalid first hour fee"
    
        second_hour = parking_fee_details.get("second_hour_fee", None)
        if second_hour == None or not second_hour.isnumeric():
            return False, "Invalid second hour fee"

        third_hour_and_beyond = parking_fee_details.get("third_hour_and_beyond_fee", None)
        if third_hour_and_beyond == None or not third_hour_and_beyond.isnumeric():
            return False, "Invalid third hour and beyond fee"

        return True, "Parking fee details is valid"
    
    def set_parking_fee(self, vehicle_type, day_type, category, fee):
        ParkingFee.set_parking_fee(vehicle_type, day_type, category, fee)
    
    def get_all_parking_fees(self):
        return ParkingFee.parking_fees_map
    


        
    

        