"""
Измените класс “Прямая” следующим образом:
* свойства класса - координаты двух точек (x1, y1) и (x2, y2) - должны быть
  динамическими и задаваться внутри нового метода, задающего прямую;
* добавьте 3 статических свойства - количество прямых, параллельных осям координат,
  и прямых, проходящих через точку начала координат
  (проверки должны осуществляться в соответствующих методах).
"""

class Straight:
    # Статические свойства класса Straight
    count_straigt = 0                       # Общее количество прямых
    count_parallel_straight = 0             # Количество прямых, параллельных осям координат
    count_straigt_origin_of_coordinates = 0  # Количество прямых,
                                             # проходящих через точку начала координат

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

        Straight.count_straigt += 1

    def straight_line(self):
        """
        Вывод уравнения прямой
        :return:
        """
        print("Уравнение прямой имеет следующий вид:")
        print(f"(x-{self.x1})/{self.x2 - self.x1} = (y - {self.y1})/{self.y2 - self.y1}")

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
            Straight.count_parallel_straight += 1

        if (self.x1 == 0 and self.y1 == 0) or (self.x2 == 0 and self.y2 == 0):
            Straight.count_straigt_origin_of_coordinates += 1
        elif self.x1 == -self.x2 and self.y1 == -self.y2:
            Straight.count_straigt_origin_of_coordinates += 1

# Создание объекта s класса Straight
s = Straight()

# Создание прямой по координатам двух точек, другими словами
# объекту s задаются динамические свойства в виде координат двух точек
s.create_straight(1, 1, -1, -1)

print('Общее количество прямых:', Straight.count_straigt)

# Вывод уравнения прямой
s.straight_line()

# Определение точек пересечения с осями координат
s.intersection()

print('Количество прямых, параллельных осям координат:', Straight.count_parallel_straight)
print('Количество прямых, проходящих через точку начала координат:', Straight.count_straigt_origin_of_coordinates)

