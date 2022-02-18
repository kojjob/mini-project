import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
cursor = connection.cursor()
  
cursor.execute('CREATE TABLE Orders (id INT NOT NULL AUTO_INCREMENT, customer_name VARCHAR(255) NOT NULL, customer_address VARCHAR(255) NOT NULL, customer_phone VARCHAR(255), PRIMARY KEY(id), courier_id INT NOT NULL, product_id VARCHAR(255) NOT NULL)')

connection.commit()
cursor.close()
connection.close()
