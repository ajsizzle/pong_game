from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

user_paddle = Paddle((350, 0))
comp_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(user_paddle.up, "Up")
screen.onkey(user_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.movement()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()
