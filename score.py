from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('#EFE1D1')
        self.hideturtle()
        self.penup()
        
    def updateScore(self,rsc,lsc):
        self.clear()
        self.goto(0,300)
        self.write(f'{rsc} : {lsc}',align='center',font=('Courier',25,'bold'))