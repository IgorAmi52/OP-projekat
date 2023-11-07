from users.user import User
from enums.roles import Roles

class LogedUser(User):
    
    name = ''
    sirname = ''
    username = ''
    password = ''
    role = Roles.NON_LOGED

    def __init__(self):
        print("registrovani korisnik")
        
    def logout(self):
        print("odjava reg korisnika")
        
    def change_info(self):
        print("izmena podataka reg korisnika")