import turtle
from turtle import Turtle, Screen
import random

race_on=False
screen=Screen()
screen.setup(width=500,height=400)
bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
yp=[-70,-40,-10,20,50,80]
l=[]

for t in range(0,6):
    tim = Turtle("turtle")
    tim.penup()
    tim.goto(x=-230, y=yp[t])
    tim.color(colors[t])
    l.append(tim)
if bet:
    race_on=True

while race_on:
    for i in l:
        if i.xcor()>230:
            race_on=False
            wincolor=i.pencolor()
            if wincolor==bet:
                print("You have won.")
            else:
                print("You have lost.")
        d=random.randint(0,10)
        i.forward(d)


screen.exitonclick()
