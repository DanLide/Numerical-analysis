from numpy import allclose, dot, zeros

eps = 10e-8

def matrix_max_row(matrix, n):
    '''
    matrix_max_row(matrix, n)
    Знаходить найбільший елемент у стопці і міняє рядки місцями.
    Якщо головний елемент меньше за eps, то алгоритм завершує роботу

    Допомагає уникнути ділення на нуль і зменшити вплив похибок заокруглень.
    
    Повертає розширену матрицю А.

    '''
    max_element = matrix[n][n]
    max_row = n

    if n == len(matrix) - 1:
        if abs(max_element) < eps:
            print('The system does not have a clear solution\n')
            return

    for i in range(n + 1, len(matrix)):
        if abs(matrix[i][n]) > abs(max_element):
            max_element = matrix[i][n]
            max_row = i
        if abs(max_element) < eps:
            print('The system does not have a clear solution\n')
            return None
        if max_row != n:
            matrix[n], matrix[max_row] = matrix[max_row], matrix[n]
            break
    return matrix


def gauss_func(matrix):
    '''
    gauss_func(matrix)
    Застосовує метод Гауса з постовпцевим вибором головного елемента до розширеної матриці А.

    Повертає розв'язок у вигляді вектора X.

    '''

    n = len(matrix)
    det = 1.0

    # Прямий хід
    for k in range(n):
        matrix = matrix_max_row(matrix, k)
        if matrix == None:
            return
        for i in range(k + 1, n):
            m = -matrix[i][k] / matrix[k][k]
            matrix[i][-1] += m * matrix[k][-1]
            for j in range(k, n):
                matrix[i][j] += m * matrix[k][j]

    # Розрахунок визначника
    for i in range(n):
        det *= matrix[i][i]
    print(f'Determinant: {det}')

    # Зворотній хід
    for k in range(n - 1, -1, -1):
        x[k] = (matrix[k][-1] - sum([matrix[k][j] * x[j] for j in range(k + 1, n)])) / matrix[k][k]
    return x

if __name__ == "__main__":

    fp = open("/home/danlide/stuDYING/NM/Numerical-analysis/Gauss_method/test.txt")

    for i in range(4):
        j = 0
        A = list()
        a = list()
        b = list()
        current_line = fp.readline()

        # Зчитування матриці з файлу та запис у змінну
        while current_line != 'n\n':
            A.append(list(map(float, current_line.split())))
            current_line = fp.readline()
            a.append(A[j][:-1])
            b.append(A[j][-1])
            j += 1

        print('Extended matrix A:')
        for row in A:
            print(row)
        print()

        x = zeros(len(A))
        print('Solution:')
        x1 = gauss_func(A)

        if x.any() != 0:
            for i in range(len(x1)):
                print(f'x{i + 1} = {x1[i]}')
            print(f'Is solution correct? {allclose(dot(a, x1), b)}\n\n')

    fp.close()
