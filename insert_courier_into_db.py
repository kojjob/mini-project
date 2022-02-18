import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host       = os.environ.get("mysql_host")
user       = os.environ.get("mysql_user")
password   = os.environ.get("mysql_pass")
database   = os.environ.get("mysql_db")

# Establish a database connection
connection     = pymysql.connect(
    host       = host,
    user       = user,
    password   = password,
    database   = database
)

# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Add code here to insert a new record

courier_info = "INSERT INTO Courier (courier_name, courier_phone) VALUES (%s, %s)"
courier_value =  [
    ('John Dodge', '+44 55–888–8888 '),           
    ('George	Dapper', '+44 555–999–0000'),	             
    ('Jack	Dodge', '+44 55–999–8888 '),            
    ('Dragon	Davich','+44 555–999–0000'),	             
    ('Steve	Curio', '+44 555–555–5454'),	             
    ('Laura	Black','+44 555–555–343'),    
   ]
cursor.executemany(courier_info, courier_value)

connection.commit()
cursor.close()
connection.close()
