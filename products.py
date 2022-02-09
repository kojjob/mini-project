
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
