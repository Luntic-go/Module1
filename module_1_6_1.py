my_dict = {'Anatoliy' : 1997,
           'Sergey' : 2000}
print(my_dict)
print(my_dict.get('Anatoliy'))
print(my_dict.get('Artem'))
my_dict.update({'Dmitriy': 2000,
                'Eduard' : 2003})
val = my_dict.pop('Eduard')
print(val)
print(my_dict)


my_set = {1,3,4,3,2,34, 'String', 6, 4,2,2,1, 'String'}
print(my_set)
my_set.update('8', '9')
my_set.discard(34)
print(my_set)