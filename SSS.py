from turtle import Turtle

MOVEDISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):

        self.SnakeBody = []
        self.CreateSnake()
        self.head = self.SnakeBody[0]

    def CreateSnake(self):
        for _ in range(3):
            self.add_segment()


    def add_segment(self):
        tim = Turtle("square")
        tim.color("white")
        tim.speed(0)
        tim.penup()
        self.SnakeBody.append(tim)

        if len(self.SnakeBody) != 1:
            Xstart = self.SnakeBody[self.SnakeBody.index(tim) - 1].xcor() - 20
            Ystart = self.SnakeBody[self.SnakeBody.index(tim) - 1].ycor()
            tim.goto(x=Xstart, y=Ystart)





    def Move(self):
        for body_num in range(len(self.SnakeBody) - 1, 0, -1):
            xgo = self.SnakeBody[body_num - 1].xcor()
            ygo = self.SnakeBody[body_num - 1].ycor()
            self.SnakeBody[body_num].goto(xgo, ygo)

        self.head.forward(MOVEDISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
