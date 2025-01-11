import random
from turtle import Turtle, Screen

paint_color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

t = Turtle()
screen = Screen()
screen.colormode(255)

t.penup()
t.ht()
t.setx(-250)
t.sety(-250)
t.speed("fastest")

number_of_dots = 0

while number_of_dots < 100:
    for _ in range(10):
        t.dot(20, random.choice(paint_color_list))
        t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.right(180)
    number_of_dots += 10

screen.exitonclick()