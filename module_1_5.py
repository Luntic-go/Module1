immutable_var = 1, 'string', True
print(immutable_var)
#immutable_var[2] = False                   Кортежи являются неизменяемым объектом, т.е. не поддерживают изменение элеиентов, находящихся внутри.

mutable_list = [1, 'string', True]
mutable_list.append("3.14")
print(mutable_list)