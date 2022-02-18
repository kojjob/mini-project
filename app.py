from products import *
from couriers import *
from orders import *
from pyfiglet import Figlet


def banner():
	f = Figlet(font="slant")
	print(f.renderText('Gen Cafe !'))
	print("""
	      Welcome to GenCafe.	 
			""")

def product_menu():
  	while True:
				product_menu_input = int(input("""
				Please choose an option: 
				1. Display Products, 
				2. Create a product
				3. Delete a product
				4. Update a product
				0. Quit,
				
				"""))

				if product_menu_input == 1:
						read_products_from_db()
									
				if product_menu_input == 2:
						add_product_to_db()		

				if product_menu_input == 3:
					delete_product()

				if product_menu_input == 4:
						update_product()

				if product_menu_input == 0:
					main_menu()

def courier_menu():
  	while True:
				courier_menu_input = int(input("""
				Please choose an option: 
				1. Display  Couriers, 
				2. Create a Courier
				3. Delete a Courier
				4. Update a Courier
				0. Main Menu,
				
				"""))

				if courier_menu_input == 1:
						read_couriers_from_db()			

				if courier_menu_input == 2:
						add_courier_to_db()			

				if courier_menu_input == 3:
					delete_courier()

				if courier_menu_input == 4:
						update_courier()
						
				if courier_menu_input == 0:
					main_menu()

def orders_menu():
  	while True:
				order_menu_input = int(input("""
				Please choose an option: 
				1. Display  Orders, 
				2. Create a Order
				3. Delete a Order
				4. Update a Order
				0. Main Menu,
				
				"""))

				if order_menu_input == 1:
						enumerate_orders(csv_lists)			

				if order_menu_input == 2:
						print("Create a new order here")			

				if order_menu_input == 3:
					print("Update a  order here")

				if order_menu_input == 4:
						print("Delete a order here")

				if order_menu_input == 0:
					print("Go to main menu")
					main_menu()

def main_menu():
		banner()
		while True:
			main_menu_input = int(input("""
			Please choose one of the following menu:  
			Enter 1: Product Menu
			Enter 2: Courier Menu
			Enter 3: Order Menu
			Enter 0: Exit.	
			"""))

			if main_menu_input == 1:
					print('This is Product menu')
					product_menu()

			if main_menu_input == 2:
					print("I am Courie menu")
					courier_menu()
			
			if main_menu_input == 3:
					print("I am Order menu")
					orders_menu()
				
			if main_menu_input == 0:
					print("Thanks for coming.")
					exit()

main_menu()
product_menu()
courier_menu()
orders_menu()
