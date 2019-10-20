'''
Author: DanLide
Date: 10.2019

A program applies Gauss method with a column-wise selection of the main element to the extended matrix
Finds solution of system of linear equations in the form of a vector X
Checks Ax = b condition
'''
import numpy as np

def matrix_max_row(matrix, n):
    '''
    matrix_max_row(matrix, n)
    Finds the largest element in a current column and rearranges the rows.

    Helps avoid rounding inaccuracy and division by zero.

    '''
    max_element = matrix[n][n]
    max_row = n

    for i in range(n + 1, len(matrix)):
        if abs(matrix[i][n]) > abs(max_element):
            max_element = matrix[i][n]
            max_row = i
        if max_element == 0:
            return None
        if max_row != n:
            matrix[n], matrix[max_row] = matrix[max_row], matrix[n]
            break
    return matrix

def is_singular(matrix):
    '''
    is_singular(matrix)
    Return True if the matrix is singular;
    Else returns False

    '''
    flag = False
    for i in range(len(matrix)):
        if not matrix[i][i]:
            flag = True
    return flag

def gauss_func(matrix):
    '''
    gauss_func(matrix)
    Applies the Gauss method with a column-wise selection of the main element to the extended matrix A.

    Returns a solution in the form of a vector X

    '''

    n = len(matrix)
    det = 1.0

    # Direct stroke
    for k in range(n - 1):
        matrix = matrix_max_row(matrix, k)
        if matrix == None:
            return
        for i in range(k + 1, n):
            m = -matrix[i][k] / matrix[k][k]
            matrix[i][-1] += m * matrix[k][-1]
            for j in range(k, n):
                matrix[i][j] += m * matrix[k][j]

    if is_singular(matrix):
        print('The system has an infinite number of solutions')
        print('Determinant: 0')
        return

    # Calculating determinant
    for i in range(n):
        det *= matrix[i][i]
    print(f'Determinant: {abs(det)}')

    # Return stroke
    for k in range(n - 1, -1, -1):
        x[k] = (matrix[k][-1] - sum([matrix[k][j] * x[j] for j in range(k + 1, n)])) / matrix[k][k]
    return x

if __name__ == "__main__":

    # First part
    fp = open('test.txt')

    for i in range(4):
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

        x = np.zeros(len(A))
        print('My solution:')
        x1 = gauss_func(A)

        if x.any() != 0:
            for i in range(len(x1)):
                print(f'x{i + 1} = {x1[i]}')
            print(f'Is solution correct? {np.allclose(np.dot(a, x1), b)}\n')
            print('Third-party library:')
            x2 = np.linalg.solve(a, b)
            print(f'Determinant: {np.linalg.det(a)}')
            for i in range(len(x2)):
                print(f'x{i + 1} = {x2[i]}')
            print(f'Is solution correct? {np.allclose(np.dot(a, x2), b)}')
    fp.close()
