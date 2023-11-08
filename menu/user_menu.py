import json

from pick import pick

from enums.paths import Paths

class UserMenu:
    
    @classmethod
    def select_option(cls, user):
        
        options = UserMenu.get_options()
        user_class = user.__class__

        option, _ = pick(
            options[user_class.role]['options'],
            options[user_class.role]['title']
        )
        return option

    @staticmethod
    def get_options():
        with open(Paths.USER_MENU.value,'r') as f:
            try:
                return json.load(f)
            except:
                print('User Menu options not working propertly')
                return {}
