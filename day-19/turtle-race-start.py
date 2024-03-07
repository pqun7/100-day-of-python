from turtle import Turtle, Screen
import random
# race_is_run = False
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "yellow", "orange", "green", "purple"]
y_pos = [-70, -40, -10, 20, 50, 75]
all_turtle = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtle.append(new_turtle)

    if user_bet:
        race_is_run = True

    while race_is_run:
        for turtle in all_turtle:
            if turtle.xcor() > 200:
                race_is_run = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(
                        f"You'v win!!, The {winning_color} turtle is the winner!")
                else:
                    print(
                        f"You'v lost!!, The {winning_color} turtle is the winner!")
            ran = random.randint(0, 10)
            turtle.forward(ran)


    screen.exitonclick()
