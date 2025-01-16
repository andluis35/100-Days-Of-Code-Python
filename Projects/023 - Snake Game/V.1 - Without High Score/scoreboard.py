from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.clear()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.show_scoreboard()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.show_scoreboard()

    def show_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)