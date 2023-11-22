import os
import json
import time

from pick import pick

from enums.paths import Paths
from users.user import User
from authentication.authentication import Authentication
from pick import pick

BAD_CHANGE_INFO_OPTIONS = {
    'title1': 'Your info cannot be blank (Password must contain more then 5 characters)',
    'title2': 'This Username is already taken.',
    'options': ['Try again', 'Back to Menu']
}


class LoggedUser(User):

    def execute_action(self):
        option = super().execute_action()
        if option == 'Logout':
            self.logout()
        if option == 'Change Info':
            self.change_info()
        return option

    def logout(self):
        self.logged_out = True

    def change_info(self):
        Authentication.change_info(self)
