from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-95,275)
        with open("data.txt") as file:
            self.highscore = int(file.read())

# Limpiamos la pantalla y escribimos la puntuación y la puntuación más alta
    def score(self, current_score):
        self.clear()
        self.write(f"Score: {current_score} High Score: {self.highscore}", font = (8))

# Si conseguimos una puntuación mayor nueva, guardamos el dato y actualizamos contadores
    def reset(self, current_score):
        if current_score > self.highscore:
            self.highscore = current_score
            with open("data.txt", mode="w") as file:
                file.write(str(current_score))
        return 0

    #def game_over(self):
    #    self.goto(-65,0)
    #    self.write("GAME OVER", font = (8))
