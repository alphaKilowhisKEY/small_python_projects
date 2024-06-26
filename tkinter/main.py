from tkinter import *

window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="a Label", font=("Courier", 12, "italic"))
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="New Text")

def click_func():
    my_label.config(text=input.get())

#Button
button = Button(text="Click Me", command=click_func)
button.pack()

#Entry
input = Entry(width=10)
input.pack()
input.get()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox
text.focus()
#Add some text to begin with
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()    

#Checkbutton
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
chebutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
chebutton.pack()    

#Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

def listbox_used(event):
    print(listbox.get(listbox.curselection()))
#Listbox
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()    

window.mainloop()