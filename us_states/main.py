"""
U.S. States Game

This game allows users to guess the names of U.S. states. 
When a correct state name is guessed, the game displays the name of the state at its corresponding location
on the map.

Dependencies:
    - pandas: For data manipulation
    - turtle: For graphics

Instructions:
    1. Run this script to start the U.S. States Game by: >> python3 main.py
    2. Enter the name of a U.S. state when prompted.
    3. If the state name is correct, the game will display the name at its location on the map.
    4. Continue guessing until all 50 states are correctly guessed.
    5. Click anywhere on the screen to exit the game.

Data Files:
    - "50_states.csv": CSV file containing the coordinates of U.S. states.

"""
import pandas, turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_clicl_coor(x, y):
    print(x, y)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:
    guess_state = screen.textinput(title=f"{len(guess_states)} / 50 correct", prompt="Give a State name")
    title_guess = guess_state.title()

    if title_guess in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == title_guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(title_guess)
        guess_states.append(title_guess)

screen.exitonclick()