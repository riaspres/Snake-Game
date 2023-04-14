from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.UpdateScore()

    def UpdateScore(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        
    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))


    def increaseScore(self):
        self.score += 1
        self.clear()
        self.UpdateScore()