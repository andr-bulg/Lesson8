"""
Внести изменения в созданный класс "Point" следующим образом:
- динамические свойства класса “Point” должны иметь модификатор доступа protected;
- определить методы getter и setter для свойств с модификатором
  доступа protected;
- любое взаимодействие с protected свойствами должно производиться
  посредством соответствующих методов getter и setter.

Продемонстрировать работу измененных классов.
"""

from math import sqrt

class Point:

    # Статические свойства
    count_point_X = 0  # количество точек, лежащих на оси X
    count_point_Y = 0  # количество точек, лежащих на оси Y
    count_point_0 = 0  # количество точек, совпадающих с началом координат


    # Переопределение конструктора
    def __new__(cls, *args, **kwargs):
        print("Объект класса Point был создан!")
        return super().__new__(cls)

    # Определение динамических свойств класса через инициализатор
    def __init__(self, x, y):
        """
        Инициализатор класса “Point”
        :param x: координата точки по оси X
        :param y: координата точки по оси Y
        """
        self.set_x(x)
        self.set_y(y)

    # Применение классовых и статических методов внутри инициализатора
        if self.check_point_0(x, y):
            Point.add_count_point_0()
        elif self.check_point_y(x, y):
            Point.add_count_point_y()
        elif self.check_point_x(x, y):
            Point.add_count_point_x()

        print(f"Объект класса Point имеет координаты X={x}, Y={y}.")

    # Переопределение деструктора
    def __del__(self):
        print(f"Объект класса Point с координатами X={self.get_x()}, Y={self.get_y()} удалён!")

    # Методы getter для свойств x и y, которые возвращают значения этих свойств
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


    # Методы setter для свойств x и y, которые устанавливают значения этих свойств
    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y


    # Добавление классовых методов
    @classmethod
    def add_count_point_x(cls):
        """
        Метод, увеличивающий на 1 количество точек, лежащих на оси X
        """
        cls.count_point_X += 1

    @classmethod
    def add_count_point_y(cls):
        """
        Метод, увеличивающий на 1 количество точек, лежащих на оси Y
        """
        cls.count_point_Y += 1

    @classmethod
    def add_count_point_0(cls):
        """
        Метод, увеличивающий на 1 количество точек, совпадающих с началом координат
        """
        cls.count_point_0 += 1


    # Добавление статических методов
    @staticmethod
    def check_point_x(x, y):
        """
        Метод, проверяющий лежит ли точка на оси X
        :param x: координата точки по оси X
        :param y: координата точки по оси Y
        :return: True или False
        """
        if x != 0 and y == 0:
            return True
        return False

    @staticmethod
    def check_point_y(x, y):
        """
        Метод, проверяющий лежит ли точка на оси Y
        :param x: координата точки по оси X
        :param y: координата точки по оси Y
        :return: True или False
        """
        if x == 0 and y != 0:
            return True
        return False

    @staticmethod
    def check_point_0(x, y):
        """
        Метод, проверяющий лежит ли точка в начале координат
        :param x: координата точки по оси X
        :param y: координата точки по оси Y
        :return: True или False
        """
        if x == 0 and y == 0:
            return True
        return False


    # Определение методов уровня класса

    def moving_point_to_x(self, x):
        """
        Метод перемещения точки по оси X
        :param x: координата точки по оси X
        """
        self.set_x(x)

    def moving_point_to_y(self, y):
        """
        Метод перемещения точки по оси Y
        :param y: координата точки по оси Y
        """
        self.set_y(y)

    def distance_to_0(self):
        """
        Метод определения расстояния от текущей точки до начала координат
        :return: Расстояние от текущей точки до начала координат
        """
        res = sqrt((0 - self.get_x()) ** 2 + (0 - self.get_y()) ** 2)
        return round(res, 2)

    def distance_to_some_point(self, x, y):
        """
        Метод, вычисляющий расстояние от текущей до заданной точки
        :param x: координата заданной точки по оси X
        :param y: координата заданной точки по оси Y
        :return: Расстояние от текущей до заданной точки
        """
        res = sqrt((x - self.get_x()) ** 2 + (y - self.get_y()) ** 2)
        return round(res, 2)

    def match_points(self, x, y):
        """
        Метод, выполняющий сравнение на совпадение и несовпадение с заданной точкой
        :param x: координата заданной точки по оси X
        :param y: координата заданной точки по оси Y
        :return: True или False
        """
        if self.get_x() == x and self.get_y() == y:
            return True
        return False

    def print_info(self):
        """
        Метод вывода информации о точке на экран
        """
        print("Объект класса Point, имеющий координаты {}, {}.".format(self.get_x(), self.get_y()))


# Демонстрация работы класса Point и всех его методов

# Создание объектов класса Point
p1 = Point(1, 3)
p2 = Point(0, 0)   # Точка лежит в начале координат
p3 = Point(0, 10)  # Точка лежит на оси Y
p4 = Point(-5, 0)  # Точка лежит на оси X

print()

print("Количество точек, лежащих на оси X:", Point.count_point_X)
print("Количество точек, лежащих на оси Y:", Point.count_point_Y)
print("Количество точек, совпадающих с началом координат:", Point.count_point_0)

print()

# Проверка работы статических методов

# Точка находится/не находится в начале координат
print(p2.check_point_0(p2.get_x(), p2.get_y()))
print(p1.check_point_0(p1.get_x(), p1.get_y()))

# Точка лежит/не лежит на оси Y
print(p3.check_point_y(p3.get_x(), p3.get_y()))
print(p1.check_point_y(p1.get_x(), p1.get_y()))

# Точка лежит/не лежит на оси X
print(p4.check_point_x(p4.get_x(), p4.get_y()))
print(p1.check_point_x(p1.get_x(), p1.get_y()))

print()

# Вызов методов уровня класса

p1.moving_point_to_x(10)
p1.moving_point_to_y(12)
print("X={}, Y={}".format(p1.get_x(), p1.get_y()))

print(f"Расстояние точки ({p1.get_x()}, {p1.get_y()}) до начала координат составляет", p1.distance_to_0())

print(f"Расстояние точки ({p1.get_x()}, {p1.get_y()}) до заданной точки равно", p1.distance_to_some_point(-40, -60))

print("Результат проверки на совпадение с заданной точкой:", p1.match_points(10, 12))
print("Результат проверки на совпадение с заданной точкой:", p1.match_points(38, 49))

for el in [p1, p2, p3, p4]:
    el.print_info()

print()

