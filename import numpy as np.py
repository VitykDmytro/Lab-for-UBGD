import numpy as np
import matplotlib.pyplot as plt

def sinc(x):
    if x == 0:
        return 1
    else:
        return np.sin(x) / x

def f(x, N):
    return sinc(2 * x * N - 1)

x_values = np.linspace(-10, 10, 1000)

N = 3
y_values = f(x_values, N)

plt.plot(x_values, y_values, label=f'N = {N}')
plt.title('Графік функції f(x) = sinc(2xN - 1)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
