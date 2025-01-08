from turtle import Turtle,Screen #import everything by using the asterisk "*"
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

def direction_change():
    for x in range(4):
        tim.forward(100)
        tim.right(90)


def dashed_lines():
    for x in range(10):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)


color_list = ["red", "green", "black", "blue", "yellow", "coral"]

def shape_generator():
    for x in range(3, 10):
        tim.color(random.choice(color_list))
        for y in range(x):
            tim.right(360/x)
            tim.forward(100)


def random_walk():
    tim.speed(10)
    tim.pensize(5)
    directions = [0, 90, 180, 270]
    for x in range(200):
        tim.forward(30)
        tim.setheading(random.choice(directions))
        tim.color(random.choice(color_list))


random_walk()

screen = Screen()
screen.exitonclick()