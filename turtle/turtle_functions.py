"""
Turtle Drawing Functions

This script contains various functions to draw different patterns and shapes using the Turtle module.

Dependencies:
    - Turtle: For creating turtle graphics.
    - Screen: For creating the drawing screen.
    - colorgram: For extracting colors from images.

Usage:
    Import this script and call the desired function(s) to draw various patterns and shapes using Turtle graphics by: >>python3 trutle_functions.py
    You can use these functions to create colorful and dynamic visualizations.
"""

from turtle import Turtle, Screen
import random
import colorgram

turtle = Turtle()
turtle.shape("turtle")

#returns dash line
def draw_dash_line():
    for i in range(50):
        if i % 2 == 0:
            turtle.penup()
            turtle.forward(5)
        else:
            turtle.pendown()    
            turtle.forward(5) 

# returns figures: triangle, square, pentagon...
def draw_figure(num_angles):
    angle = 360 / num_angles
    for _ in range(num_angles):
        turtle.right(angle)
        turtle.forward(100)

def draw_sequenz_figure(num_figures):
    for i in range(3, num_figures + 1):
        draw_figure(i)

# returns random walking of turtle
def random_walk():
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    directions = [0, 90, 180, 270]
    turtle.pensize(15)
    turtle.speed("fastest")       
    for _ in range(200):
        turtle.color(random.choice(colours))
        turtle.forward(30)
        turtle.setheading(random.choice(directions))

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# draw spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

# colorgram
def make_palette():
    rgb_colors = []        
    colors = colorgram.extract('gold_black.jpg', 2)  
    for color in colors:
        r = color.rgb.r    
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color) 
    return rgb_colors   


def draw_screen():
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.exitonclick()