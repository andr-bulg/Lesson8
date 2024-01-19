"""
Определите класс “Прямая” со свойствами:
координаты двух точек (x1, y1) и (x2, y2), и методами:
вывод уравнения прямой и определение точек пересечения с осями координат.
"""

class Straight:
    x1 = 3
    y1 = 0
    x2 = 0
    y2 = -5

    def straight_line(self):
        print("Вывод уравнения прямой:")
        print(f"(x-{self.x1})/{self.x2 - self.x1} = (y - {self.y1})/{self.y2 - self.y1}")

    def intersection(self):
        if self.x1 == 0 and self.x1 != self.x2:
            print(f'Пересечение прямой с осью Y будет в точке y={self.y1}')
        elif self.y1 == 0 and self.y1 != self.y2:
            print(f'Пересечение прямой с осью X будет в точке x={self.x1}')

        if self.x2 == 0 and self.x2 != self.x1:
            print(f'Пересечение прямой с осью Y будет в точке y={self.y2}')
        elif self.y2 == 0 and self.y2 != self.y1:
            print(f'Пересечение прямой с осью Y будет в точке y={self.x2}')

        if self.x1 != 0 and self.x2 != 0 and self.y1 != 0 and self.y2 != 0:
            print(f"Пересечения с осями координат у точек {self.x1, self.y1} и {self.x2, self.y2} - нет")

s = Straight()
s.straight_line()

s.intersection()


