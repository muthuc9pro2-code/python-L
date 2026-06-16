from cryptography.fernet import Fernet

class fakeStr(str):
    def __str__(self):
        return "***********"
    def __repr__(self):
        return "***********"


def load_key():
    return open("passwordMasking/secret.key", "rb").read()

#encrypt the plain password

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    with open("passwordMasking/get_decrypt", "wb") as file:
        file.write(encrypted)
    return encrypted

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypt = f.decrypt(encrypted_password).decode()
    return fakeStr(decrypt)

def get_decrypted_password():
    encrypt_password = open("passwordMasking/get_decrypt", "rb").read()
    return decrypt_password(encrypt_password)