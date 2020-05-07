import math

def symmetric_check(matrix_a):
    '''
    def symmetric_check(matrix_a)
    Перевіряє, чи є вхідна матриця симетричною.

    Приймає на вхід матрицю А.
 
    Повертає True, якщо матриця А симетрична.
    Інакше, повертає False.
    '''
    n = len(matrix_a)

    for i in range(n):
        for j in range(n):
            if i != j:
                if matrix_a[i][j] != matrix_a[j][i]:
                    return False
    return True


def matrix_times_vector(a, x):
    '''
    def matrix_times_vector(a, x)
    Знаходить добуток матриці на вектор.

    Приймає на вхід матрицю a та вектор x.
 
    Повертає результат множення матриці на вектор y.
    '''
    y = []
    for i in range(len(x)):
        s = 0
        for j in range(len(x)):
            s += a[i][j] * x[j]
        y.append(s)
    return y


def multiply(num, x):
    '''
    def multiply(num, x)
    Знаходить добуток числа на вектор

    Приймає на вхід дійсне число num та вектор x.
 
    Повертає результат множення у вигляді вектора x.
    '''
    for i in range(len(x)):
        x[i] *= num
    return x


def sp(a, eps=10e-6):
    '''
    def sp(a, eps=10e-6)
    Ітеративний метод, що знаходить найбільше власне значення (за модулем) та відповідний йому вектор.

    Приймає на вхід симетричну матрицю А та точність eps.
 
    Повертає власне значення l, вектор x та True,
    якщо дотримані початкові умови (симетричність матриці А),
    інакше False.
    '''
    n = len(a)
    if not symmetric_check(a):
        return 0, 0, False

    # Ініціалізуємо початковий вектор y0
    y = [1] * n
    y_last = y

    # Ініціалізуємо початкове власне значення
    l = 0
    l_last = 1

    s = sum([y[i] * y[i] for i in range(n)])
    y_norm = math.sqrt(s)
    x = [y[i] / y_norm for i in range(n)]

    k = 0
    while abs(l - l_last) > eps:
        k += 1
        l_last = l

        y = matrix_times_vector(a, y)

        # Скалярні добутки
        s = sum([y[i] * y[i] for i in range(n)])
        t = sum([y[i] * y_last[i] for i in range(n)])

        y_norm = math.sqrt(s)
        x = [y[i] / y_norm for i in range(n)]
        l = s / t

        y_last = y

    print(f'Iterations: {k}\n')
    return (l, x, True)


def main():
    fp = open('test.txt')

    for _ in range(2):
        j = 0
        A = list()
        current_line = fp.readline()

        # Зчитуємо розширену матрицю А з файлу
        while current_line != 'n\n':
            A.append(list(map(float, current_line.split())))
            current_line = fp.readline()
            j += 1

        print('Matrix A:')
        for row in A:
            print(row)
        print()

        # Застосовуємо метод скалярних добутків
        (l, x, conditions_met) = sp(A)

        # Якщо дотримані початкові умови використання методу
        if conditions_met:
            print(f'Lambda: {l}')
            print(f'X: {x}\n')

            # Перевірка
            a = matrix_times_vector(A, x)
            s = multiply(l, x)
            print(f'Verification (A*x == lambda*x):')
            print(f'A*x:\n{a}')
            print(f'lambda*x:\n{s}\n')
        else:
            print('Sufficient condition for convergence of the iterative process is not fulfilled\n')


if __name__ == "__main__":
    main()
