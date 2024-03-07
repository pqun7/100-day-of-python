FONT = ("Courier", 15, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-230, 260)
        self.hideturtle()
        self.board_update()

    def board_update(self):
        self.write(f"score: {self.score}", align="center", font=FONT)


    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"score: {self.score}", align="center", font=FONT)
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 24, "normal"))
        self.goto(-50, -20)
        self.write(f"score: {self.score}", align="center", font=FONT)
