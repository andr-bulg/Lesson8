"""
Внести изменения в созданный класс "Account" следующим образом:
- динамические свойства класса “Account” должны иметь модификатор доступа private;
- определить методы getter и setter для свойств с модификатором
  доступа private;
- любое взаимодействие с private свойствами должно производиться
  посредством соответствующих методов getter и setter.

Продемонстрировать работу измененных классов.
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

        # Установка свойств объекта через setter
        self.set_owner(owner)
        self.set_account(account)
        self.set_percent(percent)
        self.set_summa(summa)
        print(f"Счёт {account!r} для владельца {owner} был открыт!")
        print(f"На данном счёте будет храниться {summa} рублей "
              f"под {percent}% годовых.")

    # Переопределение деструктора
    def __del__(self):
        print(f"Банковский счёт {self.get_account()!r} был закрыт!")


    # Методы getter для свойств owner, account, percent, summa,
    # которые возвращают значения этих свойств
    def get_owner(self):
        return self.__owner

    def get_account(self):
        return self.__account

    def get_percent(self):
        return self.__percent

    def get_summa(self):
        return self.__summa


    # Методы setter для свойств owner, account, percent, summa,
    # которые устанавливают значения этих свойств

    def set_owner(self, owner):
        self.__owner = owner

    def set_account(self, account):
        self.__account = account

    def set_percent(self, percent):
        self.__percent = percent

    def set_summa(self, summa):
        self.__summa = summa


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
        self.set_owner(new_owner)

    def top_down_balance(self, some_money):
        """
        Метод снятия заданной суммы
        :param some_money: заданная сумма
        :return: Новая сумма на счёте в рублях
        """
        return self.set_summa(self.get_summa() - some_money)

    def top_up_balance(self, some_money):
        """
        Метод начисления заданной суммы
        :param some_money: заданная сумма
        :return: Новая сумма на счёте в рублях
        """
        return self.set_summa(self.get_summa() + some_money)

    def charge_percents(self):
        """
        Метод начисления процентов за год
        :return: Сумма процентов за год
        """
        return self.get_summa() * self.get_percent() // 100

    def convert_to_usd_2(self):
        """
        Метод для перевода суммы в рублях в доллары
        :return: Сумма в долларах
        """
        return self.get_summa() // Account.usd_rate

    def convert_to_euro_2(self):
        """
        Метод для перевода суммы в рублях в евро
        :return: Сумма в евро
        """
        return self.get_summa() // Account.euro_rate

    def print_info(self):
        """
        Метод, выводящий информацию о счёте
        :return:
        """
        print(f"Информация о счёте {self.get_account()!r}:")
        print(f"владелец счёта: {self.get_owner()}, сумма: {self.get_summa()} RUB, "
              f"процентная ставка: {self.get_percent()}% годовых.")


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
acc_1.convert_to_usd(acc_1.get_summa())
# Вызов статического метода для перевода суммы в рублях в евро
acc_1.convert_to_euro(acc_1.get_summa())

print('*' * 50)

print("Перевод суммы из RUB в USD методом уровня класса:", acc_1.convert_to_usd_2())
print("Перевод суммы из RUB в EUR методом уровня класса:", acc_1.convert_to_euro_2())

print('*' * 50)

# Смена владельца счёта
acc_1.change_owner('Петрова')

# Снятие/начисление заданной суммы
print("Текущая сумма на счёте:", acc_1.get_summa(), "RUB")
acc_1.top_down_balance(120)
acc_1.top_up_balance(300)
print("Сумма на счёте после снятия и пополнения:", acc_1.get_summa(), "RUB")

# Вычисление суммы % за год
print("Сумма % за год:", acc_1.charge_percents(), "RUB")

print('*' * 50)

acc_1.print_info()

print()
# Вызов переопределённого деструктора
del acc_1

