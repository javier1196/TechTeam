"""from flaskext.mysql import MySQL
from flask import Flask, request, jsonify,make_response


MYSQL_DATABASE_USER = 'cisco'
MYSQL_DATABASE_PASSWORD = 'techteam'
MYSQL_DATABASE_DB = 'supportsystem'
MYSQL_DATABASE_HOST = 'bnetservice.com.mx'
MYSQL_DATABASE_PORT = int('3306')

mysql = MySQL()
app = Flask(__name__)
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()
cursor.execute("SELECT * from Department")
data = cursor.fetchone()
print(data)

"""
"""import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='80.211.191.58',
                                         database='supportsystem',
                                         user='adrian',
                                             password='Privado1')
    if connection.is_connected():
        print("hiiiiii")
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM department")
        #record = cursor.fetchone()
        record = cursor.fetchall()
        print("You're connected to database: ", record)


except Error as e:
    print("Error while connecting to MySQL", e)
    finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")"""

from adapter.department import DepartmentAdapter

department = {
    "department": "prueba2"
}

functions = DepartmentAdapter()
print(functions.update(5, department))
