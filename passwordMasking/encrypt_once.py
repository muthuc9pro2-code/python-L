from password_utils import encrypt_password   # python built-in function
from cryptography.fernet import Fernet            # this is a cyrptographic method we gona use to generate password

# Generate Key and save to file


def generate_key():
    key = Fernet.generate_key()  # .generate_key is already predefined in fernet
    with open(
        "passwordMasking/secret.key", "wb"
    ) as f:  # wb is called write binary ,the .generate_key() produces a output in bytes so to write that we have to write 'wb'
        f.write(key)
    print("key saved to 'secret.key'")


if __name__ == "__main__":
    # uncomment this only the first time
    generate_key()

    # replace with real mysql root password
    encrypted = encrypt_password(input("Enter the password : "))
    print(encrypted)

