from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    ball.move()
    screen.update()
    time.sleep(0.01)

    # detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.speed_up()
    # detect miss
    if ball.xcor() > 360:
        scoreboard.l_score_up()
        ball.reset()
    if ball.xcor() < -360:
        scoreboard.r_score_up()
        ball.reset()
    if scoreboard.l_score == 2 or scoreboard.r_score == 2:
        scoreboard.win()
        game_on = False

screen.exitonclick()
