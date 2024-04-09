"""
Simple Turtle Drawing

This script enables users to control a turtle using keyboard inputs to draw on the screen. The turtle can move forwards,
backwards, turn left, turn right, and reset its position.

Dependencies:
    - Turtle: For creating turtle graphics.
    - Screen: For creating the drawing screen.

Usage:
    Run this script to open a drawing window with a turtle by: >> python3 turtle_event.py
    Use the following keys to control the turtle:
        - 'w': Move forwards
        - 's': Move backwards
        - 'a': Turn left
        - 'd': Turn right
        - 'c': Reset position
    Click on the drawing window to close it.
"""

from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
screen = Screen()

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)   

def turn_left():
    turtle.left(10)

def turn_right():
    turtle.right(10)  

def reset():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()           

screen.listen()
screen.onkey(key="w", fun=move_forwards) 
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)
screen.exitonclick()
   