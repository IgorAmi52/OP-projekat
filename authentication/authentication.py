import os
import json
import time

from pick import pick

from enums.paths import Paths
from enums.roles import Roles
from users.mapper import UserMapper
class Authentication:

    @classmethod
    def registration(cls,user):
        
        """used for registration of new users, depending on what role they are

        Args:
            user (Anonymous/Manager): user
        """
        options = Authentication.get_options()
        os.system('clear')
        name = input("Name: ")
        surname = input("Surname: ")
        username = input("Username: ")
        password = input("Password: ")
        
        #Validation 1 -- incorrect input
        if username == '' or password == '' or name == '' or surname == '':
            option, _ = pick(options['BAD_REGISTER_OPTIONS']['options'],options['BAD_REGISTER_OPTIONS']['title2']) 
            if option == 'Back to Menu': user.execute_action()
            else: user.registration()

        with open(Paths.USERS.value,'r') as f:
            try:
                data = json.load(f)
            except:
                data = {}
                
        #validation 2 --- username already exists in database
        if username in data:     
            option, _ = pick(options['BAD_REGISTER_OPTIONS']['options'],options['BAD_REGISTER_OPTIONS']['title1'])
            if option =='Back to Menu': user.execute_action()
            else: user.registration()
        else:
            data[username] = {
                'name':name,
                'surname': surname,
                'password':password,
                'role': Roles.BUYER.value
            }
            with open(Paths.USERS.value,'w') as f:
                json.dump(data, f, indent=4)
                
    @classmethod
    def login(cls,user):
        os.system('clear')
        username = input('Please enter your Username: ')
        password = input('Please enter your Password: ')
        
        with open(Paths.USERS.value,'r') as f:
            try:
                data = json.load(f)
            except:
                print("getting users was uncussesful")
                exit()
        #validation
        if username in data and data[username]['password'] == password:
            user_class = UserMapper().get(data[username]['role'])
            new_user = user_class(name = data[username]['name'],
                                    surname = data[username]['surname'],
                                    password = data[username]['password'],
                                    username=username)
            user.logged_in = new_user
            print('You successfully loged in!')
            time.sleep(2)
            os.system('clear')
            return
        options = Authentication.get_options()
        option, _ = pick(options['BAD_LOGIN_OPTIONS']['options'],options['BAD_LOGIN_OPTIONS']['title'])
        if option == 'Try again':
            user.login()

    @staticmethod
    def get_options():
        with open(Paths.AUTH_OPTIONS.value,'r') as f:
            try:
                return json.load(f)
            except:
                print('Authentication options not working propertly')
                return {}

    
