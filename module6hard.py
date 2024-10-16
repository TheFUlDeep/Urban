from math import pow
from math import pi

class Figure:
    sides_count = 0

    def __init__(self, *args):
        self.__sides = []
        # проверка на куб
        default_value = 1
        if self.sides_count == 12 and len(args[1:]) == 1:
            default_value = args[1]
        for i in range(self.sides_count):
            self.__sides.append(default_value)
        self.set_sides(*args[1:])
        self.__color = [0, 0, 0]
        self.set_color(args[0][0], args[0][1], args[0][2])

        # этот параметр нужен по ТЗ, но нигде не используется
        filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and r in range(256) and g in range(256)
                and b in range(256)):
            return True

    def set_color(self, r, g, b):
        if not self.__is_valid_color(r, g, b):
            return
        self.__color[0] = r
        self.__color[1] = g
        self.__color[2] = b

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for i in sides:
            if not isinstance(i, int) or i < 1:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if not self.__is_valid_sides(*new_sides):
            return
        for i in range(self.sides_count):
            self.__sides[i] = new_sides[i]


class Circle(Figure):
    sides_count = 1

    def __init__(self, *args):
        super().__init__(*args)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * pow(self.__radius, 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        a = sides[0]
        b = sides[1]
        c = sides[2]
        p = 1 / 2 * (a + b + c)
        return pow((p * (p - a) * (p - b) * (p - c)), (1 / 2))


class Cube(Figure):
    sides_count = 12

    def __init__(self, *args):
        super().__init__(*args)
        sides = []
        for i in range(12):
            sides.append(args[1])
        self.set_sides(sides)

    def get_volume(self):
        return pow(self.get_sides()[0], 3)


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# triangle1 = Triangle((255, 255, 255), 1, 1, 1)

# print(circle1._Circle__radius)
# print(circle1.get_square())
# print(triangle1.get_square())


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
