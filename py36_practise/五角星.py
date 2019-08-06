from turtle import *
def drawStar(x,y):
    penup()
    goto(x,y)
    pendown()
    #setheading(0)
    for i in range(5):
        forward(40)
        right(144)
for x in range(0,250,50):
    drawStar(x,0)
