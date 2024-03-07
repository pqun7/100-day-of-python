from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.heading()
        self.hideturtle()
        self.board_update()
    
    def board_update(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}", align= "center", font= ("Arial", 24, "normal"))
    

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.board_update()

    def reset_scoer(self):
        self.score = 0
        self.clear()
        self.board_update()
    def add_score(self):
        self.score += 1
        self.clear()
        self.board_update()
            