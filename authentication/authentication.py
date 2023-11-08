import json
from os import system

from pick import pick

from enums.paths import Paths

from users.anonymous import AnonymousUser
from users.buyer import Buyer
from users.seller import Seller
from users.manager import Manager
from enums.roles import Roles


class UserMapper:

    user_map = {
        Roles.BUYER.value: Buyer,
        Roles.NON_LOGED.value: AnonymousUser,
        Roles.SELLER.value: Seller,
        Roles.MANAGER.value: Manager
    }

    @classmethod
    def get(cls, user):
        return cls.user_map[user.role]


class Authentication:
    
    @staticmethod
    def registration(): ### Static Method  
        system('clear')
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
            json.dump(data, f)
        
    @staticmethod
    def login(user):
        system('clear')
        username = input('Please enter your Username: ')
        password = input('Please enter your Password: ')
        with open(Paths.USERS.value,'r') as f: 
            try:
                data = json.load(f)
            except:
                print("getting users was uncussesful")
                exit()
                
        if username in data and data[username]['password'] == password:
            user_class = UserMapper.get(data[username]['role'])
            new_user = user_class(**data[username], username=username)
            return new_user
        
        option, _ = pick(BAD_LOGIN_OPTIONS['options'],BAD_LOGIN_OPTIONS['title'])
        if option == 'Try again':
            Authentication.login(user)
        else:
            return user
            
                
BAD_LOGIN_OPTIONS = {
    'title': 'Login was unsuccessful',
    'options': ['Try again', 'Back to Menu']
}
            
        
