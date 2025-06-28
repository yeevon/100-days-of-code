import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_inpt.insert(0, password)
    pyperclip.copy(password)

    messagebox.showinfo(title="Password", message="Password saved to clipboard!")

# ---------------------------- Search ------------------------------- #
def search():
    website = website_inpt.get().strip()

    if not website:
        messagebox.showwarning(message="Enter Website Name.", title="ERROR")
    else:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title='ERROR', message='No Data File Found.')
        else:
            if website in data:
                messagebox.showinfo(
                    title=f'{website}',
                    message=f'email: {data[website]['email']}\n'
                            f'password: {data[website]['password']}')
            else:
                messagebox.showwarning(title='ERROR', message=f'{website}: No Data Found')
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    # Get Data for App UI
    get_website = website_inpt.get().strip()
    get_user = email_inpt.get().strip()
    get_password = password_inpt.get().strip()

    # Create data dictionary based on UI data
    new_data = {
        get_website: {
            'email': get_user,
            'password': get_password
        }
    }

    # Verify user entered a website and password
    if not get_website or not get_password:
        messagebox.showinfo(title="ERROR", message="Please do not leave any fields empty!")
    else:
        # Clear UI data
        website_inpt.delete(0, END)
        password_inpt.delete(0, END)

        # Get existing data from json
        try:
            with open("data.json", mode='r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = new_data
        else:
            data.update(new_data)

        # Update and rewrite data to json file
        with open("data.json", mode='w') as data_file:
            json.dump(data, data_file, indent=4)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock_pic = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_pic)
canvas.grid(column=1, row=0)

website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1)

website_inpt = Entry(width=32)
website_inpt.grid(column=1, row=1, sticky="w")
website_inpt.focus()

search_button = Button(text='Search', width=11, command=search)
search_button.grid(column=2, row=1, sticky="w")

email_lbl = Label(text="Email/Username:")
email_lbl.grid(column=0, row=2)

email_inpt = Entry(width=48)
email_inpt.grid(column=1, row=2, columnspan=2, sticky="w")
email_inpt.insert(0, "delimajm@gmail.com")

password_lbl = Label(text="Password:")
password_lbl.grid(column=0, row=3)

password_inpt = Entry(width=32)
password_inpt.grid(column=1, row=3, sticky="w")

password_btn = Button(text="Generate Password", font=("ariel", 7), command=generate_password)
password_btn.grid(column=2, row=3, sticky="w")

add_btn = Button(text="Add", width=41, command=save_info)
add_btn.grid(column=1, row=4, columnspan=2, sticky="w")
window.mainloop()
