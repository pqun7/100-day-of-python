from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()


def forward():
    turtle.fd(10)


def backwards():
    turtle.backward(10)


def counter_clockwise():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)


def clockwise():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)


def clear():
    turtle.reset()


screen.listen()
screen.onkey(forward, "w")
screen.onkey(backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()
