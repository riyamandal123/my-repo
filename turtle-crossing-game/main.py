import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player=Player()
scoreboard=Scoreboard()

screen.listen()
#use the up arrow key to move the turtle.
screen.onkey(player.move_y,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    #detect the collision with car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #detect when the player has reached the other side.
    if player.ycor() > 280:
        #player goes to the initial position.
        player.goto(0,-280)
        #cars speed is increased ever time the player goes to initial position.
        car_manager.increse_car_speed()
        #game level is also increased.
        scoreboard.increase_level()
        


screen.exitonclick()
