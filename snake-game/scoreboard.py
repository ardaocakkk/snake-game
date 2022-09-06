from tkinter import CENTER
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, ):
        super().__init__()
        self.score = 0
        with open("snake-game\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=260)
        self.update_score()
        
        
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}", align="Center",font=('Arial', 24, 'normal'))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake-game\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
                
        self.score = 0
        self.update_score()
        
        
    def increase_score(self):
        self.score += 1
        self.update_score()
        