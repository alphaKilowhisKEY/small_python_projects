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