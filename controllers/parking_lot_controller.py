from services import ParkingLotService
from utils import CommonUtils
from .gate_controller import GateController
from .parking_level_controller import ParkingLevelController
from enums import GateType

class ParkingLotController:
    parking_lot_service = ParkingLotService()
    gate_controller = GateController()
    parking_level_controller = ParkingLevelController()

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

        level_details = CommonUtils.get_data_from_user(["number_of_entry_gates", "number_of_exit_gates", "number_of_spots"])

        number_of_entry_gates = level_details.get("number_of_entry_gates")
        number_of_exit_gates = level_details.get("number_of_exit_gates")
        number_of_spots = level_details.get("number_of_spots")

        gates = []

        for idx in range(int(number_of_entry_gates)):
            gates.append(ParkingLotController.gate_controller.create_gate(GateType.ENTRY))
        
        for idx in range(int(number_of_exit_gates)):
            gates.append(ParkingLotController.gate_controller.create_gate(GateType.EXIT))
        
        parking_level = ParkingLotController.parking_level_controller.create_parking_level(
            parking_level_details.get("name"),
            gates,
            number_of_spots
        )

        ParkingLotController.parking_lot_service.add_parking_levels(parking_level)
        





        
    

        
        