import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)


player = Player()
cars = []
score = Scoreboard()
car_generation_counter = 0

screen.listen()
screen.onkeypress(fun=player.up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1 * (.93 ** score.level))
    screen.tracer(0)
    screen.update()
    car_generation_counter += 1

    if car_generation_counter == 6:
        car = CarManager()
        cars.append(car)
        car_generation_counter = 0

    for car in cars[:]:
        car.move()
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False


        if car.off_screen():
            car.hideturtle()
            cars.remove(car)
            del car

    if player.level_complete():
        for car in cars[:]:
            car.hideturtle()
            cars.remove(car)
            del car
        score.increase_level()
        player.reset_position()

screen.exitonclick()