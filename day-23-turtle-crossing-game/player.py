from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.reset_position()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def level_complete(self):
        return self.ycor() > FINISH_LINE_Y

    def reset_position(self):
        self.shape("turtle")
        self.penup()
        self.speed('fastest')
        self.setheading(90)
        self.goto(STARTING_POSITION)

