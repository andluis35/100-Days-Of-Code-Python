from turtle import Turtle

AMOUNT_TO_MOVE = 20

class Paddle(Turtle):

    def __init__(self, initial_coordinates):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(initial_coordinates)

    def up(self):
        if self.ycor() <= 220:
            new_y = self.ycor() + AMOUNT_TO_MOVE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() >= -220:
            new_y = self.ycor() - AMOUNT_TO_MOVE
            self.goto(self.xcor(), new_y)