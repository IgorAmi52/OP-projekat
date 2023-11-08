from users.anonymous import AnonymousUser
from user_mapper import UserMapper

def main():
    
    user = AnonymousUser()

    while True:
        user.execute_action()
        user = user.new_active_user or user

if __name__ == "__main__":
    main()
