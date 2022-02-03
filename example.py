# list = ['banana', 'apple', 'pear']

# with open('example.txt', 'w') as file:

#   for item in list:
#     file.write(item + "\n")

#  file.writelines(list)

list = ['banana\n', 'apple\n', 'pear\n', 'plum\n']

#list[0] = list[0].rstrip()

# for item in list:
#   #print(item.rstrip())
#   item = item.rstrip()

for index in range(0, len(list)):
    list[index] = list[index].rstrip()

print(list)