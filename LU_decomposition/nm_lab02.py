'''
Author: DanLide
Date: 10.2019

A program applies LU decomposition to find solution of system of linear equations
Finds L, U matrixes and solution in the form of a vector X
Checks main minors != 0 condition while decomposing
Checks Ax = b condition
'''

import numpy as np

def check_minors(matrix_a):
    length = len(matrix_a)
    l = list()

    for counter in range(1, length + 1):
        for i in range(counter):
            l.append([])
            for j in range(counter):
                l[i].append(a[i][j])

        print('Minor:')
        for line in l:
            for col in line:
                print(col, end=' ')
            print()

        det = np.linalg.det(l)
        print(f'Determinant: {det}\n')

        if det == 0:
            return False
        l = list()

    return True

def lu_decomposition(matrix_a, matrix_b):
    if check_minors(matrix_a) == False:
        return None

    n = len(matrix_a)

    lower = np.zeros((n, n))
    upper = np.zeros((n, n))

    # Decomposing matrix into Upper
    # and Lower triangular matrix
    for s in range(n):
        # Upper Triangular
        for j in range(s, n):
            sum = 0;
            for k in range(s):
                sum += (lower[s][k] * upper[k][j])

            upper[s][j] = matrix_a[s][j] - sum

        # Lower Triangular
        for i in range(s + 1, n):
                sum = 0
                for k in range(s):
                    sum += (lower[i][k] * upper[k][s])

                lower[i][s] = (matrix_a[i][s] - sum) / upper[s][s]
    print('L:')
    print(lower)
    print()
    print('U:')
    print(upper)
    print()

	# Perform substitution Ly = b
    y = np.zeros(n)
    for i in range(n):
        sum = 0
        for s in range(i):
            sum += lower[i][s]*y[s]
        y[i] = b[i] - sum

	# Perform substitution Ux = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum = 0
        for s in range(i + 1, n):
            sum += upper[i][s]*x[s]
        x[i] = (y[i] - sum) / upper[i][i]

    return x

if __name__ == "__main__":
    fp = open('test1.txt')

    for i in range(3):
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

        x = lu_decomposition(a, b)
        if x.any() == None:
            print('LU decomposition is impossible\n')
        elif x.any() != 0:
            print(f'Solution:\n{x}')
            print(f'Is solution correct? {np.allclose(np.dot(a, x), b)}')
            print('Third-party library:')
            print(np.linalg.solve(a, b))
            print()
    fp.close()
