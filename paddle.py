from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color('#A78295')
        self.shape('square')
        self.turtlesize(1.5,7)
        self.penup()
        self.goto(position)
        self.setheading(90)


    def moveUp(self):
        if self.ycor() <= 260:
            self.forward(50)
    
    
    def moveDown(self):
        if self.ycor() >= -260:
            self.backward(50)
    