from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.player_level += 1
        self.goto(x=-280, y=250)
        self.write(arg=f"Level: {self.player_level}", font=FONT)

    def game_over(self):
        self.goto(x=-85, y=0)
        self.write(arg="GAME OVER", font=FONT)