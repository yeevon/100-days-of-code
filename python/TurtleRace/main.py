import random
from turtle import Turtle, Screen

is_race_on = False
colors = ["red", "orange", "green", "blue", "purple", "black"]
y_positions = [-70, -40, -10, 20, 50, 80]
scr = Screen()
scr.setup(width=500, height=400)
all_turtles = []

user_bet = scr.textinput(title="Make your pet", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(0, 6):
    a = Turtle("turtle")
    a.penup()
    a.shape("turtle")
    a.color(colors[turtle_index])
    a.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(a)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You win")
            else:
                print(f"You Lose, {winning_color} turtle won!")
        distance = random.randint(0, 10)
        turtle.forward(distance)

scr.exitonclick()