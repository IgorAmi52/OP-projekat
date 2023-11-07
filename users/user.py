import json
from os import system

from pick import pick

from enums.roles import Roles
from enums.paths import Paths
from authentication.authentication import Authentication
from menu.user_menu import UserMenu

class User: ### Base class for every role

    def __init__(self):
        self.role = "User"
       

    def login(self):  #Try to Login the user 
        Authentication.login(self)
        
    def registration(self):
        Authentication.registration()
        self.user_menu()
        
    def user_menu(self):
        UserMenu.get_user_menu(self,self.role)
          
    def exit(self):
        exit()
        
    def movie_lookup(self):
        print("pregled filmova")
        
    def search(self):
        print("pretraga filma")
        
    def multi_search(self):
        print("vise krit pretraga")
    