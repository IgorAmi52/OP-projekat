from users.user import User

class LoggedUser(User):
        
    def logout(self):
        print("odjava reg korisnika")
        
    def change_info(self):
        print("izmena podataka reg korisnika")
