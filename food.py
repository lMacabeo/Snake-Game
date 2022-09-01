from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        # Heredamos los atributos y métodos de la clase Turtle
        super().__init__()
        self.shape("circle")
        self.penup()
        # Lo convertimos en vez de 20x20 en 10x10
        self.shapesize(0.5)
        self.color("DarkRed")
        self.speed(0)
        random_x = random.randint(-270,270)
        random_y = random.randint(-270,270)
        self.goto(random_x, random_y)

    def move_food(self):
        random_x = random.randint(-270,270)
        random_y = random.randint(-270,270)
        self.goto(random_x, random_y)

