from users.logged_user import LoggedUser


class Manager(LoggedUser):
    role = 'Manager'
    
    def execute_action(self):
        option = super().execute_action()
        if option == "Register New Employee":
            self.register_new_employee()



    def register_new_employee(self):
        exit()