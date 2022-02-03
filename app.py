def main_menu():
  print(""" 
        Welcome to GenCafe, here are your options.
        Enter 0: to exit.
        Enter 1: to go to menu.
  """)


def read_files_to_list():
    with open("products.txt", "r") as products_file:
      product_list = products_file.readlines()   
    # strip all the extra newline from items
    for list in product_list:
      return product_list
  
# def format_product_list(products):
#     for product in products:
#         product_list.append(product.strip())
#     return product_list

def display_products():
    for index, product in enumerate(product_list, start=1):
      print(f" {index} {product}")

def create_product():
  user_product = input("Create a product?: ")
  with open("products.txt", "a+") as products_file:
    products = products_file.write(user_product + ' \n')
    products_file.close()

def delete_product():
  user_input = int(input("Please choose a number: ")) 
  for index, product in enumerate(product_list):
    if(user_input == index):
      del product_list[index]
      print(index)

def update_product():
  product_index = int(input("Select a product number: "))
  updated_product = input("Update product name: ")

  product_list[product_index] = updated_product

  with open('products.txt', 'w') as file:

    for item in product_list:
      file.write(item)

  


# *********************************************************************
exit            =  "0"
go_to_menu      =  "1"
create_products =  "2"
delete_products  =  "3"
update_products  =  "4"
welcome = "Welcome to GenCafe.This is our menu"
product_list = read_files_to_list()

print(
  """
    Choose an options:.upper() 
    0. Quit, 
    1. Display Products, 
    2. Create a product
    3. Delete a product
    4. Update a product
  """
)

while True:
  user_input = input("Please choose an option: ")
  if(user_input == go_to_menu):
    display_products()
  elif(user_input == create_products):
    create_product()
    display_products()
  elif(user_input == delete_products):
    delete_product()

  elif(user_input == update_products):
    update_product()

  elif(user_input == exit):
    print("Thanks for coming")
    break
