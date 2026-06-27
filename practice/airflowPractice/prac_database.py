import pymysql


def main():
    conn = pymysql.connect(host="localhost", user="root", password="996232")

    try:
        with conn.cursor() as cursor:

            cursor.execute("CREATE DATABASE IF NOT EXISTS income_db")
            cursor.execute("USE income_db")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(200),
                    income INT
                )
            """)

            cursor.execute("""
                INSERT INTO employee(name, income)
                VALUES
                ('muthu', 35000),
                ('arivu', 28000)
            """)

        conn.commit()
        print("✅ Database, table and records created successfully!")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        conn.close()
        print("🔒 Database connection closed.")


if __name__ == "__main__":
    main()
    print("everything successfull")
