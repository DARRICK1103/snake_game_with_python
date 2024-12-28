import random as rd
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rdn_x = rd.randint(-280, 280)
        rdn_y = rd.randint(-280, 280)
        self.goto(rdn_x, rdn_y)


