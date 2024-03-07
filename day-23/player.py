from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.body = Turtle(shape="turtle")
        self.start()
    def start(self):
        self.hideturtle()
        self.body.penup()
        self.body.goto(STARTING_POSITION)
        self.body.left(90)
    def finish(self):
        if self.body.ycor() > FINISH_LINE_Y:
            self.body.goto(STARTING_POSITION)
    def up(self):
        self.body.fd(MOVE_DISTANCE)







