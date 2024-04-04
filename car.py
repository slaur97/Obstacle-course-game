from turtle import Turtle
import random
import time
color=['blue','orange','red','yellow','red','black']
class Car(Turtle):
    def __init__(self):
        self.objects=[]
        self.speed=15
        self.random_number=6
    
    def create_objects(self):
        random_ch=random.randint(1,self.random_number)
        if random_ch == 1:
            new_car=Turtle("square")
            new_car.color(random.choice(color))
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            coordonate_start_x=290
            coordonate_start_y=random.randint(-260,270)
            new_car.goto(coordonate_start_x,coordonate_start_y)
            self.objects.append(new_car)

    def move_car(self):
        for car in self.objects:
            car.backward(self.speed)

    

    