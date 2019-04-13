#Chapter 6_Programming Project #1 - U.S. Flag in Turtle Graphics

'''Draw the US flag using at least four functions.
a) Draw the flag and have the 13 stars in a row and add color for max effect.
b) Draw the flag and have the 13 stars in a circle
c) Have the program take an input that specifies a scale factor.'''


#Fill in white for stars
#Separate flag with stars (Circle)
#User input will specify both flags separately and scale factor
#Clean-up

import turtle
draw = turtle.Turtle()

def openingLine():
    draw.left(180)
    draw.forward(250)
    draw.right(90)
    draw.forward(260)
    draw.right(90)
    
def drawRectangle():
    draw.forward(400)
    draw.right(90)
    draw.forward(20)
    draw.right(90)
    draw.forward(400)

def drawSpace():
    draw.left(90)
    draw.forward(20)
    draw.left(90)

def beginFill():
    draw.begin_fill()



def drawStar():
    for i in range(0,5):
        draw.forward(10)
        draw.end_fill()
        draw.forward(10)
        draw.right(144)
        draw.end_fill()



openingLine()
draw.fillcolor("red")
for i in range(0,7):
    if i == 6:
        beginFill()
        drawRectangle()
        draw.end_fill()
        break
    beginFill()
    drawRectangle()
    drawSpace()
    draw.end_fill()

#Line on right side
draw.left(180)
draw.forward(400)
draw.left(90)
draw.forward(250)
draw.left(180)
draw.forward(250)
draw.right(90)
draw.forward(400)
    


#Go back for stars background
draw.fillcolor("blue")
beginFill()
draw.right(90)
draw.forward(260)
draw.right(90)
draw.forward(195)
draw.right(90)
draw.forward(180)
draw.right(90)
draw.forward(195)
draw.end_fill()

#Position for start of star
draw.right(90) #Right -> maybe enter from top to replicate all 3 stars
draw.forward(160)

#top line - 3 star
draw.fillcolor("white")
draw.right(90)
draw.penup()
draw.forward(20)
draw.pendown()
drawStar()
draw.end_fill()
draw.penup()
draw.forward(60)
draw.pendown()
drawStar()
draw.penup()
draw.forward(60)
draw.pendown()
drawStar()
draw.end_fill()

#return pos - 3 star
draw.penup()
draw.right(180)
draw.forward(140)
draw.left(90)
draw.forward(30)
draw.left(90)

#2nd line  - 2 stars
draw.forward(50)
draw.pendown()
drawStar()
draw.penup()
draw.forward(60)
draw.pendown()
drawStar()

#return pos - 2 stars
draw.penup()
draw.right(180)
draw.forward(110)
draw.left(90)
draw.forward(30)

#Third line - 3 stars
draw.left(90)
draw.forward(20)
draw.pendown()
drawStar()
draw.penup()
draw.forward(60)
draw.pendown()
drawStar()
draw.penup()
draw.forward(60)
draw.pendown()
drawStar()

#return pos - 3 star
draw.penup()
draw.right(180)
draw.forward(140)
draw.left(90)
draw.forward(30)
draw.left(90)

#Fourth line - 2 star
draw.forward(50)
draw.pendown()
drawStar()
draw.penup()
draw.forward(60)
draw.pendown()
drawStar()

#return pos - 2 stars
draw.penup()
draw.right(180)
draw.forward(110)
draw.left(90)
draw.forward(30)

#Fifth line - 3 stars
draw.left(90)
draw.forward(20)
draw.pendown()
drawStar()
draw.penup()
draw.forward(60)
draw.pendown()
drawStar()
draw.penup()
draw.forward(60)
draw.pendown()
drawStar()

















