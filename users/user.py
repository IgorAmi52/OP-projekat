import os
from menu.user_menu import UserMenu

class User: ### Base class for every role

    role = 'None'
    
    def __init__(
            self, name=None, surname=None, username=None, password=None):
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.logged_in = None
        self.logged_out = None

    def execute_action(self):
        option = UserMenu.select_option(self)

        if option == 'Exit':
            self.exit()
        elif option == 'Movie Lookup':
            self.movie_lookup()
        elif option == 'Search Movies':
            self.search()
        elif option == 'Multi Criteria Search':
            self.multi_search()
        return option

    def exit(self):
        os.system('clear')
        exit()
        
    def movie_lookup(self):
        print("pregled filmova")
        
    def search(self):
        print("pretraga filma")
        
    def multi_search(self):
        print("vise krit pretraga")
