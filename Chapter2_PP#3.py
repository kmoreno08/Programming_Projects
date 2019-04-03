#Chapter 2_Programming Project #3 - Turtle polygons
'''Prompt for the desired number of sides for your polygon.
Option: prompt for a color and color the interior of your polygon.'''



#Prompt user for a color - try/except if color is not correct
#Color interior
#Keep asking user until quit
#Functions - 1)draw_polygon 2) color_choice


import turtle

'''def color_choice():
    color = input("Which color would you like? : ")
    color = polygon.color(color)
    return color'''
    

def calc_angle():
    interior_angle = (((number_of_sides - 2) * 180) / number_of_sides)
    exterior_angle = 180 - interior_angle
    return exterior_angle

def start_pos():
    my_start = (0, 300)
    polygon.penup()
    polygon.setx(my_start[0])
    polygon.sety(my_start[1])
    polygon.pendown()

'''def fill_color(color_string):
    polygon.fillcolor(color_string)'''
    


print("Regular Polygon.")
number_of_sides = int(input("How many number of sides would you like? : "))
color = input("Which color would you like? : ")
#pentagon
polygon = turtle.Turtle()
exterior_angle = calc_angle()
#Start at the top
start_pos()
polygon.color(color)
polygon.begin_fill()
#put in function
for i in range(0, number_of_sides):
               polygon.forward(50)
               polygon.right(exterior_angle)
polygon.end_fill()



