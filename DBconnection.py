import pymysql

#step one connect to the Database

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='996232',
    database='test', # make sure this db exist
    cursorclass=pymysql.cursors.DictCursor #dictCursor is nothing but just change the output into dictionaries
)
"""
try: 
    with connection.cursor() as cursor:  #cursor will execute the queries in the mysql

        # step2: create a table
        create_query = 
        CREATE TABLE IF NOT EXISTS employees (
             id INT AUTO_INCREMENT PRIMARY KEY,
             name VARCHAR(100),
             department VARCHAR(100)
        );
    
        cursor.execute(create_query)

        # step3 : insert Data
        insert_query = "INSERT INTO employees (name, department) VALUES (%s,%s)"
        values = [("john", "IT"), ("Alice","HR"), ("Bob", "Finance")]
        cursor.executemany(insert_query,values)
        connection.commit()

        # step4 : select Data
        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)
        result = cursor.fetchall()

        for row in result:
            print(row)

# This all capital letters are sql syntax that you should learn sry bud!

finally: 
    connection.close()
"""
# you can also write that data's in other file too

try: 
    with connection.cursor() as cursor:  #cursor will execute the queries in the mysql

        # step2: create a table
        create_query = """
        CREATE TABLE IF NOT EXISTS employees (
             id INT AUTO_INCREMENT PRIMARY KEY,
             name VARCHAR(100),
             department VARCHAR(100)
        );
        """
        cursor.execute(create_query)

        # step3 : insert Data
        insert_query = "INSERT INTO employees (name, department) VALUES (%s,%s)"
        values = [("john", "IT"), ("Alice","HR"), ("Bob", "Finance")]
        cursor.executemany(insert_query,values)
        connection.commit()

        # step4 : select Data
        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)
        result = cursor.fetchall()

        with open("fileHandling/DB.txt", "w") as file:
            for row in result:
                file.write(f"{row}\n")

# This all capital letters are sql syntax that you should learn sry bud!

finally: 
    connection.close()

# now we should hard code the connection(pymysql.connect) in the file we have to mask password and stuff 
# you see that in passwordMasking folder



