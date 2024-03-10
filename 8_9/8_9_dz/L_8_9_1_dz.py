"""
Создайте базовый абстрактный класс “Прогрессия”
с методами вычисления i-го элемента и суммы прогрессии.

Реализуйте производные классы “Арифметическая прогрессия” и “Геометрическая прогрессия”
с собственными методами вычисления i-го элемента и суммы.
"""

# Импорт абстрактного базового класса и декоратора
from abc import ABC, abstractmethod

# Определение абстрактного базового класса Progression
class Progression(ABC):
    def __init__(self, elem, d):
        """
        Инициализатор абстрактного базового класса
        :param elem: первый элемент прогрессии
        :param d: разность/знаменатель прогрессии
        """
        self.elem = elem
        self.d = d

    @abstractmethod
    def calculate_element(self, i):
        """
        Абстрактный метод вычисления i-ого элемента прогрессии
        :param i: номер элемента прогрессии
        :return:
        """
        pass

    @abstractmethod
    def summa(self, i):
        """
        Абстрактный метод вычисления суммы первых i членов прогрессии
        :param i: номер элемента прогрессии
        :return:
        """
        pass


# Создание класса-потомка c реализацией абстрактных методов базового класса
class Arithmetic_Progression(Progression):

    # Реализация абстрактного метода calculate_element
    def calculate_element(self, i):
        """
        Метод вычисления i-ого элемента арифметической прогрессии
        :param i: номер элемента арифметической прогрессии
        :return: i-ый элемент арифметической прогрессии
        """
        Ai = self.elem + self.d * (i - 1)
        return Ai

    # Реализация абстрактного метода summa
    def summa(self, i):
        """
        Вычисление суммы первых i элементов арифметической прогрессии
        :param i: i-ый элемент арифметической прогрессии
        :return: Сумма первых i элементов арифметической прогрессии
        """
        s = ((self.elem + self.calculate_element(i)) * i) / 2
        return s


# Создание класса-потомка c реализацией абстрактных методов базового класса
class Geometric_Progression(Progression):

    # Реализация абстрактного метода calculate_element
    def calculate_element(self, i):
        """
        Метод вычисления i-ого элемента геометрической прогрессии
        :param i: номер элемента геометрической прогрессии
        :return: i-ый элемент геометрической прогрессии
        """
        Bi = self.elem * (self.d ** (i - 1))
        return Bi

    # Реализация абстрактного метода summa
    def summa(self, i):
        """
        Вычисление суммы первых i элементов геометрической прогрессии
        :param i: i-ый элемент геометрической прогрессии
        :return: Сумма первых i элементов геометрической прогрессии
        """
        s = (self.calculate_element(i) * self.d - self.elem) / (self.d - 1)
        return s


# Создание объектов классов-потомков,
# вызов на этих объектах, реализованных абстрактных методов

p1 = Arithmetic_Progression(2, 5)
# Вычисление значения 16-ого элемента арифметической прогрессии
print(p1.calculate_element(16))

p2 = Arithmetic_Progression(5, 10)
# Вычисление суммы первых 8 элементов арифметической прогрессии
print(p2.summa(8))

print('*'*40)

b1 = Geometric_Progression(8, 0.5)
# Вычисление значения 5-ого элемента геометрической прогрессии
print(b1.calculate_element(5))
# Вычисление суммы первых 5 элементов геометрической прогрессии
print(b1.summa(5))

