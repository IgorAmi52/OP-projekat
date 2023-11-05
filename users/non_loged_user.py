import json
from os import system

from pick import pick

from users.enums.roles import Roles
from users.user import User
from users.enums.paths import Paths

class Non_Loged_User(User):
    
    def __init__(self):  
        super().__init__()
        self.main_menu()
    
    def main_menu(self):
        option = super().main_menu(MENU_OPTIONS=MENU_OPTIONS)
        if option == 'Registration': 
            self.registration()
    
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
            'password':password
        }
        with open(Paths.USERS,'w') as f:
            json.dump(data, f)
            
      #  self.main_menu()

MENU_OPTIONS = {
        'title' : 'Main Menu: ',
        'options' : ['Exit','Movie Lookup', 'Search Movies', 'Multi Criteria Search','Login','Registration']
    }
