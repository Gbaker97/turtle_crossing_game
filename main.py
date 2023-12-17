from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time

LEVELS = [(1, 0.4), (1, 0.3), (2, 0.3), (2, 0.2), (3, 0.2), (3, 0.1), (4, 0.1)]
scoreboard = Scoreboard()

road = []


def add_cars(num):
    for _ in range(num):
        car = Car()
        road.append(car)


def game_over(screen, rd):
    time.sleep(10)
    play_again = screen.textinput("Play again?", "Type 'y' or 'n': ")
    if play_again == "y":
        screen.clear()
        rd.clear()
        scoreboard.restart_game()
        start_game(scoreboard.level)


def start_game(lvl):

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle Crossing Game")
    screen.colormode(255)
    screen.tracer(0)

    p1 = Player()

    screen.listen()
    screen.onkey(p1.go_fwd, "Up")
    screen.onkey(p1.go_left, "Left")
    screen.onkey(p1.go_right, "Right")

    game_is_on = True
    while game_is_on:
        time.sleep(LEVELS[lvl - 1][1])
        add_cars(LEVELS[lvl - 1][0])
        for car in road:
            car.move()
            # removing passed cars from road list
            if car.car[2].xcor() < -360:
                for c in car.car:
                    c.hideturtle()
                    screen.update()
                road.remove(car)

            # check collision with car
            for c in car.car:
                screen.update()
                if (p1.distance(c) < 20
                        or p1.distance(c) <= 25 and (c.ycor() + 20) >= p1.ycor() >= (c.ycor() - 20)):
                    scoreboard.game_over()
                    game_over(screen, road)
                    game_is_on = False

        # check player is at end
        if p1.ycor() > 230:
            screen.clear()
            scoreboard.update_scoreboard()
            start_game(scoreboard.level)

        screen.update()

    screen.exitonclick()

start_game(scoreboard.level)
