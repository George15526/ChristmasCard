from turtle import Turtle
from turtle import Screen
import random

turtle = Turtle()
screen = Screen()
screen.setup(800, 600)


def f():
    running = True
    while running:
        turtle.fd(50)
        turtle.lt(60)

screen.ontimer(f, 1000)   
# f()   ### makes the turtle march around
running = False

turtle.screen.mainloop()