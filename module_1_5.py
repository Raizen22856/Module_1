immutable_var = 75, 'Strong', False
print(immutable_var)
# immutable_var[0] = 32     Нельзя изменить значение элемента кортежа т.к. сам кортеж является не изменяемым списком, т.е. нельзя изменить значение элементов кортежа, если этот элемент не является изменяемым элементом по типу списков
mutable_list = [32, 'Weak', True]
print(mutable_list)
mutable_list[0] = 12
mutable_list[1] = 'Very weak'
mutable_list[2] = False
print(mutable_list)