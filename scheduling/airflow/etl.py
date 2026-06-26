import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="996232",
    database="etl",
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM employess")

data = cursor.fetchall()

for row in data:
    row["name"] = row["name"].lower()

print(data)