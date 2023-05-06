import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("green")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = int(random.randint(-260, 260))
        random_y = int(random.randint(-260, 240))
        self.goto(random_x, random_y)
