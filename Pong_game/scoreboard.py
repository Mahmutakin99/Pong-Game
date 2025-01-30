from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 220)
        # self.update()
        self.update()
    
    # def increase_score(self,l_or_r):
    #     # self.update()
    #     self.clear()
    #     self.write(f"{self.l_score} Score {self.r_score}", align=ALIGNMENT, font=FONT)
    #     if l_or_r == "l":
    #         self.l_score += 1
    #     else:
    #         self.r_score += 1
    
    def increase_score_r(self):
        self.clear()
        self.r_score += 1
        self.update()
    
    def increase_score_l(self):
        self.clear()
        self.l_score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.l_score}   {self.r_score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)