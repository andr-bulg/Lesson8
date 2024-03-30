"""
Создать класс “Pair” (пара чисел) со свойствами: числа A и B,
и методами: изменение чисел, вычисление их произведения и суммы.

Определить производный класс “Right Triangle” (прямоугольный треугольник)
со свойствами: катеты A и B, и методами: вычисление гипотенузы и площади треугольника,
вывод информации о фигуре на экран.

Продемонстрировать работу класса-наследника и всех его методов.
"""

from math import sqrt

class Pair():

    def __init__(self, A, B):
        """
        Инициализатор класса "Pair"
        :param A: первое число
        :param B: второе число
        """
        self.A = A
        self.B = B


    def change_number(self, new_A, new_B):
        """
        Метод, изменяющий значения двух чисел
        :param new_A: новое значение первого числа
        :param new_B: новое значение второго числа
        """
        self.A = new_A
        self.B = new_B

    def calculate_sum(self):
        """
        Метод для вычисления суммы двух чисел
        :return: Сумма двух чисел
        """
        return self.A + self.B

    def calculate_product(self):
        """
        Метод для вычисления произведения двух чисел
        :return: Произведение двух чисел
        """
        return self.A * self.B


class Right_Triangle(Pair):

    def calculate_hypot(self):
        """
        Метод для вычисления гипотенузы прямоугольного треугольника
        :return: Значение гипотенузы прямоугольного треугольника
        """
        res = round(sqrt(self.A ** 2 + self.B ** 2), 2)
        return res

    def calculate_area(self):
        """
        Метод для вычисления площади прямоугольного треугольника
        :return: Площадь прямоугольного треугольника
        """
        res = 0.5 * (self.A + self.B)
        return res

    def print_info(self):
        """
        Метод, выводящий информацию о прямоугольном треугольнике
        """
        print(f"Прямоугольный треугольник имеет стороны {float(self.A)}, {float(self.B)} и {self.calculate_hypot()}.")


# Демонстрация работы класса-наследника Right_Triangle и всех его методов

r_t = Right_Triangle(4, 3)
r_t.print_info()
print()

# Изменение значения двух катетов
r_t.change_number(30, 40)

print("Сумма двух катетов равна", r_t.calculate_sum())
print("Произведение двух катетов равно", r_t.calculate_product())
print("Значение гипотенузы прямоугольного треугольника равно", r_t.calculate_hypot())
print("Площадь прямоугольного треугольника равна", r_t.calculate_area())
r_t.print_info()

