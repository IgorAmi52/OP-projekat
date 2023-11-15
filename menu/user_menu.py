import json

from pick import pick

from enums.paths import Paths

class UserMenu:
    
    """Shows awailable option for user (depending on the role)

    Returns:
        string: Picked option
    """
    
    @classmethod
    def select_option(cls, user):
    
        options = UserMenu.get_options()
        option, _ = pick(
            options[user.role]['options'],
            options[user.role]['title']
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
