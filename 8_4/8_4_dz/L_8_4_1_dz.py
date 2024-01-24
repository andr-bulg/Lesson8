"""
Изменить класс “Прямая” следующим образом:
- все статические свойства классов должны изменяться только внутри классовых методов;
- выделить один или несколько вспомогательных методов (если это не было сделано ранее)
  и оформить их в виде статических методов.
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


    def create_straight(self, x1, y1, x2, y2):
        """
        Создание прямой по координатам двух точек
        :param x1: координата x1 первой точки
        :param y1: координата y1 первой точки
        :param x2: координата x2 второй точки
        :param y2: координата y2 второй точки
        :return:
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        # Было обращение через класс Straight.count_straight += 1
        # Теперь используется классовый метод
        Straight.func_count_straight()


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
        print(Straight.straight_line(self.x1, self.y1, self.x2, self.y2))


    def intersection(self):
        """
        Определение точек пересечения с осями координат
        :return:
        """
        if self.x1 == 0 and self.x1 != self.x2:
            print(f'Пересечение прямой с осью Y будет в точке y={self.y1}')
        elif self.y1 == 0 and self.y1 != self.y2:
            print(f'Пересечение прямой с осью X будет в точке x={self.x1}')

        if self.x2 == 0 and self.x2 != self.x1:
            print(f'Пересечение прямой с осью Y будет в точке y={self.y2}')
        elif self.y2 == 0 and self.y2 != self.y1:
            print(f'Пересечение прямой с осью Y будет в точке y={self.x2}')

        if self.x1 == -self.x2 and self.y1 == -self.y2:
            print("Прямая проходит через начало координат")
        elif self.x1 != 0 and self.x2 != 0 and self.y1 != 0 and self.y2 != 0:
            print(f"Пересечения с осями координат у точек {self.x1, self.y1} и {self.x2, self.y2} - нет")


        if self.y1 == self.y2 and self.y1 != 0 and self.y2 != 0:
            Straight.count_parallel_straight += 1
        elif self.x1 == self.x2 and self.x1 != 0 and self.x2 != 0:
            # Было обращение через класс Straight.count_parallel_straight += 1
            # Теперь используется классовый метод
            Straight.func_count_parallel_straight()

        if (self.x1 == 0 and self.y1 == 0) or (self.x2 == 0 and self.y2 == 0):
            Straight.count_straight_origin_of_coordinates += 1
        elif self.x1 == -self.x2 and self.y1 == -self.y2:
            # Было обращение через класс Straight.count_straight_origin_of_coordinates += 1
            # Теперь используется классовый метод
            Straight.func_count_straight_origin_of_coordinates()

# Создание объекта s класса Straight
s = Straight()

# Создание прямой по координатам двух точек, другими словами
# объекту s задаются динамические свойства в виде координат двух точек
s.create_straight(1, 1, -1, -1)

print('Общее количество прямых:', Straight.count_straight)

# Вывод уравнения прямой
s.print_straight_line()

# Определение точек пересечения с осями координат
s.intersection()

print('Количество прямых, параллельных осям координат:', Straight.count_parallel_straight)
print('Количество прямых, проходящих через точку начала координат:', Straight.count_straight_origin_of_coordinates)

