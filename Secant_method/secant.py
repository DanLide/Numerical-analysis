import math
import numpy as np
import matplotlib.pyplot as plt

def f(x: float) -> float:
    '''
    def f(x: float) -> float
    Знаходить значення функції x^2 - 20*sin(x).

    Приймає на вхід незалежну змінну x типу float.
 
    Повертає значення функції x^2 - 20*sin(x).
    '''
    return x ** 2 - 20 * np.sin(x)


def second_derivative(x, delta_x):
    '''
    def second_derivative(x, delta_x)
    Знаходить значення другої похідної в точці x.

    Приймає на вхід дійсне число x та досить мале число delta_x.
 
    Повертає значення другої похідної в точці x.
    '''
    return (f(x + delta_x) - 2 * f(x) + f(x - delta_x)) / delta_x ** 2


def secant(a, b, eps=1e-6):
    '''
    def secant(a, b, eps=1e-6)
    Ітеративний метод, що уточнює корінь рівняння f(x) = 0 на заданому відрізку [a, b],
    де f(x) - неперервна, монотонна нелінійна функція, яка на відрізку [a, b] монотонна,
    диференційована, f(a)*f(b) < 0, b - a > eps.

    Приймає на вхід початок відрізка а, кінець відрізка b та точність eps.
 
    Повертає корінь рівняння x та True,
    якщо дотримані початкові умови (симетричність матриці А),
    інакше False.
    '''
    if f(a) * f(b) >= 0 or b - a < eps:
        return 0, False

    z = b

    # Якщо кінець b нерухомий, то z набуває значення рухомого кінця
    if f(b) * second_derivative(b, eps) > 0:
        z = a

    # Формула для розрахунку кореня x на першій ітерації
    x1 = z - ((f(z) * (b - a)) / (f(b) - f(a)))
    x_prev = 0
    x = x1

    k = 0
    while abs(x - x_prev) >= eps:
        x_prev = x
        k += 1
        x = x_prev - ((f(x_prev) * (b - x_prev)) / (f(b) - f(x_prev)))

    print()
    print(f'Iterations: {k}\n')

    return x, True


def main():
    # Зчитуємо з потоку вводу a і b (перетворюючи у тип float), виконуємо метод хорд
    x, conditions_met = secant(float(input('a: ')), float(input('b: ')))

    if conditions_met:
        print(f'x = {x}')
    else:
        print('Equation has any or more than one solution')

    # Знаходимо значення заданої функції у деякому діапазоні
    y = lambda x: f(x)
    x_func = np.linspace(-5, 5, 1000)

    # Для зручності малюємо на графіку x = 0
    plt.axhline(0, color='black', linewidth="0.5")

    # Малюємо графік функції
    plt.plot(x_func, y(x_func))

    if conditions_met:
        # Позначаємо знайдений корінь рівняння x на графіку
        plt.plot(x, 0, color='red', marker='o',
            linewidth=3, markersize=3)

    plt.show()


if __name__ == "__main__":
    main()
