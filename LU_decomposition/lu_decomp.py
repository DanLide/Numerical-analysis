from numpy import allclose, dot, zeros, linalg
import copy

def find_minor_matrix(A, i, j):
    '''
    find_minor_matrix(A, i, j)
    Знаходить матрицю для доповнювального мінору.
    Приймає на вхід матрицю А, з якої треба вилучити i-ий рядок та j-ий стовпець.
 
    Повертає матрицю M.
    '''
    M = copy.deepcopy(A)
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M   
    
def find_det(A):
    '''
    find_det(A)
    Рекурсивно знаходить визначник матриці А, використовуючи формулу розкладання за першим рядком.

    Повертає число -- визначник матриці А.
    '''
    m = len(A)
    n = len(A[0]) 
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0
    # формула розкладання за першим рядком
    for j in range(n):
        determinant += A[0][j]*signum*find_det(find_minor_matrix(A, 0, j)) 
        signum *= -1
    return determinant

def check_minors(matrix_a):
    '''
    check_minors(matrix_a)
    Знаходить головні мінори матриці А та перевіряє, чи відмінні вони від нуля.
 
    Повертає True, якщо всі головні мінори матриці А відмінні від нуля.
    Інакше, повертає False.
    '''
    length = len(matrix_a)
    minor = list()

    for counter in range(1, length + 1):
        # Створення матриці головного мінора шляхом виключення n - k останніх рядків і стовпців з матриці А,
        # де n -- порядок матриці А, а k -- порядок головного мінора
        for i in range(counter):
            minor.append([])
            for j in range(counter):
                minor[i].append(a[i][j])

        print('Minor\'s matrix:')
        for line in minor:
            for col in line:
                print(col, end=' ')
            print()

        det = find_det(minor)
        print(f'Determinant: {det}\n')

        if det == 0:
            return False
        minor = list()

    return True

def lu_decomposition(matrix_a, matrix_b):
    '''
    lu_decomposition(matrix_a, matrix_b)
    Знаходить розв'язок СЛАР використовуючи метод LU-розкладу
 
    Повертає розв'язок у формі вектора x
    '''
    if check_minors(matrix_a) == False:
        return None

    n = len(matrix_a)

    lower = zeros((n, n))
    upper = zeros((n, n))

    # Вводимо заміну A = LU
    # Знаходимо верхню та нижню трикутні матриці
    for s in range(n):
        # Верхня трикутна матриця
        for j in range(s, n):
            sum = 0
            for k in range(s):
                sum += (lower[s][k] * upper[k][j])

            upper[s][j] = matrix_a[s][j] - sum

        # Нижня трикутна матриця
        for i in range(s + 1, n):
            sum = 0
            for k in range(s):
                sum += (lower[i][k] * upper[k][s])

            lower[i][s] = (matrix_a[i][s] - sum) / upper[s][s]

    print(f'L:\n{lower}\n')
    print(f'U\n{upper}\n')

    # Отже, вираз набуває вигляду LUx = b
    # Вводимо заміну Ux = y
	# Тоді маємо Ly = b, звідси знаходимо y
    y = zeros(n)
    for i in range(n):
        sum = 0
        for s in range(i):
            sum += lower[i][s]*y[s]
        y[i] = b[i] - sum

	# Повертаємося до виразу Ux = y, знаходимо x
    x = zeros(n)
    for i in range(n - 1, -1, -1):
        sum = 0
        for s in range(i + 1, n):
            sum += upper[i][s]*x[s]
        x[i] = (y[i] - sum) / upper[i][i]

    return x

if __name__ == "__main__":
    fp = open('/home/danlide/stuDYING/NM/Numerical-analysis/LU_decomposition/test1.txt')

    for i in range(3):
        j = 0
        A = list()
        a = list()
        b = list()
        current_line = fp.readline()

        # Зчитуємо матриці з файлу
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

        x = lu_decomposition(a, b)
        if x.any() == None:
            print('LU decomposition is impossible\n')
        elif x.any() != 0:
            print(f'Solution:\n{x}')
            print(f'Is solution correct? {allclose(dot(a, x), b)}\n')
    fp.close()
