from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
class CarManager:
    def __init__(self):
        super().__init__()
        self.sug = []

    def create_car(self):
        random_co = random.randint(0, 6)
        if random_co == 1:
            self.body = Turtle(shape="square")
            self.body.shapesize(1, 3)
            self.body.color(random.choice(COLORS))
            self.body.penup()
            Y_RAN = random.randint(-250, 300)
            X_RAN = random.randint(300, 500)
            self.body.goto(X_RAN, Y_RAN)
            self.sug.append(self.body)
    def move(self):
        for car in self.sug:
            car.backward(STARTING_MOVE_DISTANCE)
    def speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += 5

