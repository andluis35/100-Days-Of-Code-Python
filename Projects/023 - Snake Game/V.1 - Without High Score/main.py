from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def has_snake_collided_with_food(game_snake, game_food):
    if game_snake.head.distance(game_food) < 15:
        return True
    else:
        return False

def has_snake_collided_with_wall(game_snake):
    if game_snake.head.xcor() > 290 or game_snake.head.xcor() < -290 or game_snake.head.ycor() > 290 or game_snake.head.ycor() < -290:
        return True
    else:
        return False

def has_snake_collided_with_tail(game_snake):
    for segment in game_snake.segments[1:]:
        if game_snake.head.distance(segment) < 10:
            return True

    return False

def start_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    game_is_on = True

    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if has_snake_collided_with_food(snake, food):
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if has_snake_collided_with_wall(snake):
            game_is_on = False
            scoreboard.game_over()

        if has_snake_collided_with_tail(snake):
            game_is_on = False
            scoreboard.game_over()

    screen.exitonclick()


start_game()
