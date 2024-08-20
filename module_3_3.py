def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(100)
print_params(100, [1, 2, 3])
print_params(5, c=10)
print_params(5, b="число", c=10)
print_params(c=5, a="число", b=10)
print_params(a=5, c="число")
print_params(b=5, c=False)
print_params("123", "456", c=10)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, "True", True]
values_dict = {"a": 1, "b": "True", "c": True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [100500, [1, 2, 3]]
print_params(*values_list_2, 42)
