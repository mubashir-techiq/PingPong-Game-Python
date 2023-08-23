from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('#EFE1D1')
        self.shape('circle')
        self.newX = 10
        self.newY = 10
        self.penup()
    
    def move(self):
        x = self.xcor() +self.newX
        y = self.ycor() +self.newY
        self.goto((x,y))

    def BounceY(self):
        self.newY *= -1

    def BounceX(self):
        self.newX *= -1

    def ballUpdate(self):
        self.goto(0,0)
        self.newX *= -1
        
