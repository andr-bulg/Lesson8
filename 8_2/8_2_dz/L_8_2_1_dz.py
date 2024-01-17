"""
Определите класс “Прямая” со свойствами:
координаты двух точек (x1, y1) и (x2, y2), и методами:
вывод уравнения прямой и определение точек пересечения с осями координат.
"""

class Straight:
    x1 = 3
    y1 = 8
    x2 = 0
    y2 = -5

    def straight_line(self):
        print("Вывод уравнения прямой:")
        print(f"(x-{self.x1})/{self.x2 - self.x1} = (y - {self.y1})/{self.y2 - self.y1}")

    def intersection(self, x, y):
        if x == 0:
            print(f'Пересечение с осью Y будет в точке y={y}')

        elif y == 0:
            print(f'Пересечение с осью X будет в точке x={x}')

        else:
            print(f"Пересечения с осями координат у точки {x, y} нет")

s = Straight()
s.straight_line()

s.intersection(s.x1, s.y1)
s.intersection(s.x2, s.y2)

