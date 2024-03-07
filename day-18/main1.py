import random
import turtle as t

timmy = t.Turtle()
t.colormode(255)
timmy.pensize(9)
timmy.speed(10)

def random_color():
    r = random.randint(1.0, 255)
    g = random.randint(1.0, 255)
    b = random.randint(1.0, 255)
    random_color = (r, g, b)
    return random_color

rod = [0, 90, 180, 360, 270]
for i in range(0, 90):
    timmy.color(random_color())
    timmy.fd(20)
    timmy.setheading(random.choice(rod))

screen = Screen()
screen.exitonclick()
