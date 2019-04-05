#Chapter 2_Programming Project #3 - Turtle polygons
'''Prompt for the desired number of sides for your polygon.
Option: prompt for a color and color the interior of your polygon.'''

#Prompt user for a color - try/except if color is not correct
#Keep asking user until quit

import turtle

def calc_angle(number_of_sides):
    interior_angle = (((number_of_sides - 2) * 180) / number_of_sides)
    exterior_angle = 180 - interior_angle
    return exterior_angle

def start_pos():
    my_start = (0, 300)
    polygon.penup()
    polygon.setx(my_start[0])
    polygon.sety(my_start[1])
    polygon.pendown()

def draw_polygon(number_of_sides, exterior_angle):
    for i in range(0, number_of_sides):
               polygon.forward(50)
               polygon.right(exterior_angle)

number_of_sides = int(input("How many number of sides would you like? : "))
color = input("Which color would you like? : ")
polygon = turtle.Turtle()
#Calculate exterior angle to use for correct degrees
exterior_angle = calc_angle(number_of_sides)
#Start at the top
start_pos()
#Choose color
polygon.color(color)
#Begin fill color
polygon.begin_fill()
#Draw polygon with for loop
draw_polygon(number_of_sides, exterior_angle)
#Fill in polygon with selected color
polygon.end_fill()



