from turtle import Turtle
from random import choice, randint

CAR_LANES = [-200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200]
x_start = [350, 370, 390]


class Car:
    def __init__(self):
        self.car = []
        self.lane = choice(CAR_LANES)
        self.rand_colour = (randint(1, 255), randint(1, 255), randint(1, 255))
        self.make_car()

    def add_part(self, pos):
        car_part = Turtle(shape="square")
        car_part.color(self.rand_colour)
        car_part.shape("square")
        car_part.penup()
        car_part.setposition(pos)
        self.car.append(car_part)

    def make_car(self):
        for x in x_start:
            pos = (x, self.lane)
            self.add_part(pos)

    def move(self):
        for part in self.car:
            new_x = part.xcor() - 80
            part.goto(new_x, part.ycor())
