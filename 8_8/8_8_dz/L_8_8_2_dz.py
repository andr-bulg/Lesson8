"""
В созданном классе “Равнобедренный треугольник” переопределить методы
вычисления углов и вывода информации о фигуре.
Написать программу, демонстрирующую работу с классами:
дано N равнобедренных треугольников,
вывести треугольники в порядке возрастания их площади.
"""

from math import sqrt, acos, degrees

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.__A = (x1, y1)     # private свойство
        self.__B = (x2, y2)     # private свойство
        self.__C = (x3, y3)     # private свойство

# Геттеры для получения точек с координатами треугольника
    def get_point_A(self):
        return self.__A

    def get_point_B(self):
        return self.__B

    def get_point_C(self):
        return self.__C

    def length_side(self, P1, P2):
        """
        Вычисление длины по координатам двух точек
        :param P1: первая точка
        :param P2: вторая точка
        :return: длина стороны треугольника
        """
        length = round(sqrt((P2[0] - P1[0]) ** 2 + (P2[1] - P1[1]) ** 2), 2)
        return length

    def ABC(self):
        """
        Вычисление длин сторон треугольника
        :return: кортеж со сторонами треугольника
        """
        AB = self.length_side(self.get_point_A(), self.get_point_B())
        BC = self.length_side(self.get_point_B(), self.get_point_C())
        AC = self.length_side(self.get_point_A(), self.get_point_C())
        return AB, BC, AC

    def triangle_exists(self):
        """
        Метод проверки существования треугольника
        :return: True или False
        """
        if (self.ABC()[0] + self.ABC()[1] > self.ABC()[2]) \
                and (self.ABC()[0] + self.ABC()[2] > self.ABC()[1]) \
                and (self.ABC()[1] + self.ABC()[2] > self.ABC()[0]):
            return True

        return False

    def perimetr_triangle(self):
        """
        Вычисление периметра треугольника
        :return: периметр треугольника
        """
        p = self.ABC()[0] + self.ABC()[1] + self.ABC()[2]
        return round(p, 2)

    def area_triangle(self):
        """
        ВЫчисление площади треугольника по трём сторонам
        :return: площадь треугольника
        """
        p_2 = self.perimetr_triangle() / 2
        s = sqrt(p_2 * (p_2 - self.ABC()[0]) * (p_2 - self.ABC()[1]) * (p_2 - self.ABC()[2]))
        return round(s, 2)

    def triangle_angles(self):
        """
        Вычисление углов треугольника
        :return: углы треугольника
        """

        # Вычисление косинусов углов треугольника с последующим их преобразованием
        # в аркосинусы (измерение в радианах)
        ac = acos((self.ABC()[0] ** 2 + self.ABC()[2] ** 2 - self.ABC()[1] ** 2) / (2 * self.ABC()[0] * self.ABC()[2]))
        ab = acos((self.ABC()[0] ** 2 + self.ABC()[1] ** 2 - self.ABC()[2] ** 2) / (2 * self.ABC()[0] * self.ABC()[1]))
        bc = acos((self.ABC()[1] ** 2 + self.ABC()[2] ** 2 - self.ABC()[0] ** 2) / (2 * self.ABC()[1] * self.ABC()[2]))

        # Преобразование значений углов из радианов в градусы
        ac = round(degrees(ac), 2)
        ab = round(degrees(ab), 2)
        bc = round(degrees(bc), 2)

        return ac, ab, bc

    def get_info(self):
        """
        Вывод информации о треугольнике
        :return:
        """
        print(f"Треугольник со сторонами {self.ABC()[0]}, {self.ABC()[1]}, {self.ABC()[2]} "
              f"и углами {self.triangle_angles()[0]}, {self.triangle_angles()[1]}, {self.triangle_angles()[2]},")
        print(f"имеет периметр {self.perimetr_triangle()} и площадь {self.area_triangle()}.")


class Ravnobedr_triangle(Triangle):

    def equilateral_triangle(self):
        """
        Метод, проверяющий является ли треугольник равносторонним
        :return: True или False
        """
        if self.ABC()[0] == self.ABC()[1] and self.ABC()[0] == self.ABC()[2] and self.ABC()[1] == self.ABC()[2]:
            return True

        return False

    def get_mediana(self):
        """
        Вычисление медианы равнобедренного треугольника
        :return: медиана равнобедренного треугольника
        """
        m = round(0.5 * sqrt(4 * self.ABC()[1]**2 - self.ABC()[2]**2), 2)
        return m

    # Переопределение метода из родительского класса (29-02-2024)
    def triangle_angles(self):
        """
        Вычисление углов равнобедренного треугольника
        :return:
        """

        # Вычисление косинусов углов треугольника с последующим их преобразованием
        # в аркосинусы (измерение в радианах)
        ac = acos((self.ABC()[0] ** 2 + self.ABC()[2] ** 2 - self.ABC()[1] ** 2) / (2 * self.ABC()[0] * self.ABC()[2]))
        ab = acos((self.ABC()[0] ** 2 + self.ABC()[1] ** 2 - self.ABC()[2] ** 2) / (2 * self.ABC()[0] * self.ABC()[1]))
        bc = acos((self.ABC()[1] ** 2 + self.ABC()[2] ** 2 - self.ABC()[0] ** 2) / (2 * self.ABC()[1] * self.ABC()[2]))

        # Преобразование значений углов из радианов в градусы
        ac = round(degrees(ac), 2)
        ab = round(degrees(ab), 2)
        bc = round(degrees(bc), 2)

        print(f"Углы равнобедренного треугольника равны: ac={ac}, ab={ab}, bc={bc}")

    # Переопределение метода из родительского класса (29-02-2024)
    def get_info(self):
        """
        Вывод краткой информации о равнобедренном треугольнике
        :return:
        """
        print(f"Равнобедренный треугольник со сторонами {self.ABC()[0]}, {self.ABC()[1]}, {self.ABC()[2]}")


# Создание объектов родительского класса и класса-наследника
t1 = Triangle(-1, 0, 0, 4, 2, 0)
t2 = Ravnobedr_triangle(-2, -1, 0, 2, 2, -1)
t3 = Ravnobedr_triangle(1, 1, 3, 6, 5, 1)
t4 = Ravnobedr_triangle(0, 0, 2, 0, 1, sqrt(3))
t5 = Ravnobedr_triangle(1, 1, 3, 6, 5, 1)
t6 = Triangle(-1, 0, 0, 4, 2, 0)

# Проверка работы двух методов родительского класса
# t1.get_info()
# print('Углы треугольника:', t1.triangle_angles())


# Проверка того, что треугольник является равносторонним
# t4.equilateral_triangle()

# Вызов переопределённого в классе-потомке метода get_info() (29-02-2024)
print("*"*50)
t5.get_info()
# Вызов переопределённого в классе-потомке метода triangle_angles() (29-02-2024)
t5.triangle_angles()
print("*"*50)


# Вывод номеров треугольников с одинаковой площадью
# triangle_areas = [t1.area_triangle(), t2.area_triangle(), t3.area_triangle(),
#                  t4.area_triangle(), t5.area_triangle(), t6.area_triangle()]
# Преобразование списка в множество, чтобы убрать дублирующиеся элементы, если они есть
# triangle_areas_s = set(triangle_areas)

# Список, в котором будут храниться одинаковые площади треугольников
# same_triangle_areas = []

# for el_s in triangle_areas_s:
#     count = 0
#     for el in triangle_areas:
#         if el_s == el:
#             count += 1
#     if count > 1:
#         same_triangle_areas.append(el_s)
#
# for el in same_triangle_areas:
#     print("Треугольники с одинаковой площадью", el, "имеют номера:")
#     for i in range(len(triangle_areas)):
#         if triangle_areas[i] == el:
#             print(i+1)


# Вывод равнобедренного треугольника с наименьшей медианой

# ravnobedr_triangles = [t2, t3, t4, t5]
# min_m = min(ravnobedr_triangles, key=lambda t: t.get_mediana())
# print("Равнобедренный треугольник с наименьшей медианой это:")
# min_m.get_info()

# Вывод равнобедренных треугольников в порядке возрастания их площади (29-02-2024)
ravnobedr_triangles = [t4, t5, t2, t3]
res = sorted(ravnobedr_triangles, key=lambda el: el.area_triangle())
print("Вывод равнобедренных треугольников в порядке возрастания их площади:")
for el in res:
    print("Площадь равнобедренного треугольника:", el.area_triangle())
    el.get_info()
    print()

