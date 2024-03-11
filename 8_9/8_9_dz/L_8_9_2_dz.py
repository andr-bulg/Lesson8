"""
Создайте базовый абстрактный класс “Фигура” с методами вычисления площади и периметра.

Реализуйте производные классы “Прямоугольник”, “Трапеция” и “Круг”
с собственными методами вычисления площади и периметра.
"""

from math import pi

# Импорт абстрактного базового класса и декоратора
from abc import ABC, abstractmethod

# Определение абстрактного базового класса Figure
class Figure(ABC):

    @abstractmethod
    def calculate_area(self):
        """
        Абстрактный метод вычисления площади фигуры
        :return: Площадь фигуры
        """
        pass

    @abstractmethod
    def calculate_perimetr(self):
        """
        Абстрактный метод вычисления периметра фигуры
        :return: Периметр фигуры
        """
        pass


class Rectangle(Figure):

    def __init__(self, a, b):
        """
        Инициализатор класса Rectangle
        :param a: первая сторона прямоугольника
        :param b: вторая сторона прямоугольника
        """
        self.a = a
        self.b = b

    # Реализация абстрактного метода calculate_area
    def calculate_area(self):
        """
        Вычисление площади прямоугольника
        :return: Площадь прямоугольника
        """
        return self.a * self.b

    # Реализация абстрактного метода calculate_perimetr
    def calculate_perimetr(self):
        """
        Вычисление периметра прямоугольника
        :return: Периметр прямоугольника
        """
        return 2 * self.a + 2 * self.b


class Trapezoid(Figure):
    def __init__(self, a, b, c, d, h):
        """
        Инициализатор класса Trapezoid
        :param a: нижнее основание трапеции
        :param b: верхнее основание трапеции
        :param c: левая боковая сторона трапеции
        :param d: правая боковая сторона трапеции
        :param h: высота трапеции
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h

    # Реализация абстрактного метода calculate_area
    def calculate_area(self):
        """
        Вычисление площади трапеции
        :return: Площадь трапеции
        """
        return ((self.a + self.b)/2) * self.h

    # Реализация абстрактного метода calculate_perimetr
    def calculate_perimetr(self):
        """
        Вычисление периметра трапеции
        :return: Периметр трапеции
        """
        return self.a + self.b + self.c + self.d


class Circle(Figure):
    def __init__(self, r):
        """
        Инициализатор класса Circle
        :param r: радиус окружности
        """
        self.r = r

    # Реализация абстрактного метода calculate_area
    def calculate_area(self):
        """
        Вычисление площади окружности
        :return: Площадь окружности
        """
        return round(pi * self.r ** 2, 2)

    # Реализация абстрактного метода calculate_perimetr
    def calculate_perimetr(self):
        """
        Вычисление периметра окружности
        :return: Периметр окружности
        """
        return round(2 * pi * self.r, 2)


# Создание объектов классов-потомков,
# вызов на этих объектах, реализованных абстрактных методов

r1 = Rectangle(5, 10)
print("Площадь прямоугольника:", r1.calculate_area())
print("Периметр прямоугольника:", r1.calculate_perimetr())

print('*'*30)

t1 = Trapezoid(11, 3, 5, 5, 3)
print("Площадь трапеции:", t1.calculate_area())
print("Периметр трапеции:", t1.calculate_perimetr())

print('*'*30)

c1 = Circle(5)
print("Площадь окружности:", c1.calculate_area())
print("Периметр окружности:", c1.calculate_perimetr())

