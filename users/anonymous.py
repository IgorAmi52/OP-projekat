from authentication.authentication import Authentication

from enums.roles import Roles
from users.user import User


class AnonymousUser(User):
    def execute_action(self):
        option = super().execute_action()
        if option == 'Login':
            self.login()
        elif option == 'Registration':
            self.registration()
        return option


    def login(self):  #Try to Login the user
        self.new_active_user = Authentication.login(self)

    def registration(self):
        Authentication.registration()
