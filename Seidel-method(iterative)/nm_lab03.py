'''
Author: DanLide
Date: 10.2019

A program applies iterative Seidel method to find solution of system of linear equations.
Can be applied to any matrix with non-zero elements on the diagonals, convergence is only guaranteed if the matrix is either diagonally dominant, or symmetric and positive definite.
Checks Ax = b condition
'''

import numpy as np

EPS = 1e-6

def convergence_check(matrix_a):
    n = len(matrix_a)
    for i in range(n):
        s = sum([matrix_a[i][j] for j in range(n) if i != j])
        if matrix_a[i][i] < s:
            return False
    return True

def seidel_method(matrix_a, matrix_b):
    if not convergence_check(matrix_a):
        return 0, 0, 0, False

    n = len(matrix_a)
    x = np.zeros(n)
    iteration = 0
    error = 1

    while error > EPS:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(matrix_a[i][j] * x_new[j] for j in range(i))
            s2 = sum(matrix_a[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / matrix_a[i][i]
        error = sum(abs(x_new[i] - x[i])  for i in range(n))
        iteration += 1
        x = x_new

    return x, iteration, error, True

if __name__ == "__main__":
    fp = open('test2.txt')
    print(f'For EPS = {EPS}:')

    for i in range(2):
        j = 0
        A = list()
        a = list()
        b = list()
        current_line = fp.readline()

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

        x, iter, err, flag = seidel_method(a, b)

        if flag:
            print(f'Solution:\n{x}')
            print(f'Num of iterations: {iter}')
            print(f'Error: {err}')
            print(f'Is solution correct? {np.allclose(np.dot(a, x), b)}')
            print('Third-party library:')
            print(np.linalg.solve(a, b))
            print()
        else:
            print('Sufficient condition for convergence of the iterative process is not fulfilled')
    fp.close()
