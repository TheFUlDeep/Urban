import numbers


def calculate_structure_sum(obj):
    summ = 0
    if isinstance(obj, str):
        summ += len(obj)
        # print(obj, "is str")
    elif isinstance(obj, numbers.Number):
        summ += obj
        # print(obj, "is num")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            summ += calculate_structure_sum(k)
            summ += calculate_structure_sum(v)
    elif "__iter__" in dir(obj):
        for i in obj:
            summ += calculate_structure_sum(i)
    return summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
