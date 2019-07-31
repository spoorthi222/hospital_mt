from src.models.users import Users
import binascii,os
import hashlib
SALT_LENGTH = 16
HASH_METHOD = "SHA512"
class UserLib():

    def __init__(self):
        print "Intialsed userlib"

    def password_hashing(self,password,salt=None):
        if not salt:
            salt = binascii.hexlify(os.urandom(SALT_LENGTH/2)).decode()
        hash_library = hashlib.new(HASH_METHOD)
        salted_client_hash = str(password + salt)
        hash_library.update(salted_client_hash)
        server_hash = hash_library.hexdigest()
        return (server_hash,salt)

    @property
    def validate_input(self):
        if "name" not in self.user_info:
            return "missing key 'name'" ,False
        if "email_id" not in self.user_info:
            return "missing key 'email_id'", False
        if "password" not in self.user_info:
            return "missing key 'password'", False

        users = Users.objects.filter(email_id = self.user_info["email_id"])
        if users.count()>0:
            return "user already exists", False

        return "success" ,True


    def createUser(self,user_info):
        self.user_info= user_info

        message, status =self.validate_input
        if(status):
            print "validation is succesfull ",self.user_info
            password_hash , salt = self.password_hashing(self.user_info["password"])
            print password_hash , salt

            password_hash_2, salt_2 = self.password_hashing(self.user_info["password"],salt)
            print password_hash_2, salt_2


        else:
            return message , False

        return "user created succesfully", True


