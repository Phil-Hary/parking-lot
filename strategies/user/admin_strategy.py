from .user_strategy import UserStrategy
from controllers import ParkingLotController

class AdminStrategy(UserStrategy):
    parking_lot_controller = ParkingLotController()
    
    def display_menu(self):
        admin_operations = [
            "Add parking lot",
            "Add parking level",
            "Display parking levels",
            "Display parking level details",
            "Update parking spot status",
            "Update parking lot fee",
            "Add parking attendant",
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
            
            


     
    def dashboard(self):
        choice = None
        while True:
            self.display_menu()
            choice = input()

            if choice == "0":
                break

            self.execute_choice(choice)

        