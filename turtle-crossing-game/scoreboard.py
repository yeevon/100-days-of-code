from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.level = 0
        self.__update_score()

    def increase_level(self):
        self.level += 1
        self.__update_score()

    def __update_score(self):
        self.clear()
        self.goto(-210, 260)
        self.write(f"LEVEL: {self.level}", align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)