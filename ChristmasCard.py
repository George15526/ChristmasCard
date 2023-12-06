# CristmasCard
from turtle import Turtle
from turtle import Screen

screen = Screen()
turtle = Turtle()

screen.title("Christmas Card")
screen.setup(500, 500)

GREEN = (0, 255, 0)

turtle.ht()
turtle.st()

turtle.up()
turtle.goto(0, 100)

turtle.write("Merry Christmas!", move = False, align = "center", font = ("Arial", 30))

turtle.goto(-100, 0)
turtle.down()
turtle.right(60)

screen.colormode(255)
turtle.fillcolor(6, 77, 0)
turtle.begin_fill()

for i in range(3):
    turtle.fd(50)
    turtle.rt(120)
    turtle.fd(20)
    turtle.lt(120)
turtle.rt(120)
turtle.fd(5)

turtle.lt(90)
turtle.fd(50)
turtle.rt(90)
turtle.fd(20)
turtle.rt(90)
turtle.fd(50)
turtle.lt(90)
turtle.fd(5)

for i in range(3):
    turtle.fd(20)
    turtle.rt(120)
    turtle.fd(50)
    turtle.lt(120)

turtle.end_fill()

turtle.screen.mainloop()