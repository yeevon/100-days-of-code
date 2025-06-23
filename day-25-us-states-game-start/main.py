import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("United States Game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

states_df = pd.read_csv("50_states.csv")
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed('fast')

keep_guessing = True
correct_answer = pd.read_csv("correct_answers.csv").State.to_list()

for ca in correct_answer:
    answer = states_df[states_df.state == ca]
    pen.goto(answer.x.item(), answer.y.item())
    pen.write(ca)

while keep_guessing:
    title_text = "Guess the State" if len(correct_answer) == 0 else f"{len(correct_answer)}/50 States Correct"

    answer_state = screen.textinput(title=title_text, prompt="What's another state's name?")

    if answer_state is None:
        keep_guessing = False
        continue
    elif answer_state:
        answer_state = answer_state.title()
    else:
        continue

    answer = states_df[states_df.state == answer_state]
    if not answer.empty and answer_state not in correct_answer:
        correct_answer.append(answer_state)
        pen.goto(answer.x.item(), answer.y.item())
        pen.write(answer_state)

save_answers = {
    'State': correct_answer
}
save_df = pandas.DataFrame(save_answers)
save_df.to_csv("correct_answers.csv")
turtle.mainloop()



# 1. Convert the guess to Title case -----------------------------
# 2. Check if the guess is among the 50 states ------------------------------
# 3. Write correct guesses onto the map -----------------------------------
# 4. Use a loop to allow the user to keep guessing ----------------------
# 5. Record the correct guesses in a list ----------------------
# 6. Keep track of the score --------------------