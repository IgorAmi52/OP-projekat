
from users.user import User

from authentication.authentication import Authentication


class AnonymousUser(User):

    role = 'Anonymous'

    def execute_action(self):
        option = super().execute_action()
        if option == 'Login':
            self.login()
        elif option == 'Registration':
            self.registration()
        return option

    def registration(self):
        Authentication.registration(self)

    def login(self):
        Authentication.login(self)
