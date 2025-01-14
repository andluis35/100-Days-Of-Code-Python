from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def has_ball_collided_with_wall(game_ball):
    if game_ball.ycor() >= 290 or game_ball.ycor() <= -290:
        return True
    else:
        return False

def has_ball_collided_with_paddle(game_ball, r_paddle, l_paddle):
    if ((game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 320) or
        (game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -320)):
        return True
    else:
        return False

def has_right_paddle_missed(game_ball):
    if game_ball.xcor() >= 420:
        return True
    else:
        return False

def has_left_paddle_missed(game_ball):
    if game_ball.xcor() <= -420:
        return True
    else:
        return False

def start_game():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    right_paddle = Paddle( (350, 0) )
    left_paddle = Paddle( (-350, 0) )
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(fun=left_paddle.up, key="w")
    screen.onkey(fun=left_paddle.down, key="s")
    screen.onkey(fun=right_paddle.up, key="Up")
    screen.onkey(fun=right_paddle.down, key="Down")

    game_is_on = True

    while game_is_on:
        screen.update()
        ball.move()
        time.sleep(ball.move_speed)

        if has_ball_collided_with_wall(ball):
            ball.bounce_y()

        if has_ball_collided_with_paddle(ball, right_paddle, left_paddle):
            ball.bounce_x()

        if has_right_paddle_missed(ball):
            scoreboard.left_point()
            ball.reset_position()

        if has_left_paddle_missed(ball):
            scoreboard.right_point()
            ball.reset_position()

    screen.exitonclick()


start_game()
