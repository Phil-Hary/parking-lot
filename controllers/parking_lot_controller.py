from services import ParkingLotService
from utils import CommonUtils
from .gate_controller import GateController
from .parking_level_controller import ParkingLevelController
from .parking_spot_controller import ParkingSpotController
from .parking_fee_controller import ParkingFeeController
from enums import GateType

class ParkingLotController:
    parking_lot_service = ParkingLotService()
    gate_controller = GateController()
    parking_level_controller = ParkingLevelController()
    parking_spot_controller = ParkingSpotController()
    parking_fee_controller = ParkingFeeController()

    def add_parking_lot(self):
        if self.parking_lot_service.is_parking_lot_defined():
            print("Parking lot already added")
            return

        print("Please provide the parking lot details")
        parking_lot_details = CommonUtils.get_data_from_user(["name", "address", "location"])
            
        self.parking_lot_service.create_parking_lot(parking_lot_details)
    
    def get_parking_levels(self):
        if not self.parking_lot_service.is_parking_lot_defined():
            print("Parking lot must be defined before adding the levels")
            return
        
        return self.parking_lot_service.get_parking_levels()
    
    def add_parking_level(self):
        if not self.parking_lot_service.is_parking_lot_defined():
            print("Parking lot must be defined before adding the levels")
            return
        
        print("Please provide the parking level details")
        parking_level_details = CommonUtils.get_data_from_user(["name"])

        level_details = CommonUtils.get_data_from_user(["number_of_entry_gates", "number_of_exit_gates"])

        number_of_entry_gates = level_details.get("number_of_entry_gates")
        number_of_exit_gates = level_details.get("number_of_exit_gates")

        gates = []

        for idx in range(int(number_of_entry_gates)):
            gates.append(ParkingLotController.gate_controller.create_gate(GateType.ENTRY))
        
        for idx in range(int(number_of_exit_gates)):
            gates.append(ParkingLotController.gate_controller.create_gate(GateType.EXIT))
        
        
        spot_details = CommonUtils.get_data_from_user(["number_of_bike_spots", "number_of_car_spots", "number_of_truck_spots"])

        parking_level = ParkingLotController.parking_level_controller.create_parking_level(
            parking_level_details.get("name"),
            gates
        )

        ParkingLotController.parking_level_controller.add_spots(parking_level, spot_details)
        ParkingLotController.parking_lot_service.add_parking_levels(parking_level)
    
    def get_parking_level_id_from_user(self):
        parking_level_details = CommonUtils.get_data_from_user(["parking_level_id"])
        return parking_level_details.get("parking_level_id")

    def get_parking_spot_number_from_user(self):
        parking_spot_details = CommonUtils.get_data_from_user(["parking_spot_number"])
        return parking_spot_details.get("parking_spot_number")
    
    def display_parking_level_details(self, parking_level_id):
        parking_level = self.parking_lot_service.get_parking_level(parking_level_id)

        if parking_level == None:
            print("Parking level does not exists")
            return
    
        ParkingLevelController.parking_level_service.display_parking_level(parking_level)
    
    def toggle_parking_spot_status(self, parking_level_id, spot_number):
        parking_level = self.parking_lot_service.get_parking_level(parking_level_id)
        parking_spot = self.parking_lot_service.get_parking_spot(parking_level, spot_number)
        self.parking_spot_controller.toggle_parking_status(parking_spot)
    
    def set_parking_fees(self):
        parking_fee_details = CommonUtils.get_data_from_user(["vehicle_type", "day_type", "first_hour_fee", "second_hour_fee", "third_hour_and_beyond_fee"])
        status, message = self.parking_fee_controller.is_parking_fee_valid(parking_fee_details)

        if not status:
            print(message)

        vehicle_type = parking_fee_details.get("vehicle_type")
        day_type = parking_fee_details.get("day_type")
        
        for category in ["first_hour_fee", "second_hour_fee", "third_hour_and_beyond_fee"]:
            fee = parking_fee_details.get(category)
            self.parking_fee_controller.set_parking_fee(vehicle_type, day_type, category, fee)
    
    def display_parking_fee_details(self):
        parking_fee_details = self.parking_fee_controller.get_all_parking_fees()
        print(parking_fee_details)
        







        
    

        
        