from turtle import Turtle

MOVE_STEP = 50


class Paddle(Turtle):
    def __init__(self, start_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(start_x, 0)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def go_up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + MOVE_STEP
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - MOVE_STEP
            self.goto(self.xcor(), new_y)
