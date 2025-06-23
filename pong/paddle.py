from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def go_up(self):
        new_y = self.ycor() + 13
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 13
        self.goto(self.xcor(), new_y)