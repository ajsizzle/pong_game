from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

user_paddle = Paddle()
user_paddle.goto(350, 0)

comp_paddle = Paddle()
comp_paddle.goto(-350, 0)


screen.listen()
screen.onkey(user_paddle.up, "Up")
screen.onkey(user_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
