import csv

orders = [
  {'customer_name': 'Kojo', 'customer_address': 'St.Peters 48, London', 'customer_phone': '+44 88675309', 'customer_email': 'cust@gmail.com','courier': 2, "status": 'preparing', 'products': [1, 2, 3]},
  {'customer_name': 'Mary', 'customer_address': 'Menphis 230, Leeds', 'customer_phone': '+44 88675309', 'customer_email':'cus1@gmail.com','courier': 3, "status": 'preparing', 'products': [1, 2]},
  {'customer_name': 'John', 'customer_address': 'Accra 37, Leeds', 'customer_phone': '+44 88675309', 'customer_email': 'cus2@gmail.com','courier': 2, "status": 'preparing', 'products': [1, ]}
  ]


def write_to_csv_file(file_name, data):
    with open(file_name, mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)



def read_and_display_orders(file_name, csv_to_read):
    with open(file_name, 'r') as csv_file:
        csv_to_read = csv.DictReader(csv_file)
        csv_list = []
        for row in csv_to_read:
            csv_list.append(row)
        print(csv_list)
        return csv_list

def delete_index(list_name, deleted_input):
    del list_name[deleted_input]


def enumerate_orders(order_list):
    for key, value in enumerate(order_list):
        print(key, value)


csv_lists = read_and_display_orders('orders.csv', orders)        
        
enumerate_orders(csv_lists)