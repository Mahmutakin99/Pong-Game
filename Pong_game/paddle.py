from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setheading(90)
        self.goto(position)
    
    def go_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 30)
    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 30)