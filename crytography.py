from cryptography.fernet import Fernet


def key_fernet():
    key = Fernet.generate_key()
    token = Fernet(key)
    return token
