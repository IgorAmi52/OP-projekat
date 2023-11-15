import os
import json
import time

from pick import pick

from enums.paths import Paths
from enums.roles import Roles
from users.user import User
from users.mapper import UserMapper
from authentication.authentication import Authentication
BAD_REGISTER_OPTIONS = {
    'title1': 'Username already exists, use a diffrent username',
    'title2': 'Your info cannot be blank',
    'options': ['Try again', 'Back to Menu']
}
BAD_LOGIN_OPTIONS = {
    'title': 'Login was unsuccessful',
    'options': ['Try again', 'Back to Menu']
}


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
        


