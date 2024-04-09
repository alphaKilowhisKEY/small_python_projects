"""
Turtle Race Game

This script simulates a race between turtles of different colors. Users can place bets on the winning turtle.

Dependencies:
    - Turtle: For creating turtle graphics.
    - Screen: For creating the race screen and handling user input.
    - random: For generating random numbers.

Usage:
    Run this script to start the turtle race game by: >>python3 turtle_race.py
    The user will be prompted to enter a color to bet on.
    The turtles will start racing, and the winner will be determined.
"""

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=800, height=700)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.shapesize(stretch_wid=3, stretch_len=3)
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()