#Chapter 6_Programming Project #1 - U.S. Flag in Turtle Graphics

'''Draw the US flag using at least four functions.
a) Draw the flag and have the 13 stars in a row and add color for max effect.
b) Draw the flag and have the 13 stars in a circle
c) Have the program take an input that specifies a scale factor.'''

#Need to add 13 stars (Row)
#Seperate flag with stars (Circle)
#User input will specify both flags separately 

import turtle
draw = turtle.Turtle()

def openingLine():
    draw.left(90)
    draw.forward(260)
    draw.right(90)
    
def drawRectangle():
    draw.forward(250)
    draw.right(90)
    draw.forward(20)
    draw.right(90)
    draw.forward(250)

def drawSpace():
    draw.left(90)
    draw.forward(20)
    draw.left(90)

def beginFill():
    draw.begin_fill()

    

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
    


#Go back for stars background
draw.fillcolor("blue")
beginFill()
draw.right(90)
draw.forward(260)
draw.right(90)
draw.forward(130)
draw.right(90)
draw.forward(140)
draw.right(90)
draw.forward(130)
draw.end_fill()







