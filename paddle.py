from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self .shape("square")
        self.penup();
        self.color("white");
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.setx(x);

    def up(self):
        y = self.ycor();
        self.goto(self.xcor(), y + 40)

    def down(self):
        y = self.ycor();
        self.goto(self.xcor(), y - 40)
