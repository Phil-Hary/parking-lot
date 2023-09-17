from services import ParkingLotService
from utils import CommonUtils
from .gate_controller import GateController
from .parking_level_controller import ParkingLevelController
from .parking_spot_controller import ParkingSpotController
from .parking_fee_controller import ParkingFeeController
from .parking_attendant_controller import ParkingAttendantController
from .ticket_controller import TicketController
from .vehicle_controller import VehicleController
from enums import GateType, VehicleType, SpotStatus

class ParkingLotController:
    parking_lot_service = ParkingLotService()
    gate_controller = GateController()
    parking_level_controller = ParkingLevelController()
    parking_spot_controller = ParkingSpotController()
    parking_fee_controller = ParkingFeeController()
    parking_attendant_controller = ParkingAttendantController()
    ticket_controller = TicketController()
    vehicle_controller = VehicleController()

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

        gates = {}

        for idx in range(int(number_of_entry_gates)):
            parking_gate = self.gate_controller.create_gate(GateType.ENTRY)
            gates[parking_gate.gate_number] = parking_gate
        
        for idx in range(int(number_of_exit_gates)):
            parking_gate = self.gate_controller.create_gate(GateType.EXIT)
            gates[parking_gate.gate_number] = parking_gate
        
        
        spot_details = CommonUtils.get_data_from_user(["number_of_bike_spots", "number_of_car_spots", "number_of_truck_spots"])

        parking_level = self.parking_level_controller.create_parking_level(
            parking_level_details.get("name"),
            gates
        )

        self.parking_level_controller.add_spots(parking_level, spot_details)
        self.parking_lot_service.add_parking_levels(parking_level)
    
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
    
    def add_parking_attendant(self):
        if not self.parking_lot_service.is_parking_lot_defined():
            print("Provide parking lot details before proceeding")
            return 
        
        print("Enter parking attendant details")
        parking_attendant_details = CommonUtils.get_data_from_user(["attendant_name"])

        name = parking_attendant_details.get("attendant_name", None)

        if not name:
            print("Invalid name")
            return
        
        parking_attendant = self.parking_attendant_controller.create_parking_attendant(name)
        self.parking_lot_service.add_parking_attendant(parking_attendant)
        print(f"Parking attendant {parking_attendant.name} is added successully")
    
    def display_parking_attendants(self):
        parking_attendants =  self.parking_lot_service.get_parking_attendants()

        for attendant in parking_attendants.values():
            print(attendant.get("details").name, end="  ")
            gate = attendant.get("gate", None)

            if gate:
                gate = gate.gate_number
            print(gate)
    
    def assign_parking_attendant_to_gate(self):
        duty_details = CommonUtils.get_data_from_user(["parking_level_id", "gate_id", "attendant_id"])
        parking_level_id = duty_details.get("parking_level_id")
        gate_id = int(duty_details.get("gate_id"))
        attendant_id = int(duty_details.get("attendant_id"))

        parking_level = self.parking_lot_service.get_parking_level(parking_level_id)
        if not parking_level:
            print("Invalid parking level id")
            return

        gate = self.parking_level_controller.get_gate(parking_level, gate_id)
        if not gate:
            print("Invalid gate id")
            return

        attendant = self.gate_controller.get_gate_attendant(gate)
        if attendant:
            print("An attendant is already assigned to this gate")
            return

        attendant = self.parking_lot_service.get_parking_attendant(attendant_id)
        if not attendant:
            print("Invalid attendant id")
            return
    
        self.parking_lot_service.assign_gate_to_parking_attendant(attendant.id, gate)
        self.gate_controller.assign_parking_attendant_to_gate(attendant, gate)
    
    def book_ticket(self, user):
        print("Vehicle types available")
        print([e.name for e in VehicleType])

        print("Enter vehicle details")
        registration_details = CommonUtils.get_data_from_user(["registration_number", "type"])

        registration_number = registration_details.get("registration_number", None)
        if not registration_number:
            print("Invalid registration number")
            return
        
        type = registration_details.get("type", None)
        if not type or type not in [e.name for e in VehicleType]:
            print("Invalid vehicle type")
            return

        vehicle = self.vehicle_controller.create_vehicle(registration_number, type)

        print("Enter spot details")
        spot_details = CommonUtils.get_data_from_user(["parking_level_id, spot_number"])

        parking_level_id = spot_details.get("parking_level_id")
        parking_level = self.parking_lot_service.get_parking_level(parking_level_id)
        if not parking_level:
            print("Invalid parking level id")
            return
        
        spot_number = spot_details.get("spot_number", None)
        spot = self.parking_level_controller.get_paking_spot(parking_level, spot_number)
        if not spot:
            print("Invalid spot number")
            return

        if spot.status != SpotStatus.AVAILABLE:
            print("This spot in not available")
            return
        
        self.ticket_controller.book_ticket(vehicle, spot, user)
        print("Spot booked successfully")

        







        
    
        






        

        







        
    

        
        