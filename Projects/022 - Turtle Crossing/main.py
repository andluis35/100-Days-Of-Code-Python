import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def has_turtle_collided_with_car(game_turtle, game_cars):
    for car in game_cars:
        if game_turtle.distance(car) < 20:
            return True

    return False

def has_turtle_reached_end(game_turtle):
    if game_turtle.ycor() >= 320:
        return True
    else:
        return False

def start_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(fun=player.move, key="Up")

    game_is_on = True

    while game_is_on:
        car_manager.generate_car()
        car_manager.move_car()
        time.sleep(0.1)
        screen.update()

        if has_turtle_collided_with_car(player, car_manager.all_cars):
            scoreboard.game_over()
            game_is_on = False

        if has_turtle_reached_end(player):
            player.pass_level()
            scoreboard.update_scoreboard()
            car_manager.increase_cars_speed()

    screen.exitonclick()


start_game()
