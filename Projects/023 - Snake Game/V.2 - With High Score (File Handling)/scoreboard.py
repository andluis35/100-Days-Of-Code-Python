from turtle import Turtle
from time import sleep

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.color("white")
        self.penup()
        self.clear()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.get_high_score()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"| Score: {self.score} | High Score: {self.high_score} |", align=ALIGNMENT, font=FONT)

    def reset(self):
        sleep(1)
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        with open("highscore.txt") as file:
            self.high_score = int(file.read())

    def set_high_score(self):
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.score))