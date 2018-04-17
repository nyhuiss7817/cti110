# CTI-110
# P4T1b: Initials
# turtle graphics programs with my initials
# Steven Nyhuis
# 04/10/18

'''
Using turtle graphics, write a program that displays your first and last
initials. Choose a color and penSize of your choice.

You will want to draw your first initial, raise the turtle's pen with penUp,
then move to the right and lower the pen to draw your second initial..
'''

# initiating turtles and back ground

import turtle       
win = turtle.Screen()
win.bgcolor("khaki")   # heh, background color
win.title("My Initials")   # window title
t = turtle.Turtle()
t.shape("turtle")

# for the s
t.pensize(4)
t.pencolor("red")
t.forward(-50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(180)

# transition to the n

t.penup()
t.forward(70)
t.left(90)
t.pendown()

# for the n

t.forward(100)
t.right(150)
t.forward(115)
t.left(150)
t.forward(100)

# for the lines

t.right(180)
t.penup()
t.forward(110)
t.right(90)
t.pendown()
t.forward(127)
t.penup()
t.right(270)
t.forward(10)
t.pendown()
t.right(-90)
t.forward(127)
t.penup()
t.left(270)
t.forward(10)
t.pendown()
t.right(90)
t.forward(127)

# a box for aaron because he wanted one, blue

t.pensize(2)
t.penup()
t.forward(10)
t.pendown()
t.pencolor("blue")
t.right(90)
t.forward(140)
for x in range (4):
    t.right(90)
    t.forward(150)
