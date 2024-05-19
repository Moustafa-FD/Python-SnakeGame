from turtle import Screen
import time
from SSS import Snake
from food import Food
from scoreboard import ScoreBoard

window = Screen()
window.setup(width=600, height=600)
window.tracer(0)
window.bgcolor("black")
window.title("Snake Game")

snake = Snake()
food = Food()
score = ScoreBoard()

window.listen()
window.onkey(snake.up,"Up")
window.onkey(snake.down,"Down")
window.onkey(snake.left,"Left")
window.onkey(snake.right,"Right")




GameIsValid = True

while GameIsValid:

    window.update()
    time.sleep(0.1)
    snake.Move()




    if snake.head.distance(food) < 15:
        food.refresh()
        score.addscore()
        snake.add_segment()

    # detect collision
    if snake.head.xcor() < -280 or snake.head.xcor() > 280:
        GameIsValid = False
        score.gameover()

    if snake.head.ycor() < -280 or snake.head.ycor() > 280:
        GameIsValid = False
        score.gameover()

    for body in snake.SnakeBody[1:]:
        if snake.head.distance(body) < 10:
            GameIsValid = False
            score.gameover()



window.exitonclick()
