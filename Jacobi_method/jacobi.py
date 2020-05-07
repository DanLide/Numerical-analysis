import numpy as np

def jacobi(A, b, x_init, eps=1e-10, max_iterations=2000):
    '''
    def jacobi(A, b, x_init, epsilon=1e-10, max_iterations=2000)

    Ітеративний метод, що знаходить розв'язок СЛАР у формі вектора X.
    Вхідна матриця А представляється, як A = L + D + R,
    де L - строго нижня трикутна матриця, D - діагональна, R - строго верхня трикутна матриця.
    Початкова система має вигляд Lx + Dx + Rx = b.

    Приймає на вхід матрицю А, вектор вільних членів b, початкове наближення вектора x,
    точність eps, максимальну к-сть ітерацій max_iterations.
 
    Повертає вектор-розв'язок X та к-сть виконаних ітерацій.
    '''
    iter_num = 0
    D = np.diag(np.diag(A))
    LR = A - D
    x = x_init
    
    for iter_num in range(max_iterations):
        D_inv = np.diag(1 / np.diag(D))
        x_new = np.dot(D_inv, b - np.dot(LR, x))

        if np.linalg.norm(x_new - x) < eps:
            return x_new, iter_num
        x = x_new

    return x, iter_num


def main():
    fp = open('test.txt')

    for _ in range(2):
        j = 0
        A = list()
        a = list()
        b = list()
        current_line = fp.readline()

        # Зчитуємо з файлу розширену матрицю А
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

        x_init = np.zeros(len(b))

        # Застосовуємо метод Якобі
        x, iter_num = jacobi(a, b, x_init)

        print(f'Solution:\n{x}')
        print(f'Num of iterations: {iter_num}')
        print(f'Is solution correct? {np.allclose(np.dot(a, x), b)}')
    fp.close()

if __name__ == "__main__":
    main()