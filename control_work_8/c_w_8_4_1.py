"""
Создать базовый абстрактный класс “Pair” (пара чисел)
с арифметическими операциями: сложение, вычитание, умножение и деление.
Определить производный класс “Fuzzy numbers” (нечеткие числа),
реализующий арифметические операции следующим образом:

- A(A-a, A, A+a) + B(B-b, B, B+b) = ((A-a)+(B-b), A+B, (A+a)+(B+b))
- A(A-a, A, A+a) - B(B-b, B, B+b) = ((A-a)-(B-b), A-B, (A+a)-(B+b))
- A(A-a, A, A+a) * B(B-b, B, B+b) = ((A-a)*(B-b), A*B, (A+a)*(B+b))
- A(A-a, A, A+a) / B(B-b, B, B+b) = ((A-a)/(B-b), A/B, (A+a)/(B+b))

Решите самостоятельно, какими свойствами будет обладать каждый из классов,
и какие методы следует определить как абстрактные.
"""

# Импорт абстрактного базового класса и декоратора

from abc import ABC, abstractmethod

# Определение абстрактного базового класса Pair
class Pair(ABC):

    def __init__(self, A, B):
        """
        Инициализатор абстрактного базового класса
        :param A: первое число
        :param B: второе число
        """
        self.A = A
        self.B = B


    @abstractmethod
    def calculate_sum(self):
        """
        Абстрактный метод для сложения двух чисел
        """
        pass

    @abstractmethod
    def calculate_subtraction(self):
        """
        Абстрактный метод для вычитания двух чисел
        """
        pass

    @abstractmethod
    def calculate_product(self):
        """
        Абстрактный метод для умножения двух чисел
        """
        pass

    @abstractmethod
    def calculate_division(self):
        """
        Абстрактный метод для деления двух чисел
        """
        pass


# Создание класса-потомка c реализацией абстрактных методов базового класса
class Fuzzy_numbers(Pair):

    def __init__(self, A, B, a, b):
        """
        Инициализатор класса-потомка Fuzzy_numbers
        :param A: первое нечёткое число
        :param B: второе нечёткое число
        :param a: точка нечёткого числа A
        :param b: точка нечёткого числа B
        """
        # Вызов инициализатора родительского класса на самом классе,
        # чтобы задать свойства объекта A и B. При вызове инициализатора на классе
        # необходимо передать ссылку на объект, параметры которого будут задаваться,
        # поэтому в аргументах указывается параметр self.
        Pair.__init__(self, A, B)
        self.a = a
        self.b = b


    def calculate_sum(self):
        """
        Метод для сложения двух нечётких чисел
        :return: Выражение в виде f-строки
        """
        res = f"A({self.A - self.a}, {self.A}, {self.A + self.a}) + B({self.B - self.b}, {self.B}, {self.B + self.b}) = " \
              f"({(self.A - self.a) + (self.B - self.b)}, {self.A + self.B}, {(self.A + self.a) + (self.B + self.b)})"
        return res

    def calculate_subtraction(self):
        """
        Метод для вычитания двух нечётких чисел
        :return: Выражение в виде f-строки
        """
        res = f"A({self.A - self.a}, {self.A}, {self.A + self.a}) - B({self.B - self.b}, {self.B}, {self.B + self.b}) = " \
              f"({(self.A - self.a) - (self.B - self.b)}, {self.A - self.B}, {(self.A + self.a) - (self.B + self.b)})"
        return res

    def calculate_product(self):
        """
        Метод для умножения двух нечётких чисел
        :return: Выражение в виде f-строки
        """
        res = f"A({self.A - self.a}, {self.A}, {self.A + self.a}) * B({self.B - self.b}, {self.B}, {self.B + self.b}) = " \
              f"({(self.A - self.a) * (self.B - self.b)}, {self.A * self.B}, {(self.A + self.a) * (self.B + self.b)})"
        return res

    def calculate_division(self):
        """
        Метод для деления двух нечётких чисел
        :return: Выражение в виде f-строки
        """
        try:
            res = f"A({self.A - self.a}, {self.A}, {self.A + self.a}) / B({self.B - self.b}, {self.B}, {self.B + self.b}) = " \
               f"({round((self.A - self.a) / (self.B - self.b), 2)}, {round(self.A / self.B, 2)}, {round((self.A + self.a) / (self.B + self.b), 2)})"
            return res
        except ZeroDivisionError:
            print('Деление на ноль запрещено!')


# Демонстрация работы класса-потомка Fuzzy_numbers и его методов

f = Fuzzy_numbers(4, 1, 6, 0)

print(f.calculate_sum())
print(f.calculate_subtraction())
print(f.calculate_product())
print(f.calculate_division())

