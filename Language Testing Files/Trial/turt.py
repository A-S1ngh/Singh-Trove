import turtle
from turtle import *

def square():
    for i in range(4):
        turtle.forward(25)
        turtle.right(90)

def cooldrawing():
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()

square()
