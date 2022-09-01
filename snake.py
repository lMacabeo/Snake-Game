from turtle import Turtle

class Snake():
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.go_up = False
        self.segments = []
        self.create_snake()
        self.head_direction = 0

    def create_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)


    def move(self):
        # Esto permite que se haga una cuenta atrás en el for loop
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_segment_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_segment_y)
        self.segments[0].forward(20)
        self.head_direction = self.segments[0].heading()

    def up(self):
        if self.head_direction != 270:
            self.segments[0].setheading(90)

    def left(self):
        if self.head_direction != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.head_direction != 180:
            self.segments[0].setheading(0)

    def down(self):
        if self.head_direction != 90:
            self.segments[0].setheading(270)

    def add_segment(self, position):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.setposition(position)
        self.segments.append(body)

    def extend(self):
        # Extendemos la cola en la posición del último segmento
        self.add_segment(self.segments[len(self.segments)-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

