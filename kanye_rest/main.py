"""
Kanye Quotes GUI App

This Python script creates a simple GUI application using the tkinter library. 
The app displays a background image with a Kanye West quote in the center. 
There's also a button that, when clicked, fetches a random Kanye West quote from an API 
and updates the displayed quote.

Libraries Used:
- tkinter: for creating the GUI
- requests: for making HTTP requests to the API

Usage:
- Run the script to open the GUI window by: $ python3 main.py
- Click the Kanye image button to fetch and display a random Kanye West quote.

"""

from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    kanye_quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=kanye_quote)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()