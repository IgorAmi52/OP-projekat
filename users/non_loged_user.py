import json
from os import system

from pick import pick

from enums.roles import Roles
from users.user import User
from enums.paths import Paths
from menu.user_menu import UserMenu

class NonLogedUser(User):
    
    def __init__(self):  
        super().__init__()
        self.role = Roles.NON_LOGED.value
        self.user_menu()