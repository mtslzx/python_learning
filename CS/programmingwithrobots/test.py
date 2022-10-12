# https://stackoverflow.com/questions/15215103/sub-dots-in-python-classes

class Food(object):
    def kimchi(self):
        return 'mmm'

class country(object):
    def __init__(self):
        self.food = Food()

korea = country()
korea.food.kimchi()

print(korea.food.kimchi())