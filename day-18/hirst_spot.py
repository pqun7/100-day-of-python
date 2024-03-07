# import colorgram
# rgb_color = []
# colors = colorgram.extract('imgg.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)
import random
import turtle as t
from turtle import Screen

t.colormode(255)
color_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253),
              (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40,
                                                             154), (212, 76, 15), (17, 153, 17), (241, 36, 161),
              (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15,
                                                            8), (223, 141, 206), (11, 97, 62), (219, 159, 11),
              (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74,
                                                              212), (10, 228, 238), (73, 212, 168), (93, 233, 198),
              (65, 231, 239), (217, 88, 51)]


def color_rgb():
    random_color = random.choice(color_list)
    return random_color


tur = t.Turtle()
tur.speed(100)
tur.penup()
tur.hideturtle()
tur.setheading(225)
tur.fd(300)
tur.setheading(0)
dot = 100

for i in range(1, dot + 1):
    tur.dot(size=15)
    tur.forward(50)
    tur.color(color_rgb())
    if i % 10 == 0:
        tur.setheading(90)
        tur.fd(50)
        tur.setheading(180)
        tur.fd(500)
        tur.setheading(0)


tur.penup()


tur.hideturtle()

screen = Screen()
screen.exitonclick()
