from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter your color: ").lower()
y_position = -100
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position)
    all_turtles.append(new_turtle)
    y_position += 50


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning color is {winning_color}.")
            else:
                print(f"You've lost! The winning color is {winning_color}.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.bye()
