import sys
    ### Dodaj sve pathove gde python treba da trazi import
from users.non_loged_user import NonLogedUser
from user_mapper import UserMapper

def main():
    
    user = NonLogedUser()

    while(True):
        new_user = UserMapper.get(user)

main()