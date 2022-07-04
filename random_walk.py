from random import choice # для принятия случайных решений

class RandomWalk():

    def __init__(self, num_points=5000):
        #Инициализирует атрибуты блуждания
        self.num_points = num_points
        # все блуждания начинаются с точки ноль
        self.x_values =[0]
        self.y_values = [0]

    def get_step(self): # рефакторинг
        """Determine the direction and distance for a step."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step    

    def fill_walk(self):
        # шаги генерируются до нужной длины
        while len(self.x_values) < self.num_points: # запускаем цикл, пока точек не станет 5000
            # определение направления и длины перемещения 
            x_step = self.get_step() 
            y_step = self.get_step()
        # отклонение нулевых перемещений
            if x_step == 0 and y_step ==0:
                continue

            # Вычисление следующих значений х и у
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            x = self.x_values.append(x)
            y = self.y_values.append(y)
