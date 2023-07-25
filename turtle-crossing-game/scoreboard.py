FONT = ("Arial", 25, "bold")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.goto(-280,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level}",align="left",font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        
    
