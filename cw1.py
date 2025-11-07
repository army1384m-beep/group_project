import hashlib
from datetime import datetime
from dataclasses import dataclass , field


@dataclass
class User :
    name : str
    email : str
    hash_password  : str
    created_at : datetime = field(default_factory= datetime.now)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def user_creator(cls ,name , email , password ) :
        hash_obj  = cls.hash_password(password)
        return cls(name = name  , email = email ,hash_password = hash_obj)

user1 = User.user_creator("parsa" , "ab12@email.com" , "1234")
print(user1)