from controllers import ParkingLotController, UserController
from strategies.user import get_user_strategy

class ParkingLotApp:
    def __init__(self):
        self.user_controller = UserController()
    
    def setup(self):
        self.user_controller.setup()

    def run(self):
        print("Parking Lot Application")
        user = self.user_controller.login()

        user_strategy = get_user_strategy(user.type)
        user_strategy.dashboard()

if __name__ == "__main__":
    parking_lot_app = ParkingLotApp()
    parking_lot_app.setup()
    parking_lot_app.run()

