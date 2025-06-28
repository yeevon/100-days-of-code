from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_counter():
    global reps
    reps += 1

    if reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(60 * WORK_MIN)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(60 * LONG_BREAK_MIN)
    else:
        timer_label.config(text="Break", fg=PINK)
        count_down(60 * SHORT_BREAK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer

    display_time = f"{count//60}:{count%60:02d}"
    canvas.itemconfig(timer_text, text=display_time)

    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_counter()
        if reps % 9 == 0:
            reset_timer()
        elif reps % 2 == 0:
            checkmark_label.config(text='✔' * (int(reps/2)))


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0, bd=0, highlightbackground=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_pic)
timer_text = canvas.create_text(102, 135, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

start_btn = Button(text="Start", command=start_counter)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)


checkmark_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14))
checkmark_label.grid(column=1, row=3)


window.mainloop()