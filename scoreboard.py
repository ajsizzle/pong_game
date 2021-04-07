from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.comp_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.comp_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.user_score, align="center", font=("Courier", 80, "normal"))

    def comp_point(self):
        self.comp_score += 1
        self.update_score()

    def user_point(self):
        self.user_score += 1
        self.update_score()
