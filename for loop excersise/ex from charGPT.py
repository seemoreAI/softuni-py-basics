import turtle
from random import random
lines = 150
screen = turtle.Screen()
screen.title("Turtle")
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(10)
pen.width
side_length = 5

for x in range(lines):
    pen.pencolor(((lines-x)/lines, random(), x/lines))
    pen.width(x // 30)
    pen.forward(side_length)
    side_length = side_length + 1 + x/200
    pen.left(60.2)
turtle.done()
