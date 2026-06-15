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
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypt = f.decrypt(encrypted_password).decode()
    return fakeStr(decrypt)

def get_decrypted_password():
    encrypt_password = b'gAAAAABqLrMwd3EEcCblwGA4nIFmhuNHBoHWd6cuTOPfv1HUEl258JiEuY0nS8FTFTi7JFWQzbBR9OlCThEpggiPhCAxl--Fog=='
    return decrypt_password(encrypt_password)
