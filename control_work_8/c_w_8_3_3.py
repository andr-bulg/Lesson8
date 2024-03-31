"""
Внести изменения в созданный в задаче c_w_8_3_1 класс “Alcohol”:
переопределить методы вычисления массы и объема жидкости таким образом,
чтобы в них также рассчитывалось соответственно массовое или объемное содержание
чистого спирта, исходя из заданной крепости.

Переопределить метод вывода информации о спирте.
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


    def calculate_volume(self, m):
        """
        Переопределение метода из родительского класса
        Метод для вычисления объёма спиртосодержащей жидкости
        и объёма содержания чистого спирта в ней
        :param m: заданная масса спиртосодержащей жидкости
        :return: Объём спиртосодержащей жидкости и объём содержания чистого спирта
        """
        v = round(m / self.density, 2)
        v2 = v * self.strength / 100
        return [v, v2]

    def calculate_weight(self, v):
        """
        Переопределение метода из родительского класса
        Метод для вычисления массы спиртосодержащей жидкости
        и массы содержания чистого спирта в ней
        :param v: заданный объём спиртосодержащей жидкости
        :return: Масса спиртосодержащей жидкости и масса содержания чистого спирта
        """
        m = self.density * v
        m2 = self.density * self.calculate_volume(m)[1]
        return [m, m2]

    def print_info(self):
        """
        Переопределение метода из родительского класса
        Метод, выводящий информацию о спиртосодержащей жидкости
        """
        print(f"{self.name} имеет плотность {self.density} кг/м**3 "
              f"и крепость {self.strength} градуса/ов.")


# Демонстрация работы класса-наследника Alcohol и всех его методов

a1 = Alcohol('Пиво', 1100, 4.5)

a1.print_info()

a1.change_density(1000)
print("{} имеет новую плотность, равную {} кг/м**3.".format(a1.name, a1.density))

print(f"Объём пива массой 30 кг равен {a1.calculate_volume(30)[0]} м**3.")
print(f"Объёмное содержание чистого спирта в пиве "
      f"массой 30кг равно {a1.calculate_volume(30)[1]} м**3.")

print(f"Масса пива объёмом 2 м**3 равна {a1.calculate_weight(2)[0]} кг.")
print(f"Массовое содержание чистого спирта "
      f"в пиве объёмом 2 м**3 равно {a1.calculate_weight(2)[1]} кг.")

print("Текущая крепость пива составляет", a1.strength, "градуса.")
a1.change_strength(5)
print(f"{a1.name} имеет новую крепость, равную {a1.strength} градусам.")

