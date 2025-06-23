from tkinter import *

window = Tk()
window.title("My Frist GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
myLabel = Label(text="I am a Label", font=("Arial", 24, "bold"))
# myLabel.place(x=100, y=200)
myLabel.grid(column=0, row=0)

myLabel["text"] = "New Text"

# Button

def button_clicked():
    myLabel.config(text=frm_input.get())

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="another one").grid(column=2, row=0)

# Entry

frm_input = Entry(width=10)
frm_input.grid(column=3, row=2)

# myLabel.pack()
# button.pack()
# frm_input.pack()
window.mainloop()