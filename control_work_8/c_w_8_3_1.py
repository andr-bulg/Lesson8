"""
Создать класс "Liquid" (жидкость) со свойствами: название и плотность жидкости,
и методами: изменение плотности; вычисление объема жидкости,
соответствующего заданной массе; вычисление массы жидкости,
соответствующей заданному объему; вывод информации о жидкости.

Создать производный класс "Alcohol" (спирт) с собственным свойством - крепость,
и методом: изменение крепости.

Продемонстрировать работу класса-наследника и всех его методов.
"""

class Liquid():

    def __init__(self, name, density):
        """
        Инициализатор класса "Liquid"
        :param name: название жидкости
        :param density: плотность жидкости
        """
        self.name = name
        self.density = density


    def change_density(self, new_density):
        """
        Метод для изменения значения плотности жидкости
        :param new_density: новое значение плотности жидкости
        """
        self.density = new_density

    def calculate_volume(self, m):
        """
        Метод для вычисления объёма жидкости
        :param m: заданная масса жидкости
        :return: Объём жидкости
        """
        v = round(m / self.density, 2)
        return v

    def calculate_weight(self, v):
        """
        Метод для вычисления массы жидкости
        :param v: заданный объём жидкости
        :return: Масса жидкости
        """
        m = self.density * v
        return m

    def print_info(self):
        """
        Метод, выводящий информацию о жидкости
        """
        print(f"{self.name} имеет плотность, равную {self.density} кг/м**3.")


class Alcohol(Liquid):

    def __init__(self, name, density, strength):
        """
        Инициализатор класса-потомка "Alcohol"
        :param name: название алкоголя
        :param density: плотность алкоголя
        :param strength: крепость алкоголя
        """
        # Функция super() возвращает объект родительского класса, на котором
        # вызывается инициализатор родительского класса, и, тем самым,
        # задаются свойства объекта name и density. Параметр self не нужен,
        # так как инициализатор уже вызывается на объекте.
        super().__init__(name, density)

        self.strength = strength

    def change_strength(self, new_strength):
        """
        Метод для изменения значения крепости алкоголя
        :param new_strength: новое значение крепости алкоголя
        """
        self.strength = new_strength

# Демонстрация работы класса-наследника Alcohol и всех его методов

a1 = Alcohol('Пиво', 1100, 4.5)

a1.print_info()

a1.change_density(1000)
print("{} имеет новую плотность, равную {} кг/м**3.".format(a1.name, a1.density))

print(f"Объём 30 кг пива равен {a1.calculate_volume(30)} м**3.")

print(f"Масса пива объёмом 2 м**3 равна {a1.calculate_weight(2)} кг.")

print("Текущая крепость пива составляет", a1.strength, "градуса.")
a1.change_strength(5)
print(f"{a1.name} имеет новую крепость, равную {a1.strength} градусам.")


