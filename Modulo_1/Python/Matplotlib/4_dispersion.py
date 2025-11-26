import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, alpha=0.5)
plt.title("Dispersión Aleatoria")
plt.show()
