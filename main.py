import time
from score import Score
from snake import Snake
from food import Food
from turtle import Turtle, Screen

# Creating Screen object and setting its properties
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(f"Feed the Python")
screen.tracer(0)

# Creating object of class Snake and Food
Buttercup = Snake()
food = Food()
score = Score()

# Using listen() method to set action for moving snake
screen.listen()
screen.onkey(Buttercup.up, "Up")
screen.onkey(Buttercup.down, "Down")
screen.onkey(Buttercup.left, "Left")
screen.onkey(Buttercup.right, "Right")

# Game logic
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    Buttercup.move()
    if Buttercup.head.distance(food) < 15:
        Buttercup.snake_grow()
        Buttercup.increase_speed()
        food.refresh()
        score.increase_score()

    if Buttercup.head.xcor() > 290:
        y_cor = Buttercup.head.ycor()
        Buttercup.head.goto(-290, y_cor)
    if Buttercup.head.xcor() < -290:
        y_cor = Buttercup.head.ycor()
        Buttercup.head.goto(290, y_cor)
    if Buttercup.head.ycor() > 275:
        x_cor = Buttercup.head.xcor()
        Buttercup.head.goto(x_cor, -290)
    if Buttercup.head.ycor() < -290:
        x_cor = Buttercup.head.xcor()
        Buttercup.head.goto(x_cor, 270)
        # game_is_on = False
        # score.game_over()

    # Condition for snake colliding with its tail
    for _ in Buttercup.snake_body[1: -1]:
        if Buttercup.head.distance(_) < 10:
            Buttercup.reset()
            score.reset()

screen.exitonclick()