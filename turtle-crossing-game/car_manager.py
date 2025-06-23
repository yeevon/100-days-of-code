from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.goto(300, random.randint(-245, 250))

    def move(self):
        self.goto(self.xcor() + (-1 * MOVE_INCREMENT), self.ycor())

    def off_screen(self):
        return self.xcor() < -280