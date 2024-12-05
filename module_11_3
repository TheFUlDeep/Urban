import inspect
from pprint import pprint
import sys

def introspection_info(obj):
    res = dict()
    # тип
    res['type'] = (type(obj))

    # атрибуты
    res['attrs'] = dir(obj)

    # методы объекта
    res['methods'] = [x for x in dir(obj) if callable(getattr(obj, x))]

    # к какому модулю относится
    res['module'] = inspect.getmodule(type(obj))

    # размер
    res['size'] = sys.getsizeof(obj)

    res['isclass'] = inspect.isclass(obj)

    res['IsInstanceOfException'] = isinstance(obj, Exception)
    return res


class MyClass(Exception):
    def __init__(self):
        self.attr = 1

    def attrfunc(self):
        pass


# IsInstanceOfException будет False, isclass будет True
number_info = introspection_info(MyClass)
pprint(number_info)

# IsInstanceOfException будет True, добавится атрибут attr, isclass будет False
number_info = introspection_info(MyClass())
pprint(number_info)
