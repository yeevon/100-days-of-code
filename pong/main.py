import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard

scr = Screen()
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("Pong")
scr.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

scr.listen()
scr.onkeypress(r_paddle.go_up, "Up")
scr.onkeypress(r_paddle.go_down, "Down")

scr.onkeypress(l_paddle.go_up, "w")
scr.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.detect_wall_collision():
        ball.bounce_y()

    if ball.detect_paddle_collision(r_paddle, l_paddle):
        ball.bounce_x()
        ball.move()
        ball.ball_speed *= 0.9

    if ball.xcor() > 380:
        score.r_point()
        ball.reset_position()


    if ball.xcor() < -380:
        score.l_point()
        ball.reset_position()



scr.exitonclick()



