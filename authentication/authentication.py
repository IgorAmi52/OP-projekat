import os
import json
import time

from pick import pick

from enums.paths import Paths
from enums.roles import Roles
from users.mapper import UserMapper


class Authentication:

    @classmethod
    def registration(cls, user):
        """used for registration of new users, depending on what role they are(Anonymous becomes Buyer, Manager can select role for new users)

        Args:
            user (Anonymous/Manager): user
        """
        options = Authentication.get_options()

        os.system('clear')
        name = input("Name: ")
        surname = input("Surname: ")
        username = input("Username: ")
        password = input("Password: ")
        role = Roles.BUYER.value

        if user.role == 'Manager':
            role, _ = pick(options['REGISTER_MANAGER_ROLES']['options'],
                           options['REGISTER_MANAGER_ROLES']['title'])

        # Validation 1 -- incorrect input
        if username == '' or name == '' or surname == '' or len(password) < 6 or not any(char.isdigit() for char in password):
            option, _ = pick(options['BAD_REGISTER_OPTIONS']['options'],
                             options['BAD_REGISTER_OPTIONS']['title2'])
            if option == 'Try again':
                user.registration()
            return

        with open(Paths.USERS.value, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print('Registration users load not working propertly')
                exit()

        # validation 2 --- username already exists in database
        if username in data:
            option, _ = pick(options['BAD_REGISTER_OPTIONS']['options'],
                             options['BAD_REGISTER_OPTIONS']['title1'])
            if option == 'Try again':
                user.registration()
            else:
                return
        else:
            data[username] = {
                'name': name,
                'surname': surname,
                'password': password,
                'role': role
            }
            with open(Paths.USERS.value, 'w') as f:
                json.dump(data, f, indent=4)

    @classmethod
    def login(cls, user):
        os.system('clear')
        username = input('Please enter your Username: ')
        password = input('Please enter your Password: ')

        with open(Paths.USERS.value, 'r') as f:
            try:
                data = json.load(f)
            except:
                print("getting users was uncussesful")
                exit()
        # validation
        if username in data and data[username]['password'] == password:
            user_class = UserMapper().get(data[username]['role'])
            new_user = user_class(name=data[username]['name'],
                                  surname=data[username]['surname'],
                                  password=data[username]['password'],
                                  username=username)
            user.logged_in = new_user
            print('You successfully loged in!')
            time.sleep(2)
            os.system('clear')
            return
        options = Authentication.get_options()
        option, _ = pick(options['BAD_LOGIN_OPTIONS']
                         ['options'], options['BAD_LOGIN_OPTIONS']['title'])
        if option == 'Try again':
            user.login()

    @classmethod
    def change_info(cls, user):

        os.system('clear')
        options = Authentication.get_options()

        name = input('Current Name is ' + user.name + '. New Name: ')
        surname = input('Current Sirname is ' +
                        user.surname + '. New Sirname: ')
        username = input('Current Username is ' +
                         user.username + '. New Username: ')
        password = input('Current Password is ' +
                         user.password + '. New Password: ')

        # Validation 1 -- incorrect input
        if username == '' or password == '' or name == '' or surname == '' or len(password) < 6 or not any(char.isdigit() for char in password):
            option, _ = pick(
                options['BAD_REGISTER_OPTIONS']['options'], options['BAD_REGISTER_OPTIONS']['title1'])
            if option == 'Back to Menu':
                user.execute_action()
            else:
                user.change_info()

        with open(Paths.USERS.value, 'r') as f:
            try:
                data = json.load(f)
            except:
                print("getting users was uncussesful")
                exit()
        # validation 2 --- username already exists in database
        if username in data and user.username != username:
            option, _ = pick(
                options['BAD_REGISTER_OPTIONS']['options'], options['BAD_REGISTER_OPTIONS']['title2'])
            if option == 'Back to Menu':
                user.execute_action()
            else:
                user.change_info()
        else:
            data.pop(user.username)
            data[username] = {
                'name': name,
                'surname': surname,
                'password': password,
                'role': user.role
            }
            for key in data[username].keys():
                user.key = data[username][key]
            user.username = username
            with open(Paths.USERS.value, 'w') as f:
                json.dump(data, f, indent=4)

            os.system('clear')
            print('You successfully changed your information!')
            time.sleep(2)
            os.system('clear')
            user.execute_action()

    @classmethod
    def get_options(cls):
        with open(Paths.AUTH_OPTIONS.value, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print('Authentication options not working propertly')
                exit()
