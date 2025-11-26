import matplotlib.pyplot as plt

categorias = ['Manzanas', 'Peras', 'Naranjas']
cantidad = [20, 35, 30]

plt.bar(categorias, cantidad, color=['red', 'green', 'orange'])
plt.title("Frutas")
plt.show()
