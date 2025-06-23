from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.config(pady=20, padx=20)


def convert_distance():
    miles = float(miles_input.get())
    conversion_label.config(text=miles * 1.6)

is_equal_lbl = Label(text="is equal to")
is_equal_lbl.grid(column=0, row=1)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

conversion_label = Label(text=0)
conversion_label.grid(column=1, row=1)

calc_button = Button(text="Calculate", command=convert_distance)
calc_button.grid(column=1, row=2)

miles_lbl = Label(text="Miles")
miles_lbl.grid(column=2, row=0)

km_lbl = Label(text="KM")
km_lbl.grid(column=2, row=1)

window.mainloop()