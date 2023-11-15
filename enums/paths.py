import os
from enum import Enum

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class Paths(Enum):
    USERS = os.path.join(PROJECT_DIR, 'database', 'users.json')
    USER_MENU = os.path.join(PROJECT_DIR, 'menu', 'user_menu_options.json')
    AUTH_OPTIONS = os.path.join(PROJECT_DIR,'authentication','auth_options.json')
