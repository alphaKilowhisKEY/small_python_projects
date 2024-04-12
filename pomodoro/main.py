"""
Pomodoro Timer Application

This application implements a Pomodoro timer, which is a time management technique that
breaks work into intervals, traditionally 25 minutes in length, separated by short and long breaks.

It features a graphical user interface built with Tkinter.

Usage:
    Run this script to start the Pomodoro timer application by:
    $ python3 main.py

"""

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e72929"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM --------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)    
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------ # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text="{:.0f}:{:02.0f}".format(count_min, count_sec))

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PoMoDoRo")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")

#Label Timer
title_label = Label(text="Timer", bg=YELLOW, fg=RED, font=(FONT_NAME, 30, "bold"))
title_label.grid(column=1, row=0)

# Tomato Picture 
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

#Button Start
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

#Button Reset
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

#Check Marks
check_marks = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 24, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()