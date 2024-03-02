"""
В созданном классе “Прямоугольная пирамида с прямоугольником в основании”
переопределить методы вычисления площади и вывода информации о фигуре.
Написать программу, демонстрирующую работу с классом:
дано N прямоугольных пирамид с прямоугольником в основании,
найти среднее геометрическое площадей всех пирамид,
а также пирамиды с наибольшей и наименьшей площадями.
"""

from math import sqrt

class Quadrilateral:

    def __init__(self, a, b):
        self.a = a      # public свойство
        self.b = b      # public свойство

    def diagonal_quadrilateral(self):
        """
        Вычисление диагонали прямоугольника
        :return: диагональ прямоугольника
        """
        d = round(sqrt(self.a ** 2 + self.b ** 2), 2)
        return d

    def perimetr_quadrilateral(self):
        """
        Вычисление периметра прямогугольника
        :return: периметр прямоугольника
        """
        p = 2 * self.a + 2 * self.b
        return p

    # Переименование метода area_quadrilateral() в get_area()
    # для его дальнейшего переопределения в классе-потомке (02-03-2024)
    def get_area(self):
        """
        Вычисление площади прямоугольника
        :return: площадь прямоугольника
        """
        s = self.a * self.b
        return s

    # Переименование метода info_about_quadrilateral() в get_info()
    # для его дальнейшего переопределения в классе-потомке (02-03-2024)
    def get_info(self):
        """
        Вывод информации о прямоугольнике
        :return:
        """
        print(f"Прямоугольник со сторонами {self.a}, {self.b} и диагональю {self.diagonal_quadrilateral()}")
        print(f"имеет периметр {self.perimetr_quadrilateral()} и площадь {self.get_area()}.")


class Triangle:

    def __init__(self, a, b, c):
        self.a = a      # public свойство
        self.b = b      # public свойство
        self.c = c      # public свойство

    def perimetr_triangle(self):
        """
        Вычисление периметра треугольника
        :return: периметр треугольника
        """
        p = self.a + self.b + self.c
        return p

    # Переименование метода area_triangle() в get_area()
    # для его дальнейшего переопределения в классе-потомке (02-03-2024)
    def get_area(self):
        """
        Вычисление площади треугольника
        :return: площадь треугольника
        """
        p_2 = self.perimetr_triangle() / 2
        s = round(sqrt(p_2 * (p_2 - self.a) * (p_2 - self.b) * (p_2 - self.c)), 2)
        return s

    def right_anled_triangle(self):
        """
        Проверка является ли треугольник прямоугольным
        :return: True или False
        """
        if self.a ** 2 == self.b ** 2 + self.c ** 2 \
                or self.c ** 2 == self.a ** 2 + self.b ** 2 \
                or self.b ** 2 == self.a ** 2 + self.c ** 2:
            return True

        return False

    # Переименование метода info_about_triangle() в get_info()
    # для его дальнейшего переопределения в классе-потомке (02-03-2024)
    def get_info(self):
        """
        Вывод информации о треугольнике
        :return:
        """
        print(f"Треугольник со сторонами {self.a}, {self.b} и {self.c}")
        print(f"имеет периметр {self.perimetr_triangle()} и площадь {self.get_area()}.")


class Rectangular_pyramid(Quadrilateral, Triangle):

    def __init__(self, a, b, h):
        # Инициализация свойств объекта через родительский класс.
        # Функция super() возвращает объект родительского класса (суперкласса),
        # на котором вызывается инциализатор родительского класса,
        # задающий свойста объекта класса-потомка.
        super().__init__(a, b)
        self.h = h      # public свойство

    def volume_pyramid(self):
        """
        Вычисление объёма прямоугольной пирамиды
        :return: объём прямоугольной пирамиды
        """
        v = round((self.get_area() * self.h) / 3, 2)
        return v

    # Создание метода get_area() для его переопределения
    # в этом классе-потомке (02-03-2024)
    def get_area(self):
        """
        Вычисление площади прямогугольной пирамиды
        :return: площадь прямоугольной пирамиды
        """
        s1 = self.a * self.b  # площадь основания пирамиды
        s2 = (self.perimetr_quadrilateral() / 2) * self.h  # площадь боковой поверхности
        return round(s1 + s2, 2)

    # Переименование метода info_about_pyramid() в get_info()
    # для его переопределения в этом классе-потомке (02-03-2024)
    def get_info(self):
        """
        Вывод информации о прямоугольной пирамиде
        :return:
        """
        print(f"Прямоугольная пирамида с длинами сторон основания "
              f"{self.a}, {self.b} и высотой {self.h},")
        print(f"которая имеет объём {self.volume_pyramid()}")


# Поиск трёх прямоугольников с наименьшей площадью

# q1 = Quadrilateral(5, 60)
# q2 = Quadrilateral(10, 20)
# q3 = Quadrilateral(2, 3)
# q4 = Quadrilateral(15, 6)
# q5 = Quadrilateral(80, 4)
#
# quadrilaterals = [q1, q2, q3, q4, q5]
# quadrilateral_areas = [el.get_area() for el in quadrilaterals]
# quadrilateral_areas.sort()
#
# print("Три прямоугольника с наименьшей площадью:")
# for el in quadrilateral_areas[:3]:
#     for el2 in quadrilaterals:
#         if el2.get_area() == el:
#             el2.get_info()
#
# print()


# Поиск прямоугольных треугольников

# t1 = Triangle(7, 4, 9)
# t2 = Triangle(4, 3, 5)
# t3 = Triangle(50, 30, 40)
#
# triangles = [t1, t2, t3]
#
# print("Следующие треугольники являются прямоугольными:")
# for el in triangles:
#     if el.right_anled_triangle():
#         el.get_info()
#
# print()


# Создание объектов класса-наследника
r1 = Rectangular_pyramid(10, 6, 20)
r2 = Rectangular_pyramid(1, 2, 3)
r3 = Rectangular_pyramid(5, 10, 15)
r4 = Rectangular_pyramid(2, 3, 4)
r5 = Rectangular_pyramid(7, 8, 9)

rectangular_pyramids = [r1, r2, r3, r4, r5]

# Поиск пирамид, объём которых отличается от среднего объёма
# всех пирамид не более, чем на 10%.

# rectangular_pyramids = [r1, r2, r3, r4, r5]
# volume_rectangular_pyramids = [el.volume_pyramid() for el in rectangular_pyramids]
# avg_volume = round(sum(volume_rectangular_pyramids) / len(volume_rectangular_pyramids), 2)
#
# print("Пирамиды, объём которых отличается от среднего объёма "
#       "всех пирамид не более, чем на 10%:")
# for el in rectangular_pyramids:
#     if el.volume_pyramid() > avg_volume and el.volume_pyramid() <= 1.1 * avg_volume:
#         el.get_info()


# Вычисление среднего геометрического площадей всех пирамид (02-03-2024)
temp = 1
for el in rectangular_pyramids:
    temp *= el.get_area()

sr_geom = round(temp ** (1/len(rectangular_pyramids)), 2)
print("Среднее геометрическое площадей всех пирамид равно:", sr_geom)
print()

# Получение пирамиды с наибольшей площадью (02-03-2024)
max_p_s = max(rectangular_pyramids, key=lambda p: p.get_area())

# Получение пирамиды с наименьшей площадью (02-03-2024)
min_p_s = min(rectangular_pyramids, key=lambda p: p.get_area())

print(f"Пирамида с наибольшей площадью {max_p_s.get_area()} это:")
max_p_s.get_info()
print()
print(f"Пирамида с наименьшей площадью {min_p_s.get_area()} это:")
min_p_s.get_info()

