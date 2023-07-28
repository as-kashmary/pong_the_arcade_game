from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__();
        self.shape("circle")
        self.color("white");
        self.penup();
        self.x_mov = 10
        self.y_mov = 10

    def move(self):
        x = self.xcor();
        y = self.ycor();
        self.goto(x + self.x_mov, y + self.y_mov)

    def bouncey(self):
        self.y_mov *= -1;

    def bouncex(self):
        self.x_mov*=-1
    def refresh(self):
        self.goto(0,0);
        self.bouncex();