from tkinter import *

def calculate_miles_to_km():
    km = float(input.get()) * 0.1609344
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=350, height=100)
window.config(padx=20, pady=10)

#Entry "Miles"
input = Entry(width=7)
input.grid(column=1, row=0)

#Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

#Button "Calculate"
button = Button(text="Calculate", command=calculate_miles_to_km)
button.grid(column=1, row=2)

window.mainloop()