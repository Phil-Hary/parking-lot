from exceptions import InvalidCredentials

class User:
    user_id = 0
    users = {}

    def __init__(self, username, password, type):
        User.user_id += 1
        self.user_id = User.user_id
        self.username = username
        self.password = password
        self.type = type

    staticmethod
    def create_user(username, password, type="parking-assistant"):
        user = User(username, password, type)
        User.users[user.username] = user
        print(user)
        return user

    staticmethod
    def create_admin():
        User.create_user("admin", "1234", "admin")



        