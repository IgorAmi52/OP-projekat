from users.logged_user import LoggedUser
from authentication.authentication import Authentication


class Manager(LoggedUser):
    role = 'Manager'

    def execute_action(self):
        option = super().execute_action()
        if option == "Register New Employee":
            self.registration()

    def registration(self):
        Authentication.registration(self)
