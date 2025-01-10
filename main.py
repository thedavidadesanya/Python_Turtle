import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width =500, height =400)
user_bet = screen.textinput(title="Make your bet!!", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "orange","yellow","green", "blue", "purple"]
y_axis = -100 #could also just create a list
all_turtles = []
for x in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-250,y=y_axis)
    y_axis += 30
    all_turtles.append(new_turtle)



if user_bet:
    is_race_on = True

while is_race_on:

    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won the game! The winning turtle is {winning_color}")
            else:
                print(f"You've lost! The winning turtle is {winning_color}")
        distance = random.randint(0,10)
        t.forward(distance)

screen.exitonclick()