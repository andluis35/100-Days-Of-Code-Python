from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 48, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_player_score = 0
        self.left_player_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_player_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_player_score, align=ALIGNMENT, font=FONT)

    def left_point(self):
        self.left_player_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_player_score += 1
        self.update_scoreboard()