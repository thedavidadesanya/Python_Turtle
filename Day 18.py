#from turtle import Turtle,Screen #import everything by using the asterisk "*"
import turtle
import random


turtle.colormode(255)
tim = turtle.Turtle()

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


color_list = ["red", "green", "black", "blue", "yellow", "coral", "pink"]

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
        #tim.color(random.choice(color_list))
        tim.pencolor(random_color())



def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)

#random_walk()

def spirograph(size_of_gap):
    tim.speed("fast")
    for x in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)


spirograph(5)
#print(dir(Turtle))


screen = turtle.Screen()
screen.exitonclick()