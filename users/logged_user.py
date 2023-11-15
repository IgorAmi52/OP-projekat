import os 
import json
import time

from pick import pick

from enums.paths import Paths
from users.user import User

from pick import pick

BAD_CHANGE_INFO_OPTIONS = {
    'title1': 'Your info cannot be blank',
    'title2': 'This Username is already taken.',
    'options': ['Try again', 'Back to Menu']
}

class LoggedUser(User):

    def execute_action(self):
        option = super().execute_action()
        if option == 'Logout':
            self.logout()
        if option == 'Change Info':
            self.change_info()
        return option
        
    def logout(self):
        self.logged_out = True
        print("odjava reg korisnika")
        
    def change_info(self):
        os.system('clear')
        name = input('Current Name is ' + self.name + '. New Name: ')
        surname = input('Current Sirname is ' + self.surname + '. New Sirname: ')
        username = input('Current Username is ' + self.username + '. New Username: ')
        password = input('Current Password is ' + self.password + '. New Password: ')
        
        #Validation 1 -- incorrect input
        if username == '' or password == '' or name == '' or surname == '':
            option,_ = pick(BAD_CHANGE_INFO_OPTIONS['options'],BAD_CHANGE_INFO_OPTIONS['title1'])
            if option == 'Back to Menu': self.execute_action()
            else: self.change_info()
        
        with open(Paths.USERS.value,'r') as f:
            try:
                data = json.load(f)
            except:
                print("getting users was uncussesful")
                exit()
        #validation 2 --- username already exists in database
        if (username in data) and self.username!=username:
            option,_ = pick(BAD_CHANGE_INFO_OPTIONS['options'],BAD_CHANGE_INFO_OPTIONS['title2'])
            if option == 'Back to Menu': self.execute_action()
            else: self.change_info()
        else:
            data.pop(self.username)
            data[username] = {
                'name':name,
                'surname': surname,
                'password':password,
                'role': self.role
            }
            for key in data[username].keys(): self.key = data[username][key]
            self.username = username
            with open(Paths.USERS.value,'w') as f:
                json.dump(data, f, indent=4)
                
            os.system('clear')
            print('You successfully changed your information!')
            time.sleep(2)
            os.system('clear')
            self.execute_action()
            


        
    
