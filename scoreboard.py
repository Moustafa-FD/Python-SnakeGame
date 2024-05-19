from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(x=0,y=280)
        self.showscore()


    def showscore(self):
        self.write(f"SCORE: {self.score}", False, "center", ('Arial', 12, 'normal'))

    def addscore(self):
        self.clear()
        self.score += 1
        self.showscore()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ('Arial', 20, 'normal'))