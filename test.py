from turtle import Turtle
from turtle import Screen
import random

turtle = Turtle()
screen = Screen()

def draw_init():
    screen.setup(800, 600)
    screen.title("Merry Christmas Card")
    # turtle.setup(0.5, 0.75)
    turtle.pensize(5)
    turtle.speed(10)
    screen.bgcolor("white")
    screen.bgpic("snow.gif")
    turtle.getscreen().colormode(255)
    turtle.hideturtle()
    turtle.up()
    turtle.goto(100, -100)
    turtle.down()
    turtle.color("red", "green")

def draw_tree():
    turtle.begin_fill()
    for i in range(5):
        turtle.fd(90 - i * 10)
        turtle.lt(145)
        turtle.fd(130 - i * 10)
        turtle.rt(145)
    turtle.rt(145)
    global tree_x, tree_y
    tree_x = turtle.xcor()
    tree_y = turtle.ycor()
    
    for j in range(5):
        turtle.fd(90 + j * 10)
        turtle.lt(145)
        turtle.fd(50 + j * 10)
        turtle.rt(145)
    
    turtle.lt(145)
    turtle.fd(55)
    turtle.rt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(55)
    
    turtle.end_fill()
    
def draw_snow(num):
    turtle.speed("fastest")
    for i in range(num):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        turtle.dot(12, "white")
        
def brighten_star(r):
    turtle.pensize(3)
    turtle.speed("fastest")
    turtle.ht()
    turtle.up()
    turtle.goto(tree_x-r/2, tree_y+r/4)
    turtle.down()
    
    turtle.color("yellow")
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(r)
        turtle.right(144)
    turtle.end_fill()

    while True:
        turtle.color("orange")
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(r)
            turtle.right(144)
        turtle.end_fill()
        
        turtle.color("yellow")
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(r)
            turtle.right(144)
        turtle.end_fill()

def write(name):
    turtle.up()
    turtle.color("black")
    turtle.goto(-300, -200)
    turtle.write("Dear ", move = True, align = "left", font = ("Arial", 20, "normal"))
    turtle.goto(-220, -200)
    turtle.write(name, move = True, align = "left", font = ("Arial", 20, "normal"))
    turtle.goto(-200, -250)
    turtle.write("Merry Christmas!", move = True, align = "center", font = ("Arial", 20, "normal"))
    # turtle.write("\n")
    # turtle.write("Merry Christmas!")
    
# ==============================
# main

draw_init()
name = screen.textinput("First step", "請輸入你的名字：")
draw_tree()
draw_snow(50)
write(name)
brighten_star(50)

turtle.screen.mainloop()