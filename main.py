from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# Lo primero a crear debería ser la pantalla
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
# Activa o desactiva las animaciones
screen.tracer(0)

snake = Snake()
food = Food()
current_score = 0
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
playing = True

while playing:
    # Actualiza las animaciones
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.score(current_score)
    # Detectamos si toca la comida
    if snake.segments[0].distance(food) < 15:
        food.move_food()
        current_score += 1
        snake.extend()
    # Detectamos si toca un muro
    if snake.segments[0].xcor() > 285 or snake.segments[0].xcor() < -285 or snake.segments[0].ycor()\
            > 285 or snake.segments[0].ycor() < -285:
        current_score = scoreboard.reset(current_score)
        snake.reset()

    # Detectamos colisión con la cola
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            current_score = scoreboard.reset(current_score)
            snake.reset()

screen.exitonclick()
