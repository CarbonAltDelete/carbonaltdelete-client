from enum import Enum


class UserStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    INVITED = "INVITED"
    NO_ACCESS = "NO_ACCESS"
    DELETED = "DELETED"
