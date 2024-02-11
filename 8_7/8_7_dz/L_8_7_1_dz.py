"""
Создать класс “Четырехугольник”, свойства - координаты 4-х точек.
Предусмотреть в классе методы проверки существования четырехугольника*,
вычисления и вывода сведений о фигуре - длины сторон, диагонали, периметр, площадь.

Создать производный класс “Параллелограмм”.
Предусмотреть в классе проверку, является ли фигура параллелограммом.

Написать программу, демонстрирующую работу с классом:
дано N четырехугольников и M параллелограммов,
найти среднюю площадь N четырехугольников и параллелограммы
с наименьшей и наибольшей площадями.
"""

from math import sqrt

class Quadrilateral:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.__A = (x1, y1)
        self.__B = (x2, y2)
        self.__C = (x3, y3)
        self.__D = (x4, y4)

# Геттеры для получкения точек с координатами
    def get_point_A(self):
        return self.__A

    def get_point_B(self):
        return self.__B

    def get_point_C(self):
        return self.__C

    def get_point_D(self):
        return self.__D

    def length_side(self, P1, P2):
        """
        Вычисление длины по координатам двух точек
        :param P1: первая точка
        :param P2: вторая точка
        :return: длина стороны четырёхугольника
        """
        length = round(sqrt((P2[0] - P1[0]) ** 2 + (P2[1] - P1[1]) ** 2), 2)
        return length

    def ABCD(self):
        """
        Вычисление длин сторон четырёхугольника
        :return:
        """
        AB = self.length_side(self.get_point_A(), self.get_point_B())
        BC = self.length_side(self.get_point_B(), self.get_point_C())
        CD = self.length_side(self.get_point_C(), self.get_point_D())
        AD = self.length_side(self.get_point_A(), self.get_point_D())
        return AB, BC, CD, AD


    def quadrilateral_exists(self):
        """
        Функция проверки существования четырёхугольника
        :return:
        """
        if (self.ABCD()[0] < self.ABCD()[1] + self.ABCD()[2] + self.ABCD()[3]) \
                and (self.ABCD()[1] < self.ABCD()[0] + self.ABCD()[2] + self.ABCD()[3]) \
                and (self.ABCD()[2] < self.ABCD()[0] + self.ABCD()[1] + self.ABCD()[3]) \
                and (self.ABCD()[3] < self.ABCD()[0] + self.ABCD()[1] + self.ABCD()[2]):
            return True

        return False

    def perimetr_quadrilateral(self):
        """
        Вычисление периметра четырёхугольника
        :return:
        """
        p = self.ABCD()[0] + self.ABCD()[1] + self.ABCD()[2] + self.ABCD()[3]
        return p

    def area_quadrilateral(self):
        "Вычисление площади четырёхугольника (работает для квадрата или прямоугольника)"
        s = self.ABCD()[0] * self.ABCD()[1]
        return s

q1 = Quadrilateral(-1, 3, 2, 3, 2, -1, -1, -1)

# A = -1, 3
# B = 2, 3
# C = 2, -1
# D = -1, -1

print(q1.get_point_A()[0], q1.get_point_A()[1])
print(q1.length_side(q1.get_point_A(), q1.get_point_B()))
print(q1.ABCD())

if q1.quadrilateral_exists():
    print("Четырёхугольник существует")
else:
    print("Четырёхугольника не существует")

print(q1.perimetr_quadrilateral())
print(q1.area_quadrilateral())

