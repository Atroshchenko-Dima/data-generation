from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# создание кубика Д6
die_1 = Die()
die_2 = Die() # можем изменить кол-во граней вписав в скобки. Стандартно их 6
# Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() # результат 1 броска кубиков
    results.append(result) # добавление в список всех бросков
print(results)
# Анализ результатов
frequancies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1): # подсчитывает кол-во вхождений каждого числа в результат
    frequency = results.count(value) # присоединяет полученное значение к списку
    frequancies.append(frequency)

# Визуализация результатов
x_values = list(range(2, max_result+1)) # чтоб создать столбцовую диаграмму, создаем столбец для каждого из возможных результатов
# plotly не может получить результат функции range, поэтому преобразовываем диапазон в список
data = [Bar(x=x_values, y=frequancies)] # Bar - набор данных, который будет формироваться в виду столбцовой диаграммы

# задаем заголовки осей
x_axis_config = {'title': 'Result', 'dtick' : 1} # 'dtick' : 1 - приказывает plotly помечать все деления
y_axis_config = {'title': 'Frequency of Result'}
# класс Layout возвращает объект, который задает макет и конфигурацию диаграммы в целом.
my_layout = Layout(title = 'Results of rolling two D6 dice 1000 times', 
        xaxis=x_axis_config, yaxis=y_axis_config ) # задается заголовок диаграммы и передаются словари конфигурации осей
# вызов диаграммы, передаем словарь с объектами данныхи макета и имя файла для сохранения результата
offline.plot({'data' : data, 'layout' : my_layout}, filename='d6_d6.html')