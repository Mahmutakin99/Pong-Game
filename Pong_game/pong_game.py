import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from math import fabs

screen = t.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

def exit_game():
    screen.bye()

game_is_on = True
def game_over():
    global game_is_on
    game_is_on = False
    scoreboard.game_over()
    
screen.listen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.update()

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")
screen.onkey(fun=exit_game, key="Escape")
screen.onkey(fun=game_over, key="q")

while game_is_on:
    screen.update()
    time.sleep(fabs(ball.move_speed))
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.x_bounce()

        
    if ball.xcor() > 350 or ball.xcor() < -350:
        if ball.xcor() > 350:
            scoreboard.increase_score_l()
        else:
            scoreboard.increase_score_r()
        ball.reset_position()

screen.exitonclick()
