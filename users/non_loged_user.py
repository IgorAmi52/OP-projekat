import json
from os import system

from pick import pick

from enums.roles import Roles
from users.user import User
from enums.paths import Paths
from menu.user_menu import UserMenu

class NonLogedUser(User):
    
    def __init__(self):  
        UserMenu.get_user_menu(self, Roles.NON_LOGED.value)