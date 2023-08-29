from utils import CommonUtils
from services import UserService

class UserController:
    user_service = UserService()

    def setup(self):
        self.user_service.create_admin()

    def login(self):
        while True:
            user_credentials = CommonUtils.get_data_from_user(["username", "password"])
            username = user_credentials.get("username")
            password = user_credentials.get("password")

            user = UserController.user_service.get_user_using_credentails(username, password)

            if user:
                return user
            
            print("Invalid username or password")
            


