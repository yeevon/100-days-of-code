from tkinter import *
from PIL import Image, ImageTk
import requests


def get_quote():
    response =  requests.get(
        "https://api.api-ninjas.com/v1/quotes",
        headers={"X-API-Key": 'NT4867a9db3gzrZomJ6wyg==7sbvMsx4PdF187CD'}
    ).json()
    response.raise_for_status()
    canvas.itemconfig(quote_text, text=f"{response[0]['quote']} BY: {response[0]['author']}")


window = Tk()
window.title("Ancient Secret...")
window.config(padx=50, pady=50)

canvas = Canvas(width=700, height=800)
background = Image.open("background.png")
resize_img = background.resize((650, 800))
background_img = ImageTk.PhotoImage(resize_img)
canvas.create_image(360, 400, image=background_img)
quote_text = canvas.create_text(350, 350, text="Quote Goes HERE", width=480, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="quote.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()