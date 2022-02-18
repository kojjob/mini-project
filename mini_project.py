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

# Execute SQL query
cursor.execute('SELECT id, name, price FROM Product')

# Gets all rows from the result
rows = cursor.fetchall()
for row in rows:
    print(f'id: {str(row[0])},name: {row[1]}, price: {row[2]}')

# Can alternatively get one result at a time with the below code
# while True:
#     row = cursor.fetchone()
#     if row == None:
#         break
#     print(f'First Name: {str(row[0])}, Last Name: {row[1]}, Age: {row[2]}')

# Closes the cursor so will be unusable from this point 
cursor.close()

# Closes the connection to the DB, make sure you ALWAYS do this
connection.close()