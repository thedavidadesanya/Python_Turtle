import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

def move_forwards():
    """moves turtle cursor forwards"""
    tim.forward(10)

def move_backwards():
    """moves turtle cursor backwards"""
    tim.backward(10)

def clockwise():
    "changes angle of cursor clockwise"
    tim.right(10)

def counterclockwise():
    """changes angle of cursor counterclockwise"""
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key ="w", fun=move_forwards) #higher order function takes the input of another function
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counterclockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()