from math import sin, cos, sqrt

EPS = 0.5e-6


def f1(x):
    return ((x + 2)*sin(x))/(1 + x**2 + sqrt(cos(x)))


def f2(x):
    return (x**3)/(sin(0.8*x)*(1 + sin(0.8*x)))


def trapezoidal_rule(a, b, n, f):
    print(f'For n = {n}')
    h = (b - a) / n
    s = (f(a) + f(b)) / 2
    x = a + h

    for _ in range(n):
        s += f(x)
        x += h

    s *= h
    return s


def main(f):
    a = float(input('Enter A: '))
    b = float(input('Enter B: '))
    n = int(input('Enter N: '))
    print()

    res = trapezoidal_rule(a, b, n, f)
    print(f'Result for the integral: {res}\n')

    while True:
        n *= 2
        new_res = trapezoidal_rule(a, b, n, f)
        print(f'Result for the integral: {new_res}')
        error = abs(res - new_res)
        print(f'Error: {error}\n')
        if error < EPS:
            print('Accuracy is reached\n')
            break
        res = new_res


if __name__ == "__main__":
    main(f1)
    main(f2)