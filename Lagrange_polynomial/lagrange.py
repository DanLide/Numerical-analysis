import numpy as np
import matplotlib.pyplot as plt


def lagrange(x, y, t):
    '''
    def lagrange(x, y, t)
    Знаходить значення інтерполяційого поліному Лагранжа в точці t, що є наближенням до значення заданої функції.

    Приймає на вхід вузли інтерполяції x, значення заданої функції у вузлах інтерполяції y,
    точку t, в якій ми хочемо знайти значення поліному.
 
    Повертає значення поліному.
    '''
    polynom_value = 0

    for i in range(len(y)):
        numerator = 1
        denominator = 1

        for j in range(len(x)):
            if i != j:
                numerator = numerator * (t - x[j])
                denominator = denominator * (x[i] - x[j])

        polynom_value += y[i] * numerator / denominator
    return polynom_value


def main():
    x = np.array([-5, -1.6, -0.8, -0.2, 0.6], dtype=float)
    y = np.array([-2.31, -1.25, -0.73, -0.2, 0.57], dtype=float)

    # Точки, в яких ми хочемо знайти значення поліному
    x_new = np.linspace(np.min(x), np.max(x), 100)

    # Значення поліному в точках x_new
    y_new = [lagrange(x, y, i) for i in x_new]

    # Малюємо графік з отриманих значень функції, позначаємо вузли інтерполяції
    plt.plot(x, y, 'o', x_new, y_new)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
