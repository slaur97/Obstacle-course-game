from turtle import Turtle
coordonate_start_x=0
coordonate_start_y=-270
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()
    def create_player(self):
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(coordonate_start_x,coordonate_start_y)
        self.setheading(90)
    
    def up(self):
        self.new_y=self.ycor()+20
        self.new_x=self.xcor()
        self.goto(self.new_x,self.new_y)
    def down(self):
        if self.ycor() > -290:
            self.new_y=self.ycor()-20
            self.new_x=self.xcor()
            self.goto(self.new_x,self.new_y)