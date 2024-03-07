from turtle import Turtle, Screen
import pandas
from text import Text
screen = Screen()
turtle = Turtle()
text = Text()
screen.setup(725, 491)
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
file = pandas.read_csv(r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\100 Day\day-25\us-states-game-start\50_states.csv")
len_states = len(file["state"])
loop = 0

while loop < len_states:
    answer = screen.textinput(title=f"{loop + 1}/50 State Correct", prompt="Guess the state")
    loop += 1
    lower_answer = answer.lower()
    text.printStates(lower_answer)
    if answer == "exit":
        text.MissState()
        text.dic_to_csv()
        break


