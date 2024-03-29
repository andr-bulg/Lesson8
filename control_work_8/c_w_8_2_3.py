"""
Внести изменения в созданный класс "Time" следующим образом:
- динамические свойства класса “Time” должны иметь модификатор доступа protected;
- определить методы getter и setter для свойств с модификаторами
  доступа protected;
- любое взаимодействие с protected свойствами должно производиться
  посредством соответствующих методов getter и setter.

Продемонстрировать работу измененных классов.
"""

class Time:

    # Статическое свойство
    time_zone = "UTC +/-{}".format(0)  # часовой пояс


    # Переопределение конструктора
    def __new__(cls, *args, **kwargs):
        print("Создан новый момент времени в виде объекта Time!")
        return super().__new__(cls)

    # Определение динамических свойств класса через инициализатор
    def __init__(self, h, m, s):
        """
        Инициализатор класса “Time”
        :param h: количество часов
        :param m: количество минут
        :param s: количество секунд
        """

        if not self.check_data(h, m, s):
            print(f"Свойства для объекта класса Time: '{h:02}:{m:02}:{s:02}' заданы неправильно!")
            print("Будет создан объект, имеющий некорректные свойства.")

        self.set_h(h)
        self.set_m(m)
        self.set_s(s)
        print(f"Объект класса Time: '{h:02}:{m:02}:{s:02}'")

    # Переопределение деструктора
    def __del__(self):
        print("Момент времени '{:02}:{:02}:{:02}' был удалён!".format(self.get_h(), self.get_m(), self.get_s()))


    # Методы getter для свойств h, m и s, которые возвращают значения этих свойств
    def get_h(self):
        return self._h

    def get_m(self):
        return self._m

    def get_s(self):
        return self._s


    # Методы setter для свойств h, m и s, которые устанавливают значения этих свойств
    def set_h(self, h):
        self._h = h

    def set_m(self, m):
        self._m = m

    def set_s(self, s):
        self._s = s


    # Добавление классового метода
    @classmethod
    def change_time_zone(cls, some_h):
        """
        Метод для редактирования часового пояса
        :param some_h: количество часов
        :return: None
        """
        if some_h > 0:
            cls.time_zone = f"UTC +{some_h}"
        elif some_h < 0:
            cls.time_zone = f"UTC {some_h}"
        else:
            return


    # Добавление статических методов
    @staticmethod
    def check_data(h, m, s):
        """
        Метод для проверки корректности заданных величин (часов, минут, секунд)
        :param h: количество часов
        :param m: количество минут
        :param s: количество секунд
        :return: True или False
        """
        if h < 0 or h > 23:
            print("Неправильно задано количество часов!")
            print("Задайте количество часов в диапазоне от 0 до 23...")
            return False

        elif m < 0 or m > 59:
            print("Неправильно задано количество минут!")
            print("Задайте количество минут в диапазоне от 0 до 59...")
            return False

        elif s < 0 or s > 59:
            print("Неправильно задано количество секунд!")
            print("Задайте количество секунд в диапазоне от 0 до 59...")
            return False

        return True

    @staticmethod
    def convert_to_seconds(h, m, s):
        """
        Метод для преобразования заданного момента времени в секунды
        :param h: количество часов
        :param m: количество минут
        :param s: количество секунд
        :return: Заданное время в секундах
        """
        res = h * 60 * 60 + m * 60 + s
        return res

    @staticmethod
    def convert_to_time(s):
        """
        Метод для конвертации заданного количество секунд
        в момент времени в формате 'Час:Минута:Секунда'
        :param s: количество секунд
        :return: Момент времени в формате 'Час:Минута:Секунда'
        """
        h = s // 3600         # количество часов
        temp = s - h * 3600   # количество минут и секунд в секундах
        m = temp // 60        # количество минут
        s = temp - m * 60     # количество секунд
        res = "'{:02}:{:02}:{:02}'".format(h, m, s)
        return res


    # Определение методов уровня класса
    def time_diffence(self, h, m, s):
        """
        Метод для вычисления разницы между двумя моментами времени в секундах,
        моментом времени в виде объекта и заданным моментом времени
        :param h: заданное количество часов
        :param m: заданное количество минут
        :param s: заданное количество секунд
        :return: Разница между двумя моментами времени в секундах
        """
        res = self.convert_to_seconds(self.get_h(), self.get_m(), self.get_s()) - Time.convert_to_seconds(h, m, s)
        return abs(res)

    def addition_seconds(self, s):
        """
        Метод для сложения момента времени объекта с заданным количеством секунд
        :param s: заданное количество секунд
        :return: Итоговый момент времени
        """
        res = self.convert_to_seconds(self.get_h(), self.get_m(), self.get_s()) + s
        res = self.convert_to_time(res)
        return res

    def subtraction_seconds(self, s):
        """
        Метод для вычитания из момента времени объекта заданного количества секунд
        :param s: заданное количество секунд
        :return: Итоговый момент времени
        """
        temp = self.convert_to_seconds(self.get_h(), self.get_m(), self.get_s())
        if temp < s:
            print("Заданное количество секунд больше, чем момент времени объекта!")
            return
        res = self.convert_to_time(temp - s)
        return res

    def compare_time_moments(self, h, m, s):
        """
        Метод для сравнения двух моментов времени:
        момента времени объекта и заданного момента времени
        :param h: заданное количество часов
        :param m: заданное количество минут
        :param s: заданное количество секунд
        :return: None
        """
        res_obj = self.convert_to_seconds(self.get_h(), self.get_m(), self.get_s())
        res = Time.convert_to_seconds(h, m, s)
        if res_obj > res:
            print("Момент времени объекта больше, чем заданный момент времени.")
        elif res_obj < res:
            print("Заданный момент времени больше, чем момент времени объекта.")
        else:
            print("Момент времени объекта и заданный момент времени равны.")

    def print_info(self):
        """
        Метод вывода на экран информации об объекте класса Time
        """
        print(f"Экземпляр класса Time имеет вид {self.get_h():02}:{self.get_m():02}:{self.get_s():02}")


# Демонстрация работы класса Time и всех его методов

# Создание объектов класса Time
t1 = Time(23, 45, 59)
t2 = Time(0, 0, 0)
print()

# Проверка методов уровня класса
t2.print_info()
print()

print("Разница между двумя моментами времени в секундах:", t2.time_diffence(1, 1, 1))
print()

print("Сложение с заданным количеством секунд:", t2.addition_seconds(362))
print()

t2.subtraction_seconds(222)
print("Вычитание с заданным количеством секунд:", t1.subtraction_seconds(333))
print()

# Сравнение момента времени объекта t1 с заданным моментом времени
t1.compare_time_moments(23, 45, 59)
t1.compare_time_moments(23, 45, 58)
Time.compare_time_moments(t1, 23, 46, 1)
print()

# Проверка классового метода
print("Текущий часовой пояс:", t1.time_zone)

Time.change_time_zone(5)
print("Новый часовой пояс:", t1.time_zone)
t1.change_time_zone(-3)
print("Новый часовой пояс:", Time.time_zone)
print()

# Проверка статических методов

# Преобразование заданного момента времени в секунды
print("Число секунд:", Time.convert_to_seconds(12, 48, 39))

# Преобразование заданного количества секунд в момент времени
print("Момент времени:", Time.convert_to_time(4))

# Проверка корректности заданных величин (часов, минут, секунд)
print()
print(Time.check_data(24, 1, 34))
print(Time.check_data(21, 60, 0))
print(t1.check_data(5, 10, 60))
print(t1.check_data(23, 59, 59))
print(t1.check_data(0, 0, 0))
print()
