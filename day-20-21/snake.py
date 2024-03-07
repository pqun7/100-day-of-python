from turtle import Turtle
STARTING_POSITIONS = ((0, 0),(-20,0),(-40,0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.hade = self.segments[0]

    
    def create_snake(self):
        global STARTING_POSITIONS, SCORE
        for body in STARTING_POSITIONS:
            self.add_segment(body)
            
    
    def add_segment(self, body):
        snake = Turtle(shape="square")
        snake.penup()
        snake.goto(body)
        snake.color("white")
        self.segments.append(snake)
    def reset(self):
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.hade = self.segments[0]
    
    def exdend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.hade.heading() != DOWN:
            self.hade.setheading(UP)

    def down(self):
        if self.hade.heading() != UP:
            self.hade.setheading(DOWN)

    def left(self):
        if self.hade.heading() != RIGHT:
            self.hade.setheading(LEFT)

    def right(self):
        if self.hade.heading() != LEFT:
            self.hade.setheading(RIGHT)
