STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

from turtle import Turtle 
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(2)
        self.penup()
        self.goto(STARTING_POSITION)
        self.right(-90)
    def move_y(self):
        new_y=self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
