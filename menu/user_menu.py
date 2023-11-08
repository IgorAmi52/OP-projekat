import json

from pick import pick

from enums.paths import Paths

class UserMenu:
    
    @classmethod
    def select_option(cls, user):
        
        options = cls.get_options(cls)
        
        option, _ = pick(
            options[user.role]['options'],
            options[user.role]['title']
        )
        return option

    @staticmethod
    def get_options(self):
        with open(Paths.USER_MENU.value,'r') as f:
            try:
                return json.load(f)
            except:
                print('User Menu options not working propertly')
                return {}
