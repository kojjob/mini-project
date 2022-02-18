import csv
import pymysql
import os
from dotenv import load_dotenv
from prettytable import PrettyTable

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")


def read_products_from_db():
  	
	connection = pymysql.connect(
	host = host,
	user = user,
	password = password,
	database = database
	)

	cursor = connection.cursor()
	
	cursor.execute('SELECT id, name, price FROM Product')

	rows = cursor.fetchall()
	for row in rows:
			print(f' {str(row[0])}: {row[1]}, £{row[2]}')
	
			cursor.close()
			connection.close()

def add_product_to_db():
  	
		connection = pymysql.connect(
		host = host,
		user = user,
		password = password,
		database = database
		)

		cursor = connection.cursor()

		item_name = str(input("Enter product name: "))
		item_price = float(input("Enter product price: "))

		product_sql    = "INSERT INTO Product (name, price) VALUES (%s, %s)"
		product_value  = (item_name, item_price)

		cursor.execute(product_sql, product_value)
		print("Your product has been added to the database")

		connection.commit()
		cursor.close()
		connection.close()

	


def read_files_to_list():
    with open("products.txt", "r") as products_file:
      product_list = products_file.readlines()
    return product_list

product_list = read_files_to_list()

def display_products():
	for index, product in enumerate(product_list):
  		print(f" {index} {product}")

def create_product():
	user_product = input("Create a product?: ")
	with open("products.txt", "a+") as products_file:
		products_file.write(user_product + ' \n')

def delete_product():
		user_input = int(input("Please choose the number of item you want to delete: "))
		del product_list[user_input]
		with open('products.txt', 'w') as file:
			file.writelines(product_list)

def update_product():
		product_index = int(input("Select a product number: "))
		updated_product = input("Update product name: ")

		product_list[product_index] = updated_product + "\n"

		with open('products.txt', 'w') as file:
			file.writelines(product_list)