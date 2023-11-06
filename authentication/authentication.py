import json
from os import system

from pick import pick

from enums.roles import Roles
from enums.paths import Paths

class Authentication:
    
    @staticmethod
    def registration(): ### Static Method  
        system('clear')
        name = input("Name: ")
        sirname = input("Sirname: ")
        user_name = input("Username: ")
        password = input("Password: ")
        
        with open(Paths.USERS.value,'r') as f:
            try:
                data = json.load(f)
            except:
                data = {}
            
        data[user_name] = {
            'name':name,
            'sirname': sirname,
            'password':password,
            'role': Roles.BUYER.value
        }
        with open(Paths.USERS.value,'w') as f:
            json.dump(data, f)
        
    @staticmethod
    def login(user):
        
        system('clear')
        user_name = input('Please enter your Username: ')
        password = input('Please enter your Password: ')   
        data = {}
        with open(Paths.USERS.value,'r') as f: 
            try:
                data = json.load(f)
            except:
               
                print("getting users was uncussesful")
                exit()
                
        if((user_name in data) and data[user_name]['password']==password):
            for key, value in data[user_name].items():
                setattr(user, key, value)
            return
        
        option, _ = pick(BAD_LOGIN_OPTIONS['options'],BAD_LOGIN_OPTIONS['title'])
        if(option =='Try again'):
            user.login()
        else:
            user.user_menu()
            
                
BAD_LOGIN_OPTIONS = {
    'title': 'Login was unsuccessful',
    'options': ['Try again','Back to Menu']
}
            
        
        