from users.anonymous import AnonymousUser
from users.buyer import Buyer
from users.seller import Seller
from users.manager import Manager
from enums.roles import Roles


class UserMapper:
    
    user_map = {
        Roles.BUYER.value: Buyer,
        Roles.NON_LOGED.value: AnonymousUser,
        Roles.SELLER.value: Seller,
        Roles.MANAGER.value: Manager
    }

    @classmethod
    def get(cls, user):
        return cls.user_map[user.role]
    
