from turtle import Turtle
import random

MOVE_STEP = 2.5


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.setheading(30)
        self.penup()
        self.dir_y = random.choice([-1,1])
        self.dir_x = random.choice([-1,1])
        self.velocity=1

    def move(self):
        new_x = self.xcor() + MOVE_STEP * self.velocity * self.dir_x
        new_y = self.ycor() + MOVE_STEP * self.velocity * self.dir_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dir_y *= -1

    def bounce_x(self):
        self.dir_x *= -1

    def speed_up(self):
        self.velocity *= 1.5

    def reset(self):
        self.velocity = 1
        self.goto(0, 0)
        self.dir_x=random.choice([-1,1])
        self.dir_y=random.choice([-1,1])
