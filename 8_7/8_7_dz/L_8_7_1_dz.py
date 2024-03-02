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
        "Инициализатор объекта четырёхугольник"

        self.__A = (x1, y1)     # private свойство
        self.__B = (x2, y2)     # private свойство
        self.__C = (x3, y3)     # private свойство
        self.__D = (x4, y4)     # private свойство

# Геттеры для получения точек с координатами четырёхугольника
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
        :return: кортеж со сторонами четырёхугольника
        """
        AB = self.length_side(self.get_point_A(), self.get_point_B())
        BC = self.length_side(self.get_point_B(), self.get_point_C())
        CD = self.length_side(self.get_point_C(), self.get_point_D())
        AD = self.length_side(self.get_point_A(), self.get_point_D())
        return AB, BC, CD, AD


    def quadrilateral_exists(self):
        """
        Метод проверки существования четырёхугольника
        :return: True или False
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
        :return: периметр четырёхугольника
        """
        p = self.ABCD()[0] + self.ABCD()[1] + self.ABCD()[2] + self.ABCD()[3]
        return p

    def area_quadrilateral(self):
        """
        Вычисление площади четырёхугольника (работает для квадрата или прямоугольника)
        :return: площадь четырёхугольника
        """
        s = self.ABCD()[0] * self.ABCD()[1]
        return s

    def giagonal_quadrilateral(self):
        """
        Вычисление диагонали четырёхугольника
        :return: диагональ четырёхугольника
        """
        d = round(sqrt(self.ABCD()[0] ** 2 + self.ABCD()[1] ** 2), 2)
        return d

    def get_info(self):
        """
        Вывод информации о четырёхугольнике
        :return:
        """
        print(f"Четырёхугольник с периметром {self.perimetr_quadrilateral()} и площадью {self.area_quadrilateral()}")
        print(f"имеет стороны: {self.ABCD()[0]}, {self.ABCD()[1]}, {self.ABCD()[2]}, {self.ABCD()[3]} и диагональ {self.giagonal_quadrilateral()}.")

class Parallelogram(Quadrilateral):
    def parallelogram_exists(self):
        """
        Метод проверки существования параллелограмма
        :return: True или False
        """
        if self.ABCD()[0] == self.ABCD()[2] and self.ABCD()[1] == self.ABCD()[3]:
            return True

        return False


# Создание первого четырёхугольника
q1 = Quadrilateral(-1, 3, 2, 3, 2, -1, -1, -1)

print(q1.get_point_A()[0], q1.get_point_A()[1])
print(q1.length_side(q1.get_point_A(), q1.get_point_B()))
print(q1.ABCD())

if q1.quadrilateral_exists():
    print("Четырёхугольник существует")
else:
    print("Четырёхугольника не существует")

print(q1.perimetr_quadrilateral())
print(q1.area_quadrilateral())
print(q1.giagonal_quadrilateral())
q1.get_info()
print()

# Создание второго четырёхугольника
q2 = Quadrilateral(0, 2, 2, 2, 2, 0, 0, 0)
q2.get_info()
print()

# Создание первого параллелограмма
p1 = Parallelogram(-2, 4, 2, 4, 1, -1, -3, -1)
p1.parallelogram_exists()
if p1.parallelogram_exists():
    print("Параллелограмм существует")
else:
    print("Параллелограмма не существует")

# Создание второго параллелограмма
p2 = Parallelogram(-1, 3, 1, 3, 0, 1, -2, 1)
print(p2.parallelogram_exists())


# Список четырёхугольников
quadrilaterals = [q1, q2]

# Получение списка, состоящего из площадей объектов класса Quadrilateral
q_s = list(map(lambda q: q.area_quadrilateral(), quadrilaterals))
if len(q_s) > 1:
    print(f"Средняя площадь {len(q_s)} четырёхугольников равна:")
    print(round(sum(q_s) / len(q_s), 2))

# Список параллелограммов
parallelograms = [p1, p2]

# Получение объекта класса Parallelogram с минимальной площадью
min_p_s = min(parallelograms, key=lambda p: p.area_quadrilateral())
# Получение объекта класса Parallelogram с максимальной площадью
max_p_s = max(parallelograms, key=lambda p: p.area_quadrilateral())

print("Параллелограмм с минимальной площадью это:")
min_p_s.get_info()
print()
print("Параллелограмм с максимальной площадью это:")
max_p_s.get_info()

