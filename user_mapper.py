from users.non_loged_user import NonLogedUser
from users.buyer import Buyer
from users.seller import Seller
from users.manager import Manager
from enums.roles import Roles


class UserMapper:
    
    user_map = {
        Roles.BUYER: Buyer,
        Roles.NON_LOGED: NonLogedUser,
        Roles.SELLER: Seller,
        Roles.MANAGER: Manager
    }

    @classmethod
    def get(cls, role):
        return cls.user_map.get(role)
    
    