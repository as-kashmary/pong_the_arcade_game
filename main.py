from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score


screen=Screen();
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong The First Arcade Game")
screen.tracer(0)

screen.listen();

l_pad=Paddle(-350);
r_pad=Paddle(350);
ball=Ball();
score=Score();



game_start=True
while game_start:
    time.sleep(0.1)
    screen.onkey(r_pad.up,"Up")
    screen.onkey(r_pad.down, "Down")
    screen.onkey(l_pad.up, "w")
    screen.onkey(l_pad.down, "s")
    screen.update()
    ball.move();
    if ball.ycor()> 280  or ball.ycor() <-280 :
        ball.bouncey();

    if (ball.xcor() >320 and ball.distance(r_pad) <50) or (ball.xcor() <-320 and ball.distance(l_pad) <50) :
        ball.bouncex();
    if (ball.xcor() > 390 and ball.distance(r_pad) >= 50 and ball.distance(l_pad) >= 50):
        ball.refresh();
        score.r_change();
    if (ball.xcor() <-390 and ball.distance(r_pad) >= 50 and ball.distance(l_pad) >= 50):
        ball.refresh();
        score.l_change();






screen.exitonclick();