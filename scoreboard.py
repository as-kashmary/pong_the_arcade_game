from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-100,250)
        self.l_score=0
        self.r_score=0
        self.hideturtle();
        self.write(str(self.l_score),False,"center",("ariel",20,"normal"))
        self.goto(100, 250)
        self.write(str(self.r_score), False, "center", ("ariel", 20, "normal"))

    def l_change(self):
        self.l_score+=1;
        self.clear();
        self.write(str(self.r_score), False, "center", ("ariel", 20, "normal"))
        self.goto(100, 250)
        self.write(str(self.l_score), False, "center", ("ariel", 20, "normal"))

    def r_change(self):
        self.r_score+=1;
        self.clear();
        self.write(str(self.r_score), False, "center", ("ariel", 20, "normal"))
        self.goto(-100, 250)
        self.write(str(self.l_score), False, "center", ("ariel", 20, "normal"))
