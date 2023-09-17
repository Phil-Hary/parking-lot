from .admin_strategy import AdminStrategy

def get_user_strategy(user):
    if user.type == "admin":
        return AdminStrategy(user)