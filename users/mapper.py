from users.logged_user import LoggedUser


class UserMapper:
    """
        Returns a user class depending on the role picked
    """
    def __init__(self):
        self.user_map = {}
        for user_class in LoggedUser.__subclasses__():
            self.user_map[user_class.role] = user_class

    def get(self, role):
        return self.user_map[role]
