from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.125) #SPEED WHICH GAME UPDATES MOVES
    snake.move()
    
    #DETECT FOOD COLISSION
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extendSnake()
        scoreboard.increaseScore()
    
    #DETECT WALL COLISSION
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        gameIsOn = False
        scoreboard.gameOver()
        
    #DETECT TAIL COLISSION
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            gameIsOn = False
            scoreboard.gameOver()
        

screen.exitonclick()

