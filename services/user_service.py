from models import User

class UserService:
    def get_user_using_credentails(self, username, password):
        user = User.users.get(username, None)

        if user:
            if user.password == password:
                return user
        
        return None

    def create_admin(self):
        User.create_admin()