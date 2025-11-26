import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [1, 2, 3]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Gráfico 1")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Gráfico 2")

plt.show()
