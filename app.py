from pyfiglet import Figlet


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


'++++++++++++++++++++++++++++++++++++++++++++++++++++++++'


def read_files_to_list():
	with open("couriers.txt", "r") as courier_file:
		courier_list = courier_file.readlines()
		# strip all the extra newline from items
		for list in courier_list:
			return courier_list


courier_list = read_files_to_list()


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


'++++++++++++++++++++++++++++++++++++++++++++++++++++++++'


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
			print("Display products here")
			display_products()

		if product_menu_input == 2:
			print("Create a new product here")
			create_product()

		if product_menu_input == 3:
			print("Delete a  product here")
			delete_product()

		if product_menu_input == 4:
			print("Update a product here")
			update_product()

		if product_menu_input == 0:
			print("Go to main menu")
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
			print("Display couriers here")
			display_courier()

		if courier_menu_input == 2:
			print("Create a new courier here")
			create_courier()

		if courier_menu_input == 3:
			print("Delete a  courier here")
			delete_courier()

		if courier_menu_input == 4:
			print("Update a courier here")
			update_courier()

		if courier_menu_input == 0:
			print("Go to main menu")
			main_menu()


def order_menu():
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
			print("Display orders here")

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
			order_menu()

		if main_menu_input == 0:
			print("Thanks for coming.")
			exit()


main_menu()
product_menu()
courier_menu()
order_menu()
