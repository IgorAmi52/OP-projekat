import json
from os import system

from pick import pick

from enums.paths import Paths
from enums.roles import Roles

class UserMenu:
    
    
    @classmethod
    def get_user_menu(cls, user, role):
        
        OPTIONS = cls.get_options(cls)
        
        option, _ = pick(OPTIONS[role]['options'], OPTIONS[role]['title'])
       
        if option == 'Exit': 
            user.exit()
        elif option == 'Movie Lookup': 
            user.movie_lookup()
        elif option == 'Search Movies': 
            user.search()
        elif option == 'Multi Criteria Search': 
            user.multi_search()
        elif option == 'Login': 
            user.login()
        elif option == 'Registration':
            user.registration()
        else:
            exit()
            
    @staticmethod
    def get_options(self):
        with open(Paths.USER_MENU.value,'r') as f:
            try:
                return json.load(f)
            except:
                print('User Menu options not working propertly')
                return {}
    