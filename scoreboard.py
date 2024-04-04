from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.nivel=1
        self.level()
    def level(self):
        self.clear()
        self.penup()
        self.goto(x=-260,y=280)
        self.write(f"Level:{self.nivel}",align="center",font=("Arial",13,"normal"))
        self.hideturtle()
    def game_over(self):
        self.penup()
        self.color("blue")
        self.goto(x=0,y=0)
        self.write("Game Over",align="center",font=("Arial",13,"normal"))
        self.hideturtle()