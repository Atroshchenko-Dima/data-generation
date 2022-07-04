
import matplotlib.pyplot as plt

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# Назначение заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square", fontsize=14)
# Назначение размера шрифта на дальних на осях
ax.tick_params(axis="both", which='major', labelsize=14)

# назначение диапазона для каждой оси
ax.axis([0, 1200, 0, 1100000]) # x, x, y, y

plt.show()