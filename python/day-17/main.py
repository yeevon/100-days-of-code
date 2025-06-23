from turtle import Turtle, Screen

tim = Turtle()
scr = Screen()
moving_cw = False
moving_ccw = False

def move_clockwise():
    if moving_cw:
        tim.forward(10)
        tim.right(10)
    if moving_ccw:
        tim.forward(10)
        tim.left(10)
    scr.ontimer(move_clockwise, 10)


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def start_clockwise():
    global moving_cw
    moving_cw = True

def stop_clockwise():
    global moving_cw
    moving_cw = False

def start_counterClockwise():
    global moving_ccw
    moving_ccw = True

def stop_counterClockwise():
    global moving_ccw
    moving_ccw = False

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

    
scr.onkeypress(key='w', fun=start_clockwise)
scr.onkeyrelease(key='w', fun=stop_clockwise)
scr.onkeypress(key='a', fun=move_backwards)
scr.onkeypress(key='s', fun=start_counterClockwise)
scr.onkeyrelease(key='s', fun=stop_counterClockwise)
scr.onkeypress(key='d', fun=move_forwards)
scr.onkey(key='c', fun=clear)

Screen().listen()
move_clockwise()
scr.exitonclick()