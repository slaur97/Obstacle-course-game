from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from car import Car
import time


screen=Screen()
screen.bgcolor("white")
screen.setup(width=600,height=600)
screen.tracer(0)


player=Player()
car=Car()
score=ScoreBoard()
screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")

start=True
up_score=True
while start:
    time.sleep(0.07)
    screen.update()
    car.create_objects()
    car.move_car()
    for cars in car.objects:
        if cars.distance(player) < 20:
            score.game_over()
            start=False
    
    if player.ycor()>285:
        up_score=True
        score.nivel+=1
        score.level()
        player.create_player()
        car.speed+=2
    if score.nivel ==5 and up_score==True:
        up_score=False
        car.random_number-=1
    if score.nivel ==7 and up_score==True:
        up_score=False
        car.random_number-=1
    if score.nivel ==13 and up_score==True:
        up_score=False
        car.random_number-=1
    if score.nivel == 16 and up_score==True:
        up_score=False
        car.random_number-=1
    if score.nivel ==16 and up_score==True:
        up_score=False
        car.random_number-=1

            
           
    
screen.exitonclick()