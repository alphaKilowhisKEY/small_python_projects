from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("GRID")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="Label", font=("Courier", 12, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Button", command=button_clicked)
button.grid(row=1, column=1)

#New Button
button = Button(text="New Button", command=button_clicked)
button.grid(row=0, column=2)

#Entry
input = Entry(width=10)
input.grid(row=3, column=4)
input.get()

window.mainloop()