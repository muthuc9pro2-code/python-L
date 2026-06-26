import pymysql

conn = pymysql.connect(host="localhost", user="root", password="996232", database="etl")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO employess(name, age)
VALUES("MUTHU", 22)
""")

conn.commit()  # .commit() is to save the file or changes in mysql

print("success")

conn.close()


