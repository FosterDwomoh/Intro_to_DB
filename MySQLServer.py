import mysql.connector
from mysql.connector import errorcode
def create_database():
    try:
        connection = mysql.connector.connect(
                host = "localhost"
                user = "root"
                password = Scuba_1234
                )
        mycursor = connection.cursor()
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        mycursor.execute(create_db_query)
        connection.commit()
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("somthing is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Error: {err}")
        finally:
            if mycursor:
                mycursor.close()
            if connection:
                connection.close()
                if __name__ == "__main__":
                    create_database()

