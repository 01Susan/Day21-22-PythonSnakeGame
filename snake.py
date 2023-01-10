from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    # TODO 1. Creating the body of snake
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.goto(position)
        new_snake.color("white")
        new_snake.penup()
        self.segment.append(new_snake)

    # TODO 5. Extend the length of snake
    def extend(self):
        self.add_segment(self.segment[-1].position())

    # TODO 2. Function to move our snake Forward
    def move(self):
        for snake in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[snake - 1].xcor()
            new_y = self.segment[snake - 1].ycor()
            self.segment[snake].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    # TODO 3. Adding control feature to control the snake
    def up(self):
        if self.head.heading() == 0.0 or self.head.heading() == 180.0:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 0.0 or self.head.heading() == 180.0:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() == 90.0 or self.head.heading() == 270.0:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() == 90.0 or self.head.heading() == 270.0:
            self.head.setheading(180)
