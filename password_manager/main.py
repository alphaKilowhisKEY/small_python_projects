"""
This script implements a simple password manager using Tkinter for the user interface and Pandas 
for handling JSON file operations.

The script provides the following functionalities:
1. Generate a random password
2. Save password entries (Website, Email/Username, Password) to a JSON file
3. Check if the data already exists in the JSON file before adding new entries
4. Display error/warning messages using Tkinter messagebox

Dependencies:
- Tkinter: For creating the graphical user interface (GUI)
- Random: For generating random passwords
- JSON

Usage:
    Run this script:  $python3 main.py.

"""

import json
from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Courier", 12, "bold")
FILE_PATH = "entries_dict.csv"

# ---------------------------- SEARCH FUNCTION---- ---------------------- #
def search():

    website = website_input.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- PASSWORD GENERATOR ---------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    total_symbols_list = (letters + digits + symbols)
    random.shuffle(total_symbols_list)

    password = ""

    for _ in range(8):
        password += random.choice(total_symbols_list)

    password_input.delete(0, END)  
    password_input.insert(0, password)  

# ---------------------------- SAVE PASSWORD --------------------------- #
def add_entries():

    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    new_data = {
            website: {
                'username': username,
                'password': password,
            }
        }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="No empty fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP -------------------------------- #
#Main Window
window = Tk()
#window.minsize(width=400, height=400)
window.title("Password Manager")
window.config(padx=30, pady=30)

#Logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Website Label
website = Label(text="Website:", font=FONT)
website.grid(column=0, row=1)

#Website Input
website_input = Entry(width=28)
website_input.grid(column=1, row=1)
website_input.focus()

#Email/Username Label
username = Label(text="Email/Username:", font=FONT)
username.grid(column=0, row=2)

#Email/Username Input
username_input = Entry(width=53)
username_input.insert(0, "username@email.com")
username_input.grid(column=1, row=2, columnspan=2)

#Password Label
password = Label(text="Password:", font=FONT)
password.grid(column=0, row=3)

#Password Input
password_input = Entry(width=28)
password_input.grid(column=1, row=3)

#Search Button
search_button = Button(text="Search", font=FONT, width=17, command=search)
search_button.grid(column=2, row=1)

#Generate Password Button
generate_passw_button = Button(text="Generate Password", font=FONT, command=generate_password)
generate_passw_button.grid(column=2, row=3)

#Add Button
add_button = Button(text="Add", width=40, font=FONT, command=add_entries)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()