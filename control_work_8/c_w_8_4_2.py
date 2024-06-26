"""
Создать базовый абстрактный класс “Array” (массив)
с методами сложения и поэлементной обработки.
Определить производные классы “AndArray” и “OrArray”.
В первом классе операция сложения реализуется как пересечение множеств,
а поэлементная обработка представляет собой извлечение квадратного корня.
Во втором классе операция сложения реализуется как объединение,
а поэлементная обработка - вычисление логарифма.

Решите самостоятельно, какими свойствами будет обладать каждый из классов,
и какие методы следует определить как абстрактные.
"""

# Импорт абстрактного базового класса и декоратора
from abc import ABC, abstractmethod

from math import sqrt, log

# Определение абстрактного базового класса Array
class Array():

    def __init__(self, spisok_1, spisok_2):
        """
        Инициализатор абстрактного базового класса
        :param spisok_1: первый массив (список)
        :param spisok_2: второй массив (список)
        """
        self.spisok_1 = spisok_1
        self.spisok_2 = spisok_2


    @abstractmethod
    def addition(self):
        """
        Абстрактный метод для сложения двух массивов
        """
        pass

    @abstractmethod
    def processing(self):
        """
        Абстрактный метод для поэлементной обработки массивов
        """
        pass


# Создание класса-потомка c реализацией абстрактных методов базового класса
class AndArray(Array):

    def addition(self):
        """
        Метод для выполнения пересечения множеств
        :return: Множество, состоящее из общих элементов заданных массивов
        """
        # Преобразование списков во множества,
        # чтобы устранить в них повторяющиеся элементы
        s1 = set(self.spisok_1)
        s2 = set(self.spisok_2)
        return s1.intersection(s2)

    def processing(self):
        """
        Метод для извлечения квадратного корня из элементов заданных массивов
        """
        temp = [round(sqrt(el), 2) for el in self.spisok_1]
        print(temp)
        temp = [round(sqrt(el), 2) for el in self.spisok_2]
        print(temp)


# Создание класса-потомка c реализацией абстрактных методов базового класса
class OrArray(Array):

    def addition(self):
        """
        Метод для выполнения объединения множеств
        :return: Множество со всеми уникальными элементами заданных массивов
        """
        # Преобразование списков во множества,
        # чтобы устранить в них повторяющиеся элементы
        s1 = set(self.spisok_1)
        s2 = set(self.spisok_2)
        return s1.union(s2)

    def processing(self):
        """
        Метод для вычисления (натурального) логарифма из элементов заданных массивов
        """
        temp = [round(log(el), 2) for el in self.spisok_1]
        print(temp)
        temp = [round(log(el), 2) for el in self.spisok_2 if el > 0]
        print(temp)


# Демонстрация работы классов-потомков AndArray и OrArray,
# и всех их абстрактных методов

spisok_1 = [1, 1, 3, 4, 6]
spisok_2 = [0, 1, 4, 4, 8, 9]

# Создание объекта класса AndArray
aa_1 = AndArray(spisok_1, spisok_2)

print("Пересечение множеств:", aa_1.addition())

print("Списки значений квадратных корней, извлекаемых из элементов заданных массивов:")
aa_1.processing()

print()

# Создание объекта класса OrArray
oa_1 = OrArray(spisok_1, spisok_2)

print("Объединение множеств:", oa_1.addition())

print("Списки (натуральных) логарифмов из элементов заданных массивов:")
oa_1.processing()

