import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] # subplots - позволяет сгенерировать 1 или несколько диаграмм на одном рисунке
plt.style.use('seaborn') # выбор стиля графика
fig, ax = plt.subplots() # fig - весь рисунок или набор генерируемых диаграмм. ах - одна диаграмма на рисунке
ax.plot(input_values, squares, linewidth=3)
# plot - строит осмысленное графическое представление для данных чисел
# назначение заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=24) # заголовок диаграммы
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Назначение размера шрифта делений на осях
ax.tick_params(axis="both", labelsize=14)
plt.show()
