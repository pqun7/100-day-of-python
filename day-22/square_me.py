from turtle import Turtle
class Square_Me(Turtle):
    def __init__(self):
        super().__init__()
        self.op = Turtle(shape="square")
        self.body()
    
        
    def body(self):
        self.op.shapesize(4, 0.5)
        self.op.color("white")
        self.op.penup()
        self.speed(10)
        self.op.goto(-380, 0)
        
    def Up(self):
        self.op.penup()
        new_yoc = self.op.ycor() + 20
        self.op.goto(self.op.xcor(), new_yoc)
        
    def Down(self):
        self.op.penup()
        new_yoc = self.op.ycor() - 20
        self.op.goto(self.op.xcor(), new_yoc)
