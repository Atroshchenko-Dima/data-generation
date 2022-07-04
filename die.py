from random import randint

class Die():
# Класс представляющий один кубик
    def __init__(self, num_sides=6): # шестигранный кубик
        self.num_sides = num_sides
    
    def roll(self):
        # возвращает одно число от 1 до числа граней(6)
        return randint(1, self.num_sides)
        