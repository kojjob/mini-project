import csv
import pymysql
import os
from dotenv import load_dotenv






def read_couriers_from_db():
  	
	load_dotenv()
	host = os.environ.get("mysql_host")
	user = os.environ.get("mysql_user")
	password = os.environ.get("mysql_pass")
	database = os.environ.get("mysql_db")

  	
	connection = pymysql.connect(
	host = host,
	user = user,
	password = password,
	database = database
)

	cursor = connection.cursor()
	
	cursor.execute('SELECT id, courier_name, courier_phone FROM Courier')

	rows = cursor.fetchall()
	for row in rows:
			print(f'{row[1]}, {row[2]}')
	
	cursor.close()
	connection.close()

def add_courier_to_db():
  	
		load_dotenv()
		host = os.environ.get("mysql_host")
		user = os.environ.get("mysql_user")
		password = os.environ.get("mysql_pass")
		database = os.environ.get("mysql_db")
 	
		connection = pymysql.connect(
		host = host,
		user = user,
		password = password,
		database = database
	)

		cursor = connection.cursor()

		courier_name = str(input("Enter cuourier name: "))
		courier_phone = str(input("Enter cuourier phone number: ")) 

		courier_sql    = "INSERT INTO Courier (courier_name, courier_phone) VALUES (%s, %s)"
		courier_value  = (courier_name, courier_phone)

		cursor.execute(courier_sql, courier_value)
		print("Your cuourier has been added to the database")

		cursor.close()
		connection.close()





def read_files_to_list():
    with open("couriers.txt", "r") as courier_file:
      courier_list = courier_file.readlines()
    # strip all the extra newline from items
      for list in courier_list:
        return courier_list


courier_list = read_files_to_list()
print(courier_list)

def display_courier():
	for index, courier in enumerate(courier_list, start=1):
  		print(f" {index} {courier}")

def create_courier():
			user_courier = input("Create a courier?: ")
			with open("couriers.txt", "a+") as couriers_file:
				couriers_file.write(user_courier + ' \n')
				couriers_file.close()

def delete_courier():
		user_input = int(input("Please choose a number: ")) 
		del courier_list[user_input]
		with open('courier.txt', 'w') as file:
			file.writelines(courier_list)		

def update_courier():
		courier_index = int(input("Select a courier number: "))
		updated_courier = input("Update courier name: ")

		courier_list[courier_index] = updated_courier + "\n"

		with open('couriers.txt', 'w') as file:
			file.writelines(courier_list)