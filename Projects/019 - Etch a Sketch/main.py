from turtle import Turtle, Screen

def move_forwards():
    t.forward(20)

def move_backwards():
    t.backward(20)

def turn_counterclockwise():
    t.left(10)

def turn_clockwise():
    t.right(10)

def clear_drawing():
    t.penup()
    t.clear()
    t.home()
    t.pendown()


t = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
