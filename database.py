import os
import mysql.connector
from mysql.connector import errorcode

DB_CONFIG = {
    'host': os.environ.get('DB_HOST', '127.0.0.1'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'database': os.environ.get('DB_NAME', 'kokani_bazaar')
}

connection = None
cursor = None

try:
    # Connect to the database
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    # Initialize the database
    with open('database.sql', 'r') as sql_file:
        sql_commands = sql_file.read()
        for command in sql_commands.split(';'):
            if command.strip():
                cursor.execute(command)
    connection.commit()
    print("Database initialized successfully!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid credentials. Please check your DB_USER and DB_PASSWORD.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)

finally:
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()
