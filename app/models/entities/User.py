

class User():

    def __init__(self, id, username, password, email, created_at) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.created_at = created_at

    @classmethod
    def check_password(self, key_fernet, password):

        print(key_fernet, password)
        if key_fernet == password:
            return True
        else:
            return False
