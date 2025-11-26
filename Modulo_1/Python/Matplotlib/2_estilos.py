import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, color='red', linestyle='--', marker='o', label='Cuadrados')
plt.legend()
plt.grid(True)
plt.show()
