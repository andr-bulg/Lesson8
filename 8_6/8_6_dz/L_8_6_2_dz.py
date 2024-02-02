"""
Изменить созданный ранее класс “Матрица” следующим образом:
- установить для одного из динамических свойств класса модификатор доступа protected,
  а для остальных (если имеются) - модификатор доступа private;
- добавить соответствующие методы getter и setter.
"""


class Matrix:
    # Статические свойства класса Matrix
    count_matrix = 0  # Общее количество созданных матриц
    count_unit_matrix = 0  # Количество единичных матриц
    count_null_matrix = 0  # Количество нулевых матриц
    count_diagonal_matrix = 0  # Количество диагональных матриц

    # Определение классового метода для изменения общего количества созданных матриц
    @classmethod
    def func_count_matrix(cls):
        cls.count_matrix += 1

    # Определение классового метода для изменения количества единичных матриц
    @classmethod
    def func_count_unit_matrix(cls):
        cls.count_unit_matrix += 1

    # Определение классового метода для изменения количества нулевых матриц
    @classmethod
    def func_count_null_matrix(cls):
        cls.count_null_matrix += 1

    # Определение классового метода для изменения количества диагональных матриц
    @classmethod
    def func_count_diagonal_matrix(cls):
        cls.count_diagonal_matrix += 1

    # Добавление конструктора
    def __new__(cls, *args, **kwargs):
        print("Новый объект класса Matrix создан!")
        return super().__new__(cls)

    # Для задания свойств объекта этот инициализатор использовался ранее
    def __init__(self, n_matr, matrix):
        """
        Инициализация исходных свойств объекта класса Matrix
        :param n_matr: размерность матрицы
        :param matrix: элементы матрица
        """
        # self._n = n_matr          protected
        # self.__matr = matrix      private

        # Установка свойств объекта через setter
        self.set_n(n_matr)        # protected
        self.set_matr(matrix)     # private

        # Было обращение через класс Matrix.count_matrix += 1
        # Теперь используется классовый метод
        Matrix.func_count_matrix()
        print(f"Исходные свойства объекта {self.get_matr()} заданы!")

    # Добавление деструктора
    def __del__(self):
        print(f"Объект {self.get_matr()} был удалён!")


    # Методы getter для свойств n, matr, которые возвращают их значения
    def get_n(self):
        return self._n

    def get_matr(self):
        return self.__matr

    # Методы setter для свойств n, matr, устанавливающие их значения
    def set_n(self, num):
        self._n = num

    def set_matr(self, matr):
        self.__matr = matr


    def static_properties(self):
        """
        Форматированный вывод на экран статических свойств класса
        :return:
        """
        print(f"Общее количество созданных матриц: {Matrix.count_matrix}")
        print(f"Общее количество единичных матриц: {Matrix.count_unit_matrix}")
        print(f"Общее количество нулевых матриц: {Matrix.count_null_matrix}")
        print(f"Общее количество диагональных матриц: {Matrix.count_diagonal_matrix}")


    def print_matrix(self):
        """
        Вывод матрицы на экран
        :return:
        """
        print(f"Вывод на печать матрицы размерностью {self.get_n()}:")
        for row in self.get_matr():
            for el in row:
                print(el, end=' ')
            print()

    # Создание статического метода как вспомогательного
    @staticmethod
    def determinant_matrix(n, matrix):
        """
        Вычисление детерминанта двумерной матрицы
        :param n: размерность матрицы
        :param matrix: элементы матрицы
        :return: значение детерминанта или 0, если матрица не является двумерной
        """
        if n != 2:
            # Детерминант вычисляется только для двумерной матрицы
            return 0
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    def print_determinant_matrix(self):
        """
        Вывод на печать детерминанта двумерной матрицы,
        полученного из статического метода determinant_matrix()
        :return:
        """
        det = Matrix.determinant_matrix(self.get_n(), self.get_matr())
        if not det:
            print("Детерминант вычисляется только для двумерной матрицы")
        else:
            print(f"Детерминант матрицы равен: {det}")


    def unit_matrix(self):
        """
        Определение единичной матрицы
        :return:
        """
        flag = 0
        for i in range(len(self.get_matr())):
            for j in range(len(self.get_matr()[i])):
                if i == j and self.get_matr()[i][j] != 1:
                    print("Матрица не является единичной")
                    flag = 1
                    break

                elif i != j and self.get_matr()[i][j] != 0:
                    print("Матрица не является единичной")
                    flag = 1
                    break

            if flag == 1:
                break
        else:
            print("Матрица является единичной")
            # Было обращение через класс Matrix.count_unit_matrix += 1
            # Теперь используется классовый метод
            Matrix.func_count_unit_matrix()
            self.print_matrix()

    def null_matrix(self):
        """
        Определение нулевой матрицы
        :return:
        """
        flag = 0
        for i in range(len(self.get_matr())):
            for j in range(len(self.get_matr()[i])):
                if self.get_matr()[i][j] != 0:
                    print("Матрица не является нулевой")
                    flag = 1
                    break

            if flag == 1:
                break
        else:
            print("Матрица является нулевой")
            # Было обращение через класс Matrix.count_null_matrix += 1
            # Теперь используется классовый метод
            Matrix.func_count_null_matrix()
            self.print_matrix()

    def diagonal_matrix(self):
        """
        Определение диагональной матрицы
        :return:
        """
        flag = 0
        for i in range(len(self.get_matr())):
            for j in range(len(self.get_matr()[i])):
                if i == j and self.get_matr()[i][j] == 0:
                    print("Матрица не является диагональной")
                    flag = 1
                    break

                elif i != j and self.get_matr()[i][j] != 0:
                    print("Матрица не является диагональной")
                    flag = 1
                    break

            if flag == 1:
                break
        else:
            print("Матрица является диагональной")
            # Было обращение через класс Matrix.count_diagonal_matrix += 1
            # Теперь используется классовый метод
            Matrix.func_count_diagonal_matrix()
            self.print_matrix()


# Создание объекта (экземпляра) класса Matrix
n_matr = 2
matrix = [[1, 7],
          [3, 2]]
m = Matrix(n_matr, matrix)

# Вызов методов на объекте класса
m.print_matrix()
m.null_matrix()

# Вызов методов на классе с передачей самого объекта в качестве аргумента
Matrix.unit_matrix(m)
Matrix.diagonal_matrix(m)

# Вычисление детерминанта матрицы
m.print_determinant_matrix()

m.static_properties()

# Единичная матрица
matrix2 = [[1, 0],
           [0, 1]]
m2 = Matrix(n_matr, matrix2)
m2.unit_matrix()
m2.static_properties()

# Нулевая матрица
matrix3 = [[0, 0],
           [0, 0]]
m3 = Matrix(n_matr, matrix3)
m3.null_matrix()
m3.static_properties()

# Диагональнная матрица
matrix4 = [[1, 0],
           [0, 2]]
m4 = Matrix(n_matr, matrix4)
m4.diagonal_matrix()
m4.static_properties()

# Изменение значения свойств объекта m3 через сеттеры
m3.set_n(3)
m3.set_matr([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Получение свойств объекта m3 и вывод их на печать через геттеры
print("Новые свойства объекта m3 класса Matrix:")
print(f"Матрица размерностью {m3.get_n()}:")
for row in m3.get_matr():
    print(row)


