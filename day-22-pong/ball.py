from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.ball_speed = 0.1

        self.x = random.randint(0, 1)
        self.y = random.randint(0, 1)

        self.x = -10 if self.x == 0 else 10
        self.y = -10 if self.y == 0 else 10


    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def reset_position(self):
        self.bounce_x()
        self.ball_speed = 0.1
        self.goto(0,0)


    def bounce_x(self):
        self.x *= -1

    def bounce_y(self):
        self.y *= -1

    def detect_paddle_collision(self, r_paddle, l_paddle):
        return (
                (
                    self.distance(r_paddle) < 50
                    and
                    self.xcor() > 335
                )
                or
                (
                    self.distance(l_paddle) < 50
                    and
                    self.xcor() < -335
                )
               )


    def detect_wall_collision(self):
        return self.ycor() > 285 or self.ycor() < -285