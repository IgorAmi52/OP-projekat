import json
from os import system

from pick import pick

from users.enums.roles import Roles
from users.enums.paths import Paths

class User:
    
    def __init__(self):
        self.name = ''
        self.sir_name = ''
        self.user_name = ''
        self.password = '',
        self.role = Roles.NON_LOGED
        
    def main_menu(self, MENU_OPTIONS):
        option, _ = pick(MENU_OPTIONS['options'], MENU_OPTIONS['title'])
       
        if option == 'Exit': 
            self.exit()
        elif option == 'Movie Lookup': 
            self.movie_lookup()
        elif option == 'Search Movies': 
            self.search()
        elif option == 'Multi Criteria Search': 
            self.multi_search()
        elif option == 'Login': 
            self.login()
        return option

    @property
    def get_role(self):
        return self.role
    
    def login(self):  
        system('clear')
        user_name = input('Please enter your Username: ')
        password = input('Please enter your Password: ')   

        with open(Paths.USERS.value,'r') as f:
            try:
                data = json.load(f)
            except:
                data = {}
        if((user_name in data) and data[user_name]['password']==password):
            for key,value in data[user_name].items():
                print()
            return 
            
        option, _ = pick(BAD_LOGIN_OPTIONS['options'],BAD_LOGIN_OPTIONS['title'])
        if(option =='Try again'):
            self.login()
        else:
            self.main_menu()
            
    
        
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
            
        
        