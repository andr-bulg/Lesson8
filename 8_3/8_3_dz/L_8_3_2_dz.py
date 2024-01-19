"""
Измените класс “Матрица” следующим образом:
* свойства класса - размерность матрицы и элементы - должны быть динамическими
  и задаваться внутри нового метода, определяющего матрицу;
* добавьте статические свойства - общее количество созданных матриц,
  количество единичных, нулевых и диагональных матриц;
* добавьте метод, реализующий форматированный вывод на экран статических свойств класса.
"""


class Matrix:

# Статические свойства класса Matrix
    count_matrix = 0            # Общее количество созданных матриц
    count_unit_matrix = 0       # Количество единичных матриц
    count_null_matrix = 0       # Количество нулевых матриц
    count_diagonal_matrix = 0   # Количество диагональных матриц
    
    def __init__(self, n_matr, matrix):
        """
        Создание нового объекта матрица через конструктор __init__()
        :param n_matr: размерность матрицы
        :param matrix: элементы матрица
        """
        self.n = n_matr
        self.matr = matrix
        Matrix.count_matrix += 1

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
        print(f"Вывод на печать матрицы размерностью {self.n}:")
        for row in self.matr:
            for el in row:
                print(el, end=' ')
            print()

    def determinant_matrix(self):
        """
        Вычисление детерминанта двумерной матрицы
        :return:
        """
        if self.n != 2:
            print("Детерминант вычисляется только для двумерной матрицы")
            return
        det = self.matr[0][0] * self.matr[1][1] - self.matr[1][0] * self.matr[0][1]
        return det

    def unit_matrix(self):
        """
        Определение единичной матрицы
        :return:
        """
        flag = 0
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                if i == j and self.matr[i][j] != 1:
                    print("Матрица не является единичной")
                    flag = 1
                    break

                elif i != j and self.matr[i][j] != 0:
                    print("Матрица не является единичной")
                    flag = 1
                    break

            if flag == 1:
                break
        else:
            print("Матрица является единичной")
            Matrix.count_unit_matrix += 1
            self.print_matrix()

    def null_matrix(self):
        """
        Определение нулевой матрицы
        :return:
        """
        flag = 0
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                if self.matr[i][j] != 0:
                    print("Матрица не является нулевой")
                    flag = 1
                    break

            if flag == 1:
                break
        else:
            print("Матрица является нулевой")
            Matrix.count_null_matrix += 1
            self.print_matrix()

    def diagonal_matrix(self):
        """
        Определение диагональной матрицы
        :return:
        """
        flag = 0
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                if i == j and self.matr[i][j] == 0:
                    print("Матрица не является диагональной")
                    flag = 1
                    break

                elif i != j and self.matr[i][j] != 0:
                    print("Матрица не является диагональной")
                    flag = 1
                    break

            if flag == 1:
                break
        else:
            print("Матрица является диагональной")
            Matrix.count_diagonal_matrix += 1
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

print("Детерминант матрицы равен:", m.determinant_matrix())

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

