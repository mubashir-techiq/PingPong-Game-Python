from score import Score
from paddle import Paddle
from ball import Ball
import turtle as t
import time

GAME = True
positions = [(470,0),(-470,0)]
l_score = 0
r_score = 0
SPEED = 0.08
hit = False

screen = t.Screen()
screen.setup(width=1000,height=700)
screen.bgcolor('#331D2C')
screen.tracer(0)

l_pad = Paddle(positions[0])
r_pad = Paddle(positions[1])

score = Score()
score.updateScore(r_score,l_score)
ball = Ball()


screen.listen()
screen.onkey(r_pad.moveUp,'w')
screen.onkey(r_pad.moveDown,'s')
screen.onkey(l_pad.moveUp,'Up')
screen.onkey(l_pad.moveDown,'Down')

while GAME:
    time.sleep(SPEED)
    
    screen.update()
    ball.move()
    if ball.ycor() >= 350 or ball.ycor() <= -350:
        ball.BounceY()

    if ball.distance(l_pad) <= 50 or ball.distance(r_pad) <= 50:
        ball.BounceX()
        hit = True

    if ball.xcor() <= -500:
        ball.ballUpdate()
        l_score+=1
        score.updateScore(r_score,l_score)
        SPEED = 0.08
    elif ball.xcor() >= 500:
        ball.ballUpdate()
        r_score+=1
        score.updateScore(r_score,l_score)
        SPEED = 0.08

    if hit== True:
        if SPEED > 0.06:
            SPEED *= 0.9
        hit = False

screen.exitonclick()
