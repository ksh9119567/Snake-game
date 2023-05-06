from turtle import Turtle

X_POSITION = [10, -10, -30]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for _ in range(0, 3):
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.speed(10)
            new_snake.penup()
            new_snake.speed(10)
            new_snake.goto(x=X_POSITION[_], y=0)
            self.snake_body.append(new_snake)

    def move(self):
        for _ in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[_ - 1].xcor()
            new_y = self.snake_body[_ - 1].ycor()
            self.snake_body[_].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def increase_speed(self):
        for _ in range(0, len(self.snake_body)):
            i = 10
            self.snake_body[_].speed(i)
            i -= 1

    def snake_grow(self):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        self.snake_body.append(new_snake)
        count = len(self.snake_body) - 1
        new_x = self.snake_body[count - 1].xcor()
        new_y = self.snake_body[count - 1].ycor()
        self.snake_body[count].goto(new_x, new_y)

    def reset(self):
        for _ in self.snake_body:
            _.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
