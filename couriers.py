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
