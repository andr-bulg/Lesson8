"""
Определить класс “Матрица” со свойствами: размерность матрицы, элементы матрицы,
и методами: вывод матрицы на экран,
вычисление определителя матрицы (для матриц с размерностью 2 или 3)
и проверки, является ли матрица единичной, нулевой или диагональной.

* Расширьте метод вычисления определителя матрицы для матриц любой размерности.
"""


class Matrix:
    n = 2
    matr = [[1, 7],
            [3, 2]]

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
        if Matrix.n != 2:
            print("Детерминант вычисляется только для двумерной матрицы")
            return
        det = Matrix.matr[0][0] * Matrix.matr[1][1] - Matrix.matr[1][0] * Matrix.matr[0][1]
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
            self.print_matrix()

    def null_matrix(self):
        """
        Определение нулевой матрицы
        :return:
        """
        flag = 0
        for i in range(len(Matrix.matr)):
            for j in range(len(Matrix.matr[i])):
                if Matrix.matr[i][j] != 0:
                    print("Матрица не является нулевой")
                    flag = 1
                    break

            if flag == 1:
                break
        else:
            print("Матрица является нулевой")
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
            self.print_matrix()


# Создание объекта (экземпляра) класса Matrix
m = Matrix()

# Вызов методов на объекте класса
m.print_matrix()
m.null_matrix()

# Вызов методов на классе с передачей самого объекта в качестве аргумента
Matrix.unit_matrix(m)
Matrix.diagonal_matrix(m)

print(m.determinant_matrix())
