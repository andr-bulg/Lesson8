"""
Изменить созданный ранее класс “Прямая” следующим образом:
- установить для одного из динамических свойств класса модификатор доступа protected,
  а для остальных (если имеются) - модификатор доступа private;
- добавить соответствующие методы getter и setter.
"""


class Straight:
    # Статические свойства класса Straight
    count_straight = 0                       # Общее количество прямых
    count_parallel_straight = 0             # Количество прямых, параллельных осям координат
    count_straight_origin_of_coordinates = 0  # Количество прямых,
                                             # проходящих через точку начала координат

    # Определение классового метода для изменения общего количества прямых
    @classmethod
    def func_count_straight(cls):
        cls.count_straight += 1

    # Определение классового метода для изменения общего количества прямых,
    # параллельных осям координат
    @classmethod
    def func_count_parallel_straight(cls):
        cls.count_parallel_straight += 1

    # Определение классового метода для изменения общего количества прямых,
    # проходящих через точку начала координат
    @classmethod
    def func_count_straight_origin_of_coordinates(cls):
        cls.count_straight_origin_of_coordinates += 1


    # Добавление конструктора
    def __new__(cls, *args, **kwargs):
        print("Новый объект класса Straight создан!")
        return super().__new__(cls)

    # Преобразование метода create_straight(self, x1, y1, x2, y2) в инициализатор
    def __init__(self, x1, y1, x2, y2):
        """
        Инициализация исходных свойств объекта класса Straight
        :param x1: координата x1 первой точки
        :param y1: координата y1 первой точки
        :param x2: координата x2 второй точки
        :param y2: координата y2 второй точки
        :return:
        """
        # self._x1 = x1    protected
        # self._y1 = y1    protected
        # self.__x2 = x2   private
        # self.__y2 = y2   private

        # Установка свойств объекта через setter
        self.set_x1(x1)  # protected
        self.set_y1(y1)  # protected
        self.set_x2(x2)  # private
        self.set_y2(y2)  # private

        # Было обращение через класс Straight.count_straight += 1
        # Теперь используется классовый метод
        Straight.func_count_straight()
        print(f"Исходные свойства объекта {self.get_x1(), self.get_y1(), self.get_x2(), self.get_y2()} заданы!")

    # Добавление деструктора
    def __del__(self):
        print(f"Объект {self.get_x1(), self.get_y1(), self.get_x2(), self.get_y2()} был удалён!")


    # Методы getter для свойств x1, y1, x2, y2, которые возвращают их значения
    def get_x1(self):
        return self._x1

    def get_y1(self):
        return self._y1

    def get_x2(self):
        return self.__x2

    def get_y2(self):
        return self.__y2


    # Методы setter для свойств x1, y1, x2, y2, устанавливающие их значения
    def set_x1(self, x):
        self._x1 = x

    def set_y1(self, y):
        self._y1 = y

    def set_x2(self, x):
        self.__x2 = x

    def set_y2(self, y):
        self.__y2 = y


    # Создание статического метода как вспомогательного
    @staticmethod
    def straight_line(x1, y1, x2, y2):
        """
        Формирование уравнения прямой
        :param x1: координата x1 первой точки
        :param y1: координата y1 первой точки
        :param x2: координата x2 второй точки
        :param y2: координата y2 второй точки
        :return: уравнение прямой в виде f-строки
        """
        return f"(x-{x1})/{x2 - x1} = (y - {y1})/{y2 - y1}"

    def print_straight_line(self):
        """
        Вывод на печать уравнения прямой,
        полученного из статического метода straight_line()
        :return:
        """
        print("Уравнение прямой имеет следующий вид:")
        print(Straight.straight_line(self.get_x1(), self.get_y1(), self.get_x2(), self.get_y2()))


    def intersection(self):
        """
        Определение точек пересечения с осями координат
        :return:
        """
        if self.get_x1() == 0 and self.get_x1() != self.get_x2():
            print(f'Пересечение прямой с осью Y будет в точке y={self.get_y1()}')
        elif self.get_y1() == 0 and self.get_y1() != self.get_y2():
            print(f'Пересечение прямой с осью X будет в точке x={self.get_x1()}')

        if self.get_x2() == 0 and self.get_x2() != self.get_x1():
            print(f'Пересечение прямой с осью Y будет в точке y={self.get_y2()}')
        elif self.get_y2() == 0 and self.get_y2() != self.get_y1():
            print(f'Пересечение прямой с осью Y будет в точке y={self.get_x2()}')

        if self.get_x1() == -self.get_x2() and self.get_y1() == -self.get_y2():
            print("Прямая проходит через начало координат")
        elif self.get_x1() != 0 and self.get_x2() != 0 and self.get_y1() != 0 and self.get_y2() != 0:
            print(f"Пересечения с осями координат у точек {self.get_x1(), self.get_y1()} и {self.get_x2(), self.get_y2()} - нет")


        if self.get_y1() == self.get_y2() and self.get_y1() != 0 and self.get_y2() != 0:
            Straight.count_parallel_straight += 1
        elif self.get_x1() == self.get_x2() and self.get_x1() != 0 and self.get_x2() != 0:
            # Было обращение через класс Straight.count_parallel_straight += 1
            # Теперь используется классовый метод
            Straight.func_count_parallel_straight()

        if (self.get_x1() == 0 and self.get_y1() == 0) or (self.get_x2() == 0 and self.get_y2() == 0):
            Straight.count_straight_origin_of_coordinates += 1
        elif self.get_x1() == -self.get_x2() and self.get_y1() == -self.get_y2():
            # Было обращение через класс Straight.count_straight_origin_of_coordinates += 1
            # Теперь используется классовый метод
            Straight.func_count_straight_origin_of_coordinates()

# Создание объекта прямая s класса Straight по координатам двух точек, другими словами,
# объекту s задаются динамические свойства в виде координат двух точек

s = Straight(1, 1, -1, -1)

print('Общее количество прямых:', Straight.count_straight)

# Вывод уравнения прямой
s.print_straight_line()

# Определение точек пересечения с осями координат
s.intersection()

print('Количество прямых, параллельных осям координат:', Straight.count_parallel_straight)
print('Количество прямых, проходящих через точку начала координат:', Straight.count_straight_origin_of_coordinates)

# Изменение значения свойств объекта s через сеттеры
s.set_x1(10)
s.set_y1(20)
s.set_x2(-5)
s.set_y2(0)

# Получение свойств объекта s и вывод их на печать через геттеры
print("Новые свойства объекта s класса Straight:")
print(s.get_x1(), s.get_y1(), s.get_x2(), s.get_y2())

