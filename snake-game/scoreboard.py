from tkinter import CENTER
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, ):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=260)
        self.update_score()
        
        
        
    def update_score(self):
        self.write(f"Score: {self.score}", align="Center",font=('Arial', 24, 'normal'))
        
    def game_over(self):
         self.goto(0,0)
         self.write(f"Game OVER", align="Center",font=('Arial', 24, 'normal'))   
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        