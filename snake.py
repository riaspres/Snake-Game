from turtle import Turtle
startingPosition = [(0, 0), (-20, 0), (-40,0 )]
moveDistance = 20
up = 90
down = 270
left = 180
right = 0

class Snake:
    
    def __init__(self):
        super().__init__()
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]
        
    def createSnake(self):
        for position in startingPosition:
            self.addSnakeSegment(position)
    
    def addSnakeSegment(self, position):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)
    
    def extendSnake(self):
        self.addSnakeSegment(self.segments[-1].position())
    
    def move(self):    
        for segNum in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segNum -1].xcor()
            newY = self.segments[segNum -1].ycor()
            self.segments[segNum].goto(newX, newY)
        self.head.forward(moveDistance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
                
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
                                