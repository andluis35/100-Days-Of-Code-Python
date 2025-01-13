from turtle import Turtle, Screen
import random

def create_all_turtles():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_coordinates = [-100, -60, -20, 20, 60, 100]
    turtles_list = []

    for i in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(-230, y_coordinates[i])
        turtles_list.append(new_turtle)

    return turtles_list

def define_winner(color, user_choice):
    print("\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    if color == user_choice.lower():
        print(f"You've won! The {color} turtle is the winner!")
    else:
        print(f"You lose! The {color} turtle is the winner!")
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

def start_race():
    screen = Screen()
    screen.setup(width=500, height=400)
    is_race_on = False
    all_turtles = []
    user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

    if user_bet:
        is_race_on = True
        all_turtles = create_all_turtles()

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                define_winner(winning_color, user_bet)
                is_race_on = False

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

    screen.exitonclick()


start_race()
