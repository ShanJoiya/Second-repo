my_dict = {'Name': 'Jack', 'Age': 26, 'Citizen': 'Pakistan'}

print(my_dict['Name'])
print(my_dict.get('Age'))

my_dict['Age'] = 27
print(my_dict)


my_dict['Address'] = 'Downtown'
print(my_dict)

my_dict.pop('Age')
print(my_dict)


print("Address :", my_dict.get('Address'))

my_dict.clear()
print(my_dict)

print(my_dict.get('Citizen'))



