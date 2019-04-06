#Chapter 2_Programming Project #3 - Turtle polygons
'''Prompt for the desired number of sides for your polygon.
Option: prompt for a color and color the interior of your polygon.'''

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
        


print("Welcome to the turtle polygon program. This program will ask you how \
many number of sides and what color you would like for your polygon. \
Remember: To exit, type in 'exit' at anytime. Enjoy!")

loop = True
while loop:
    number_of_sides = input("How many number of sides would you like? : ")
    number_of_sides = number_of_sides.lower()
    #Exit program
    if number_of_sides == 'exit':
        print("Break exit.")
        break
    #Change to int
    number_of_sides = int(number_of_sides)
    #Check if color is correct, if not message occurs. Still draws shape in black.
    try:
        color = input("Which color would you like? : ")
        #Lower case input
        color = color.lower()
        #Exit program
        if color == 'exit':
            print('Color Exit')
            break
        polygon = turtle.Turtle()
        #Calculate exterior angle to use for correct degrees
        exterior_angle = calc_angle(number_of_sides)
        #Start at the top
        start_pos()
        #Choose color
        polygon.color(color)
    except:
        print("Program does not recognize that color, polygon will be filled in black. ")
    #Begin fill color
    polygon.begin_fill()
    #Draw polygon with for loop
    draw_polygon(number_of_sides, exterior_angle)
    #Fill in polygon with selected color
    polygon.end_fill()

print("Have a great day!")

