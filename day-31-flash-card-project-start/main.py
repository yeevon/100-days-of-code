from tkinter import *
import random
import pandas as pd
import os

BACKGROUND_COLOR = "#B1DDC6"


# =================== read data from csv ======================= #

if os.path.exists('data/words_to_learn.csv'):
    df = pd.read_csv("data/words_to_learn.csv")
else:
    df = pd.read_csv("data/french_words.csv")

list_of_dict = df.to_dict(orient='records')
print(len(list_of_dict))
current_card = {}

def next_word():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    card.itemconfig(canvas_image, image=CARD_FRONT)
    current_card = random.choice(list_of_dict)
    card.itemconfig(card_title, text='French', fill='black')
    card.itemconfig(card_word, text=current_card['French'], fill='black')

    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    card.itemconfig(canvas_image, image=CARD_BACK)
    card.itemconfig(card_title, text='English', fill='White')
    card.itemconfig(card_word, text=current_card['English'], fill='White')


def correct_answer():
    list_of_dict.remove(current_card)
    pd.DataFrame(list_of_dict).to_csv('data/words_to_learn.csv', index=False)
    next_word()


# ===================== tkinter ui ============================= #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Create image constants
CARD_FRONT = PhotoImage(file="images/card_front.png")
CARD_BACK = PhotoImage(file="images/card_back.png")
RIGHT_PIC = PhotoImage(file="images/right.png")
WRONG_PIC = PhotoImage(file="images/wrong.png")

card = Canvas(width=850, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = card.create_image(435,300)
card_title = card.create_text(425, 140, text='', font=("Ariel", 40, "italic"))
card_word = card.create_text(425, 310, text="", font=("Ariel", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=WRONG_PIC, command=next_word)
wrong_button.grid(column=0, row=1)

right_button = Button(image=RIGHT_PIC, command=correct_answer)
right_button.grid(column=1, row=1)

next_word()

window.mainloop()