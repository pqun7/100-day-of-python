from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()


def move():
    turtle.fd(100)


screen.listen()
screen.onkey(key="l", fun=move)
screen.exitonclick()
