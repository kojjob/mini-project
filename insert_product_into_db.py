import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host      = os.environ.get("mysql_host")
user      = os.environ.get("mysql_user")
password  = os.environ.get("mysql_pass")
database  = os.environ.get("mysql_db")

# Establish a database connection
connection    = pymysql.connect(
    host      = host,
    user      = user,
    password  = password,
    database  = database
)

# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Add code here to insert a new record

# name = input('Please enter your first name: ')
# price = float(input('Please enter your last name: '))


# print(f'This user is {first_name} {last_name} your are {age} and your email is {email} ')

product_info  = "INSERT INTO Product (name, price) VALUES (%s, %s)"
product_value =  [
    ('Tea', 1.50),
    ('Milk', 3.00),
    ('Bread', 2.00),
    ('Eggs', 3.50),
    ('Macchiato', 3.50),
    ('Espresso', 3.99),
    ('Cappuccino', 3.5),
    ('Latte', 1.45),
    ('Mocha', 2.95),
    ('Hot Chocolate', 3.35),
    ('Tea', 1.95),
    ('Coffee', 2.59),
    ('Coffee with milk', 2.25),
    ('chocolate', 2.95),
   ]
cursor.executemany(product_info, product_value)

connection.commit()
cursor.close()
connection.close()