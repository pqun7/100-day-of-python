import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "w")
screen.onkey(player.up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    if player.body.ycor() > 280:
        player.finish()
        scoreboard.add_score()
        cars.speed()

    for carss in cars.sug:
        if player.body.distance(carss) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()