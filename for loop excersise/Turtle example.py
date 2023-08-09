import turtle
from random import random
lines = 150
screen = turtle.Screen()
screen.title("Turtle")
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(50)
side_length = 5

for x in range(lines):
    pen.pencolor(((lines-x)/lines, random(), x/lines))
    pen.width(3 - x // 50)
    pen.forward(side_length)
    side_length = side_length + 1 + x/200
    pen.left(61)
turtle.done()
