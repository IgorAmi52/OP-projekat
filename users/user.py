import json
from os import system

from pick import pick

from enums.roles import Roles
from enums.paths import Paths

class User: ### Base class for every role

    def login(self):  #Try to Login the user 
        system('clear')
        user_name = input('Please enter your Username: ')
        password = input('Please enter your Password: ')   

        with open(Paths.USERS.value,'r') as f: 
            try:
                data = json.load(f)
            except:
                data = {}
        if((user_name in data) and data[user_name]['password']==password):
            for key, value in data[user_name].items():
                setattr(self, key, value)
            return self
            
        option, _ = pick(BAD_LOGIN_OPTIONS['options'],BAD_LOGIN_OPTIONS['title'])
        if(option =='Try again'):
            self.login()
        else:
            self.main_menu()
        
    
    def registration(self): ### Static Method  
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
            
    def exit(self):
        exit()
        
    def movie_lookup(self):
        print("pregled filmova")
        
    def search(self):
        print("pretraga filma")
        
    def multi_search(self):
        print("vise krit pretraga")
    
    
BAD_LOGIN_OPTIONS = {
    'title': 'Login was unsuccessful',
    'options': ['Try again','Back to Menu']
}
            
        
        