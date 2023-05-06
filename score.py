from turtle import Turtle

ALIGN = 'center'
FONT = ("Arial", 16, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.your_score = 0
        self.high_score = 0
        self.pencolor('white')
        self.penup()
        self.goto(0, 278)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 278)
        with open("High_Score.txt") as file:
            score = file.read()
        self.write(f'Score: {self.your_score}  High Score: {score}', True, 'center', ("Arial", 16, "normal"))

    def reset(self):
        if self.high_score < self.your_score:
            self.high_score = self.your_score
            self.save_score()
        self.your_score = 0
        self.update_score()

    def save_score(self):
        with open("High_Score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", True, ALIGN, FONT)

    def increase_score(self):
        self.your_score += 1
        self.update_score()