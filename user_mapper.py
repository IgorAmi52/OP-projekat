from users.non_loged_user import NonLogedUser
from users.buyer import Buyer
from users.seller import Seller
from users.manager import Manager
from enums.roles import Roles


class UserMapper:
    
    user_map = {
        Roles.BUYER.value: Buyer,
        Roles.NON_LOGED.value: NonLogedUser,
        Roles.SELLER.value: Seller,
        Roles.MANAGER.value: Manager
    }

    @classmethod
    def get(cls, user):
        new_user = cls.user_map[user.role]()
        new_user.name = user.name
        new_user.sirname = user.sirname
        new_user.password = user.password
        new_user.username = user.username
        
        return new_user
    
    