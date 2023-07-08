######################################################
# Project: Project 1
# Student Name:  <your name: Chang, Yeonsoo>
# UIN: <673272656>
# URL: <https://replit.com/@ychan57/CS-111project1YeonsooChang673272656#main.py>
######################################################

## information for scorers

## on what line number is the required for loop?
## <line 69>

## on what line number is the required use of a random number?
## <line 70>

## on what line number is the required use of a conditional statement?
## <line 76>

## on what line number is the required use of a list?
## <line 63, 334>

## The title for this drawing I put is "Chicago" which I wrote in the sign.

import turtle
from random import randint

s = turtle.Screen()
s.setup(width=800, height=550)
s.bgcolor("black")
s.tracer(0) # Being able to see the results right away
t1 = turtle.Turtle()
t2 = turtle.Turtle()

"""
This function draws a sky with rectangle by getting its length and width
"""
def draw_sky (t, x, y, length, width, pen_color, fill_color, heading, pensize):
  draw_rectangle (t, x, y, length, width, pen_color, fill_color, heading, pensize)


"""
This function draws stars with a certain angle and length
"""
def draw_star(t, x, y, heading, pensize):
  t.penup()
  t.hideturtle()
  t.goto(x, y)
  t.pendown()
  t.pensize(pensize)
  t.setheading(heading)
  t.left(144)
  t.forward(10)
  t.left(144)
  t.forward(10)
  t.left(144)
  t.forward(10)
  t.left(144)
  t.forward(10)
  t.left(144)
  t.forward(10)


starcolor = ["yellow", "orange", "pink"]

"""
This function draws a background by calling draw_star()
"""
def draw_background (t): # Draw a total of 30 stars and change the color everytime drawing 10 stars
    for i in range(0,30): 
      x = randint(-150,300)
      y = randint(50,270)
      t.penup()
      t.hideturtle()
      t.goto(x, y)
      t.pendown()
      if i <= 10:
        t.color(starcolor[0])
      else:
        if i <= 20:
          t.color(starcolor[1])
        else:
          t.color(starcolor[2])
      draw_star(t1, x, y, 90, 1) # Call the draw_star from which I made in def draw_Star()


"""
This function draws a rectangle by getting its length and width
"""
def draw_rectangle (t, x, y, length, width, pen_color, fill_color, heading, pensize):
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.pendown()
    t.pensize(pensize)
    t.setheading(heading)
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.end_fill()

"""
This function draws a triangle by getting its length, width, side_length
"""
def draw_triangle(t, x, y, length, width, side_length, pen_color, fill_color, heading, pensize):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(pensize)
    t.setheading(heading)
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.left(63.44)
    t.forward(side_length)
    t.left(116.56)
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.end_fill()

"""
This function draws a road with rectangle by getting its length and width
"""
def draw_road (t, x, y, length, width, pen_color, fill_color, heading, pensize):
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.pendown()
    t.pensize(pensize)
    t.setheading(heading)
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.left(63.44)
    t.forward(length)
    t.left(26.56)
    t.forward(width)
    t.left(153.44)
    t.forward(length)
    t.left(26.56)
    t.forward(width)
    t.end_fill()

"""
This function draws a building with rectangle by getting its length and width
"""
def draw_building (t, x, y, length, width, pen_color, fill_color, heading, pensize):
  draw_rectangle(t, x, y, length, width, pen_color, fill_color, heading, pensize)


"""
This function draws a sign with rectangle by getting its length and width
"""
def draw_sign (t, x, y, length, width, pen_color, fill_color, heading, pensize):
  draw_rectangle(t, x, y, length, width, pen_color, fill_color, heading, pensize)


"""
This function draws a window with rectangle by getting its length and width
"""
def draw_window (t, x, y, length, width, pen_color, fill_color, heading, pensize):
  draw_rectangle(t, x, y, length, width, pen_color, fill_color, heading, pensize)


"""
This function draws a circle by getting its radius, extent, and steps
"""
def draw_circle (t, x, y, radius, extent, steps, pen_color, fill_color, pensize):
  t.penup()
  t.goto(x,y)
  t.pencolor(pen_color)
  t.fillcolor(fill_color)
  t.begin_fill()
  t.circle(radius)
  t.end_fill()

"""
This function runs the whole program
"""
def main():

  # Gives gradation effect to the sky with shape of rectangle
  draw_sky (t1, 400, 37.5, 50, 800, "royalblue1", "royalblue1", 90, 2)
  draw_sky (t1, 400, 87.5, 50, 800, "royalblue3", "royalblue3", 90, 2)
  draw_sky (t1, 400, 137.5, 50, 800, "royalblue4", "royalblue4", 90, 2)
  draw_sky (t1, 400, 187.5, 50, 800, "midnightblue", "midnightblue", 90, 2)

  # Make the background with shape of star
  draw_background(t1)

  # Make the sidewalk and the road with shape of rectangle
  draw_rectangle (t1, 400, -550, 537.5, 800, 'yellowgreen', 'yellowgreen', 90, 2)
  draw_rectangle (t1, 400, -12.5, 50, 800, "gainsboro", "gainsboro", 90, 2)

  # Make the sidewalk and the road with shape of triangle and rectangle
  draw_triangle (t1, 400, -275, 800, 550, 970.8, "gainsboro", "gainsboro", 90, 2)
  draw_triangle (t1, 50, -275, 800, 550, 970.8, "light goldenrod","light goldenrod", 90, 2)
  draw_road (t2, 300, -225, 111.8, 350, "white", "white", 90, 2) 
  draw_road (t2, 280, -215, 71.8, 32, "gainsboro", "gainsboro", 90, 2) 
  draw_road (t2, 207, -215, 71.8, 62, "gainsboro", "gainsboro", 90, 2) 
  draw_road (t2, 100, -215, 71.8, 62, "gainsboro", "gainsboro", 90, 2) 
  draw_road (t2, -7, -215, 71.8, 62, "gainsboro", "gainsboro", 90, 2) 

  # Make the roadline with shape of rectangle
  draw_road (t2, -65, -120, 100, 20, "white", "white", 90, 0)
  draw_rectangle (t2, 35, 12.5, 5, 120, "white", "white", 90, 0)
  draw_rectangle (t2, 290, 12.5, 5, 120, "white", "white", 90, 0)

  # Make the left building with shape of rectangle
  draw_rectangle (t1, -192.5, -275, 550, 207.5, "burlywood4", "burlywood4", 90,2)

  # Make the window for the left building with shape of rectangle
  draw_rectangle (t1, -192.5,  170, 80, 207.5, "lightsalmon4", "lightsalmon4", 90, 2)
  draw_window (t1, -194.5, 248, 120, 120, "lightsalmon4", "lightblue", 90, 6)
  draw_window (t1, -242.5, 248, 120, 120, "lightsalmon4", "lightblue", 90, 6)
  draw_window (t1, -352.5, 248, 120, 120, "lightsalmon4", "lightblue", 90, 6)
  draw_window (t1, -218.5, 172, 78, 5, "black", "black", 90, 3)
  draw_window (t1, -258.5, 172, 78, 5, "black", "black", 90, 3)
  draw_window (t1, -298.5, 172, 78, 5, "black", "black", 90, 3)
  draw_window (t1, -338.5, 172, 78, 5, "black", "black", 90, 3)
  draw_window (t1, -378.5, 172, 78, 5, "black", "black", 90, 3)

  draw_rectangle (t1, -192.5, -60, 80, 207.5, "lightsalmon4", "lightsalmon4", 90, 2)
  draw_window (t1, -194.5, 20, 120, 120, "lightsalmon4", "lightblue", 90, 6)
  draw_window (t1, -242.5, 20, 120, 120, "lightsalmon4", "lightblue", 90, 6)
  draw_window (t1, -352.5, 20, 120, 120, "lightsalmon4", "lightblue", 90, 6)
  draw_window (t1, -218.5, -58, 78, 5, "black", "black", 90, 3)
  draw_window (t1, -258.5, -58, 78, 5, "black", "black", 90, 3)
  draw_window (t1, -298.5, -58, 78, 5, "black", "black", 90, 3)
  draw_window (t1, -338.5, -58, 78, 5, "black", "black", 90, 3)
  draw_window (t1, -378.5, -58, 78, 5, "black", "black", 90, 3)

  draw_rectangle (t1, -192.5, -275, 80, 207.5, "lightsalmon4", "lightsalmon4", 90, 2)
  draw_window (t1, -194.5, -208, 120, 120, "lightsalmon4", "lightblue", 90, 6)
  draw_window (t1, -242.5, -208, 120, 120, "lightsalmon4", "lightblue", 90, 6)
  draw_window (t1, -352.5, -208, 120, 120, "lightsalmon4", "lightblue", 90, 6)
  draw_window (t1, -218.5, -273, 66, 5, "black", "black", 90, 3)
  draw_window (t1, -258.5, -273, 66, 5, "black", "black", 90, 3)
  draw_window (t1, -298.5, -273, 66, 5, "black", "black", 90, 3)
  draw_window (t1, -338.5, -273, 66, 5, "black", "black", 90, 3)
  draw_window (t1, -378.5, -273, 66, 5, "black", "black", 90, 3)

  # Make the sign "Chicago" with shape of rectangle
  draw_sign (t1, -112.5, -70, 290, 30, "orange", "orange", 90, 40)
  draw_sign (t1, -120, -60, 270, 15, "firebrick1", "firebrick1", 90, 40)
  draw_sign (t1, -163, 160, 7, 28, "tomato3","tomato3", 90, 2)
  draw_sign (t1, -163, 0, 7, 28, "tomato3", "tomato3", 90, 2)

  # Make the right building with the several rectangles
  draw_building (t2, 190, -40, 250, 150, "white", "gold", 90,4)
  draw_building (t2, 200, -45, 250, 150, "gold", "gold", 90,2)
  draw_building (t2, 210, -50, 250, 150, "gold", "gold", 90,2)
  draw_building (t2, 220, -55, 250, 150, "gold", "gold", 90,2)
  draw_building (t2, 230, -60, 250, 150, "gold", "gold", 90,2)
  draw_building (t2, 240, -65, 250, 150, "gold", "gold", 90,2)
  draw_building (t2, 250, -70, 250, 150, "gold", "gold", 90,2)
  draw_building (t2, 260, -75, 250, 150, "white", "gold", 90,4)

  draw_building (t2, 260.5, 176.5, 80, 5, "white", "white", 153.44, 0)
  draw_building (t2, 111.5, 176, 80, 5, "white", "white", 153.44, 0)
  draw_building (t2, 113, -72, 80, 5, "white", "white", 153.44, 0)

  draw_building (t2, 260, -75, 150, 150, "white", "greenyellow", 90,4)
  draw_building (t2, 270, -80, 150, 150, "greenyellow", "greenyellow", 90,2)
  draw_building (t2, 280, -85, 150, 150, "greenyellow", "greenyellow", 90,2)
  draw_building (t2, 290, -90, 150, 150, "greenyellow", "greenyellow", 90,2)
  draw_building (t2, 300, -95, 150, 150, "greenyellow", "greenyellow", 90,2)
  draw_building (t2, 310, -100, 150, 150, "greenyellow", "greenyellow", 90,2)
  draw_building (t2, 320, -105, 150, 150, "greenyellow", "greenyellow", 90,2)
  draw_building (t2, 330, -110, 150, 150, "greenyellow", "greenyellow", 90,2)

  draw_building (t2, 330, 42, 80, 5, "white", "white", 153.44, 0)
  draw_building (t2, 181, 42, 80, 5, "white", "white", 153.44, 0)
  draw_building (t2, 330, 38, 4, 150, "white", "white", 90, 0)
  draw_building (t2, 183, -107, 80, 5, "white", "white", 153.44, 0)

  draw_building (t2, 330, -110, 200, 150, "white", "mediumpurple1", 90, 4)
  draw_building (t2, 340, -115, 200, 150, "mediumpurple1", "mediumpurple1", 90, 2)
  draw_building (t2, 350, -120, 200, 150, "mediumpurple1", "mediumpurple1", 90, 2)
  draw_building (t2, 360, -125, 200, 150, "mediumpurple1", "mediumpurple1", 90, 2)
  draw_building (t2, 370, -130, 200, 150, "mediumpurple1", "mediumpurple1", 90, 2)
  draw_building (t2, 380, -135, 200, 150, "mediumpurple1", "mediumpurple1", 90, 2)
  draw_building (t2, 390, -140, 200, 150, "mediumpurple1", "mediumpurple1", 90, 2)
  draw_building (t2, 400, -145, 200, 150, "mediumpurple1", "mediumpurple1", 90, 2)

  draw_building (t2, 403.5, 56.5, 80, 5, "white", "white", 153.44, 0)
  draw_building (t2, 253, 56, 80, 5, "white", "white", 153.44, 0)
  draw_building (t2, 253, -142, 80, 5, "white", "white", 153.44, 0)

  draw_building (t2, 400, -145, 220, 150, "white", "indianred1", 90, 4)
  draw_building (t2, 410, -150, 220, 150, "indianred1", "indianred1", 90, 2)
  draw_building (t2, 420, -155, 220, 150, "indianred1", "indianred1", 90, 2)
  draw_building (t2, 430, -160, 220, 150, "indianred1", "indianred1", 90, 2)
  draw_building (t2, 440, -165, 220, 150, "indianred1", "indianred1", 90, 2)
  draw_building (t2, 450, -170, 220, 150, "indianred1", "indianred1", 90, 2)
  draw_building (t2, 460, -175, 220, 150, "indianred1", "indianred1", 90, 2)
  draw_building (t2, 470, -180, 220, 150, "white", "indianred1", 90, 4)

  draw_building (t2, 323, 39, 80, 5, "white", "white", 153.44, 0)
  draw_building (t2, 323, -177, 80, 5, "white", "white", 153.44, 0)

  # Make the street lamp with shape of rectangle and circle
  draw_rectangle (t2, 305, -225, 70, 10, "gray", "gray", 90, 2)
  draw_rectangle (t2, 145.5, -144.5, 70, 10, "gray", "gray", 90, 2)
  draw_rectangle (t2, -15, -65, 70, 10, "gray", "gray", 90, 2)
  draw_rectangle (t2, 25, -15, 70, 10, "gray", "gray", 90, 2)

  draw_rectangle (t2, -145.5, -180.5, 70, 10, "gray", "gray", 90, 2)
  draw_rectangle (t2, 15.5, -255.5, 70, 10, "gray", "gray", 90, 2)

  draw_circle (t2, 310, -155, 12, 0, 0, "orange", "orange", 2)
  draw_circle (t2, 305, -155, 7, 0, 0, "yellow", "yellow", 2)
  draw_circle (t2, 150.5, -74.5, 12, 0, 0, "orange", "orange", 2)
  draw_circle (t2, 145.5, -74.5, 7, 0, 0, "yellow", "yellow", 2)
  draw_circle (t2, -10, 5, 12, 0, 0, "orange", "orange", 2)
  draw_circle (t2, -15, 5, 7, 0, 0, "yellow", "yellow", 2)
  draw_circle (t2, 30, 55, 12, 0, 0, "orange", "orange", 2)
  draw_circle (t2, 25, 55, 7, 0, 0, "yellow", "yellow", 2)
  draw_circle (t2, -140.5, -110.5, 12, 0, 0, "orange", "orange", 2)
  draw_circle (t2, -145.5, -110.5, 7, 0, 0, "yellow", "yellow", 2)
  draw_circle (t2, 20.5, -185.5, 12, 0, 0, "orange", "orange", 2)
  draw_circle (t2, 15.5, -185.5, 7, 0, 0, "yellow", "yellow", 2)

main() # Call main() from which is made in def main()

name= ['C','H','I','C','A','G','O'] # Make the name of the sign by list and the title of the drawing
t3 = turtle.Turtle()
t3.hideturtle()
t3.penup()
t3.pencolor('yellow')
t3.goto(-137, 180)
t3.write((str(name[0])), # Call the first source of the list and put it into str() to print it correctly based on its type
        font=('Arial', 20, 'normal'))
t3.goto(-137, 140)
t3.write((str(name[1])),
        font=('Arial', 20, 'normal'))
t3.goto(-130, 100)
t3.write((str(name[2])),
        font=('Arial', 20, 'normal'))
t3.goto(-137, 60)
t3.write((str(name[3])),
        font=('Arial', 20, 'normal'))
t3.goto(-137, 20)
t3.write((str(name[4])),
        font=('Arial', 20, 'normal'))
t3.goto(-137, -20)
t3.write((str(name[5])),
        font=('Arial', 20, 'normal'))
t3.goto(-137, -60)
t3.write((str(name[6])),
        font=('Arial', 20, 'normal'))


student_uin = '673272656'
student_name = 'Yeonsoo Chang'
t3 = turtle.Turtle()
t3.hideturtle()
t3.penup()
t3.pencolor('black')
t3.goto(180,-170)
t3.write(str(student_uin) + ' - ' + str(student_name))