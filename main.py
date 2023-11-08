from users.anonymous import AnonymousUser

def main():
    user = AnonymousUser()

    while True:
        user.execute_action()
        if user.logged_out:
            user = AnonymousUser()
        else:
            user = user.logged_in or user

if __name__ == "__main__":
    main()
