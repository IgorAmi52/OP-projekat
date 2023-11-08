from users.user import User

class LoggedUser(User):

    def execute_action(self):
        option = super().execute_action()
        if option == 'Logout':
            self.logout()
        return option
        
    def logout(self):
        self.logged_out = True
        print("odjava reg korisnika")
        
    def change_info(self):
        print("izmena podataka reg korisnika")
