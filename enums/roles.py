from enum import Enum


class Roles(Enum):
    NON_LOGED = 'Non logged User'
    BUYER = "Buyer"
    SELLER = 'Seller'
    MANAGER = 'Manager'