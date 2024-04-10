"""
Flash Cards Application

This program implements a flash cards application that helps users learn French words and their English translations.

Dependencies:
    - pandas: for reading data from CSV files
    - tkinter: for creating the graphical user interface (GUI)
    - random: for randomly selecting flash cards

Usage:
    Run the script to launch the flash cards application: $python3 main.py
    
    Click the "Check" button to remove a card from the learning list if you know its translation,

    or 
    
    click the "Cross" button to proceed to the next card without removing it from the learning list.

"""

import pandas as pd
from tkinter import *
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ("Ariel", 40, "italic")
FONT_2 = ("Courier", 60, "bold")
data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
is_remove = False

# ---------------------------- NEXT CARD --------------------------------- #
def next_card():
    global flip_timer, is_remove

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=current_card["French"])

    if is_remove:
        to_learn.remove(current_card)
        is_remove = False

    flip_timer = window.after(3000, flip_card, current_card)
    
# ----------------------------FLIP THE CARD ------------------------------ #   
def flip_card(card):
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=card["English"])
    #next_card()

# ----------------------------REMOVE THE CARD ---------------------------- #  
def remove_card():
    global is_remove
    is_remove = True
    next_card()

# ---------------------------- UI SETUP ---------------------------------- #
#Main Window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#Front and Back Card Images
canvas = Canvas(width=800, height=526) 
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 260, image=card_front_img)
title_text = canvas.create_text(400, 120, text="", fill="black", font=FONT_1)
word_text = canvas.create_text(400, 300, text="", fill="black", font=FONT_2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#Button Cross
button_image_cross = PhotoImage(file="images/wrong.png")
cross_button = Button(image=button_image_cross, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

#Button Check
button_image_check = PhotoImage(file="images/right.png")
check_button = Button(image=button_image_check, highlightthickness=0, command=remove_card)
check_button.grid(column=1, row=1)

next_card()

window.mainloop()