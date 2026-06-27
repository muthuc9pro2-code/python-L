import pymysql

conn = pymysql.connect(
    host="localhost", user="root", password="996232", database="income_db", cursorclass=pymysql.cursors.DictCursor
)

with conn.cursor() as cursor: 

    cursor.execute("SELECT * FROM employee")

    rows = cursor.fetchall()

    for row in rows:
        row["name"] = row["name"].upper()

    print(row)