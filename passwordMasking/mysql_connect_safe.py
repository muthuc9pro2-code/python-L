import pymysql
from password_utils import get_decrypted_password


def connect_mysql():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password=get_decrypted_password(),
        database="test",  
    )

    print("connection is successful")
    print(get_decrypted_password())
    connection.close()

if __name__ == "__main__":  #This is a python predefined idiom
    connect_mysql()



