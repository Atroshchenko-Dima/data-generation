from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# создание кубика Д6
die = Die()
# Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(1000):
    result = die.roll() # результат 1 броска кубика
    results.append(result) # добавление в список всех бросков

# Анализ результатов
frequancies = []
for value in range(1, die.num_sides+1): # подсчитывает кол-во вхождений каждого числа в результат
    frequency = results.count(value) # присоединяет полученное значение к списку
    frequancies.append(frequency)

# Визуализация результатов
x_values = list(range(1, die.num_sides+1)) # чтоб создать столбцовую диаграмму, создаем столбец для каждого из возможных результатов
# plotly не может получить результат функции range, поэтому преобразовываем диапазон в список
data = [Bar(x=x_values, y=frequancies)] # Bar - набор данных, который будет формироваться в виду столбцовой диаграммы

# задаем заголовки осей
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
# класс Layout возвращает объект, который задает макет и конфигурацию диаграммы в целом.
my_layout = Layout(title = 'Results of rolling one D6 1000 times', 
        xaxis=x_axis_config, yaxis=y_axis_config ) # задается заголовок диаграммы и передаются словари конфигурации осей
# вызов диаграммы, передаем словарь с объектами данныхи макета и имя файла для сохранения результата
offline.plot({'data' : data, 'layout' : my_layout}, filename='d6.html')