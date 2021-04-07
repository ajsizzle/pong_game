from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

user_paddle = Paddle((350, 0))
comp_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(user_paddle.up, "Up")
screen.onkey(user_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(user_paddle) < 50 and ball.xcor() > 320 or ball.distance(comp_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when user paddle misses
    if ball.xcor() > 420:
        ball.restart()
        scoreboard.comp_point()

    # Detect when comp paddle misses
    if ball.xcor() < -420:
        ball.restart()
        scoreboard.user_point()

screen.exitonclick()
