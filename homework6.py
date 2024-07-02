my_dict= {'София': 2010, 'Диана': 2012, 'Наталия': 2021}
print(my_dict)
print(my_dict['Диана'])
my_dict['Ксения'] = 2020
print(my_dict['Ксения'])
my_dict.update({'Марина': 2023, 'Виктория':2024})
print(my_dict)
a=my_dict.pop('Диана')
print(a)
print(my_dict)
my_set={'София', 10, 12, 21, 'Диана',10, 21,12, True }
print(my_set)
my_set.update({15, 16})
print(my_set)
my_set.remove(15)
print(my_set)