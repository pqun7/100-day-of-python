from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball()
        self.y = 10
        self.x = 10
    
    def ball(self):
        self.shape("circle")
        self.shapesize(0.5)
        self.color("white")
        self.penup()
    
    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)
    
    def move_again(self):
        self.goto(0, 0)
        self.move()
    
    def bounce(self):
        self.y *= -1
    
    def bounce_back(self):
        self.x *= -1
         
