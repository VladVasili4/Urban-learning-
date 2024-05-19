def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params('you', 4, 'me')
print_params(3)
print_params(b = 'столбец')
print_params(b = 25)
print_params(c = [1,2,3])
# --------------------------------------------

values_list = [[7, 9, 8], 'cmol', 67]
values_dict = {'a': 95, 'b': ['R', 'I', 'O'], 'c': 'Rex'}

print_params(*values_list)
print_params(**values_dict)
# --------------------------------------------

values_list2 = [(0, 1), {2, 3}]
print(values_list2)
print_params(*values_list2)
print_params(*values_list2, 42)
print_params(42, *values_list2)