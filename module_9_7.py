def is_prime(func):
    def wrapper(*args, **kwargs):
        func_res = func(*args, **kwargs)
        _is_prime = True
        for i in range(2, func_res):
            if func_res % i == 0:
                _is_prime = False
                break
        if _is_prime:
            print('Простое')
        else:
            print('Составное')
        return func_res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
