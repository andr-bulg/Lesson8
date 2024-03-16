"""
Создать класс “Account”, представляющий собой банковский счет.
Класс должен содержать:
- динамические свойства: фамилия владельца, номер счета,
   процент начисления, сумма в рублях;
- статические свойства: курс рубля по отношению к доллару, курс рубля по отношению к евро;
- классовые методы: редактировать курс рубля по отношению к доллару,
  редактировать курс рубля по отношению к евро;
- статические методы: перевод суммы в доллары и евро;
- конструктор: вызывает конструктор родительского класса и выводит сообщение
  о создании нового банковского счета;
- инициализатор: определяет динамические свойства класса и выводит информацию
  об открытом счете;
- деструктор: выводит сообщение о том, что банковский счет закрыт;
- методы: смена владельца счета, снятие заданной суммы,
  начисление заданной суммы, начисление процентов,
  перевод в доллары и евро (в отличие от аналогичных статических методов,
  данные методы не принимают параметров), вывод информации о счете;

Продемонстрировать работу класса и всех его методов.
"""

class Account():

    # Статические свойства
    usd_rate = 90    # курс рубля по отношению к доллару
    euro_rate = 100  # курс рубля по отношению к евро


    # Переопределение конструктора
    def __new__(cls, *args, **kwargs):
        print("Новый банковский счёт был создан!")
        return super().__new__(cls)

    # Определение динамических свойств класса через инициализатор
    def __init__(self, owner, account, percent, summa):
        """
        Инициализатор класса “Account”
        :param owner: фамилия владельца счёта
        :param account: номер банковского счёта
        :param percent: процент начисления
        :param summa: сумма на счёте в рублях
        """
        self.owner = owner
        self.account = account
        self.percent = percent
        self.summa = summa
        print(f"Счёт {self.account!r} для владельца {self.owner} был открыт!")
        print(f"На данном счёте будет храниться {self.summa} рублей "
              f"под {self.percent}% годовых.")

    # Переопределение деструктора
    def __del__(self):
        print(f"Банковский счёт {self.account!r} был закрыт!")


    # Определение классового метода для редактирования курса рубля по отношению к доллару
    @classmethod
    def change_usd_rate(cls, new_value):
        """
        :param new_value: значение нового курса доллара по отношению к рублю
        """
        cls.usd_rate = new_value

    # Определение классового метода для редактирования курса рубля по отношению к евро
    @classmethod
    def change_euro_rate(cls, new_value):
        """
        :param new_value: значение нового курса евро по отношению к рублю
        """
        cls.euro_rate = new_value

    # Создание статического метода для перевода суммы в рублях в доллары
    @staticmethod
    def convert_to_usd(summa):
        """
        :param summa: Сумма в рублях, которая будет переведена в доллары
        """
        res = summa // Account.usd_rate
        print(f"{summa} RUB - это {res} USD.")

    # Создание статического метода для перевода суммы в рублях в евро
    @staticmethod
    def convert_to_euro(summa):
        """
        :param summa: Сумма в рублях, которая будет переведена в евро
        """
        res = summa // Account.euro_rate
        print(f"{summa} RUB - это {res} EUR.")


    # Определение методов уровня класса

    def change_owner(self, new_owner):
        """
        Метод смены владельца счёта
        :param new_owner: фамилия нового владельца счёта
        :return:
        """
        self.owner = new_owner

    def top_down_balance(self, some_money):
        """
        Метод снятия заданной суммы
        :param some_money: заданная сумма
        :return: Новая сумма на счёте в рублях
        """
        self.summa -= some_money
        return self.summa

    def top_up_balance(self, some_money):
        """
        Метод начисления заданной суммы
        :param some_money: заданная сумма
        :return: Новая сумма на счёте в рублях
        """
        self.summa += some_money
        return self.summa

    def charge_percents(self):
        """
        Метод начисления процентов за год
        :return: Сумма процентов за год
        """
        return self.summa * self.percent // 100

    def convert_to_usd_2(self):
        """
        Метод для перевода суммы в рублях в доллары
        :return: Сумма в долларах
        """
        return self.summa // self.usd_rate

    def convert_to_euro_2(self):
        """
        Метод для перевода суммы в рублях в евро
        :return: Сумма в евро
        """
        return self.summa // self.euro_rate

    def print_info(self):
        """
        Метод, выводящий информацию о счёте
        :return:
        """
        print(f"Информация о счёте {self.account!r}:")
        print(f"владелец счёта: {self.owner}, сумма: {self.summa} RUB, "
              f"процентная ставка: {self.percent}% годовых.")


# Демонстрация работы класса Account и всех его методов

# Создание объекта класса Account
acc_1 = Account('Иванов', '12345678043', 5, 4000)
print("Курс рубля по отношению к доллару:", acc_1.usd_rate)
print("Курс рубля по отношению к евро:", acc_1.euro_rate)

print('*' * 50)

# Изменение курса доллара и евро через классовые методы
Account.change_usd_rate(100)
Account.change_euro_rate(120)
print("Новый курс рубля по отношению к доллару:", acc_1.usd_rate)
print("Новый курс рубля по отношению к евро:", acc_1.euro_rate)

print('*' * 50)

# Вызов статического метода для перевода суммы в рублях в доллары
acc_1.convert_to_usd(acc_1.summa)
# Вызов статического метода для перевода суммы в рублях в евро
acc_1.convert_to_euro(acc_1.summa)

print('*' * 50)

print("Перевод суммы из RUB в USD методом уровня класса:", acc_1.convert_to_usd_2())
print("Перевод суммы из RUB в EUR методом уровня класса:", acc_1.convert_to_euro_2())

print('*' * 50)

# Смена владельца счёта
acc_1.change_owner('Петрова')

# Снятие/начисление заданной суммы
print("Текущая сумма на счёте:", acc_1.summa, "RUB")
acc_1.top_down_balance(120)
acc_1.top_up_balance(300)
print("Сумма на счёте после снятия и пополнения:", acc_1.summa, "RUB")

# Вычисление суммы % за год
print("Сумма % за год:", acc_1.charge_percents(), "RUB")

print('*' * 50)

acc_1.print_info()

print()
# Вызов переопределённого деструктора
del acc_1

