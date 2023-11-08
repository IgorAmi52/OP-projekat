import os
import json
from pick import pick
from enums.paths import Paths
from enums.roles import Roles

from users.user import User
from users.mapper import UserMapper

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

    @staticmethod
    def registration():
        os.system('clear')
        name = input("Name: ")
        surname = input("Surname: ")
        username = input("Username: ")
        password = input("Password: ")

        with open(Paths.USERS.value,'r') as f:
            try:
                data = json.load(f)
            except:
                data = {}

        data[username] = {
            'name':name,
            'surname': surname,
            'password':password,
            'role': Roles.BUYER.value
        }
        with open(Paths.USERS.value,'w') as f:
            json.dump(data, f, indent=4)

    def login(self):
        os.system('clear')
        username = input('Please enter your Username: ')
        password = input('Please enter your Password: ')
        with open(Paths.USERS.value,'r') as f:
            try:
                data = json.load(f)
            except:
                print("getting users was uncussesful")
                exit()

        if username in data and data[username]['password'] == password:
            user_class = UserMapper().get(data[username]['role'])
            new_user = user_class(**data[username], username=username)
            self.logged_in = new_user
            return

        option, _ = pick(BAD_LOGIN_OPTIONS['options'],BAD_LOGIN_OPTIONS['title'])
        if option == 'Try again':
            self.login()


