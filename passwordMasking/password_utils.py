from cryptography.fernet import Fernet

def load_key():
    return open("passwordMasking/secret.key", "rb").read()

#encrypt the plain password

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(password):
    key = load_key()
    f = 

