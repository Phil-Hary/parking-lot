from .admin_strategy import AdminStrategy

def get_user_strategy(user_type):
    if user_type == "admin":
        return AdminStrategy()