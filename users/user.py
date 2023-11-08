from menu.user_menu import UserMenu

class User: ### Base class for every role

    def __init__(
            self, name=None, surname=None, username=None,
            password=None, role=None
    ):
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.role = role
        self.new_active_user = None
        
    def execute_action(self):
        option = UserMenu.select_option(self)

        if option == 'Exit':
            self.exit()
        elif option == 'Movie Lookup':
            self.movie_lookup()
        elif option == 'Search Movies':
            self.search()
        elif option == 'Multi Criteria Search':
            self.multi_search()
        return option

    def exit(self):
        exit()
        
    def movie_lookup(self):
        print("pregled filmova")
        
    def search(self):
        print("pretraga filma")
        
    def multi_search(self):
        print("vise krit pretraga")
