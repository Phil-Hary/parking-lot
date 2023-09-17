from .user_strategy import UserStrategy
from controllers import ParkingLotController

class AdminStrategy(UserStrategy):
    parking_lot_controller = ParkingLotController()

    def __init__(self, user):
        self.user = user
    
    def display_menu(self):
        admin_operations = [
            "Add parking lot",
            "Add parking level",
            "Display parking levels",
            "Display parking level details",
            "Toggle parking spot status",
            "Set parking lot fee",
            "Display parking lot fees",
            "Add parking attendant",
            "View parking attendants",
            "Assign parking attendant",
            "Generate Ticket",
            "Generate Invoice"
        ]
        
        for idx, operation in enumerate(admin_operations):
            print(f"{idx + 1}. {operation}")
        
        print("0. Exit")
    
    def execute_choice(self, choice):
        
        if choice == "1":
            AdminStrategy.parking_lot_controller.add_parking_lot()
            print("Parking lot added successfully")
        
        elif choice == "2":
            AdminStrategy.parking_lot_controller.add_parking_level()
        
        elif choice == "3":
            parking_levels = AdminStrategy.parking_lot_controller.get_parking_levels()

            if not parking_levels:
                return
            
            if len(parking_levels):                
                for parking_level in parking_levels:
                    print(parking_level.name)
            else:
                print("No parking levels")       
            
        elif choice == "4":
            parking_levels = AdminStrategy.parking_lot_controller.get_parking_levels()

            if not parking_levels:
                print("No parking levels")

            parking_level_id = self.parking_lot_controller.get_parking_level_id_from_user()
            self.parking_lot_controller.display_parking_level_details(parking_level_id)
        
        elif choice == "5":
            parking_levels = AdminStrategy.parking_lot_controller.get_parking_levels()

            if not parking_levels:
                print("No parking levels")

            parking_level_id = self.parking_lot_controller.get_parking_level_id_from_user()
            parking_spot_number = self.parking_lot_controller.get_parking_spot_number_from_user()
            self.parking_lot_controller.toggle_parking_spot_status(parking_level_id, parking_spot_number)
        
        elif choice == "6":
            self.parking_lot_controller.set_parking_fees()
        
        elif choice == "7":
            self.parking_lot_controller.display_parking_fee_details()
        
        elif choice == "8":
            self.parking_lot_controller.add_parking_attendant()

        elif choice == "9":
            self.parking_lot_controller.display_parking_attendants()
        
        elif choice == "10":
            self.parking_lot_controller.assign_parking_attendant_to_gate()
        
        elif choice == "11":
            self.parking_lot_controller.book_ticket(self.user)
     
    def dashboard(self):
        choice = None
        while True:
            self.display_menu()
            choice = input()

            if choice == "0":
                break

            self.execute_choice(choice)

        