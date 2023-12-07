from turtle import Turtle
from turtle import Screen
import random

turtle = Turtle()
screen = Screen()
screen.setup(800, 600)

turtle.shape("square")
turtle.up()
turtle.goto(-330, -180)
turtle.down()
turtle.shapesize(130, 50)

turtle.screen.mainloop()