import csv
import pymysql
import os
from dotenv import load_dotenv

# def read_csv_file(file_name, csv_to_read):
#     with open(file_name, 'r') as csv_file:
#         csv_to_read = csv.DictReader(csv_file)
#         csv_list = []
#         for row in csv_to_read:
#             csv_list.append(row)
#         return csv_list


# def save_list(file_name, list_name):
#     with open(file_name, "w", newline='') as updated:
#         if list_name:
#             writer = csv.DictWriter(updated, fieldnames=list_name[0].keys())
#             writer.writeheader()
#             writer.writerows(list_name)


# def print_csv_file(file_name, csv_file):
#     with open(file_name, 'r') as csv_print:
#         csv_file = csv.DictReader(csv_print)
#         for row in csv_file:
#             print(dict(row))


# def append_dict(file_name, dict_of_elem, field_names):
#     with open(file_name, 'a+', newline='') as write_obj:
#         dict_writer = csv.DictWriter(write_obj, fieldnames=field_names)
#         dict_writer.writerow(dict_of_elem)


# def update_index(list_name, update_input, updated_input):
#     list_name[update_input] = updated_input

# def delete_index(list_name, deleted_input):
#     del list_name[deleted_input]


# def enumerate_orders(order_list):
#     for key, value in enumerate(order_list):
#         print(key, value)
