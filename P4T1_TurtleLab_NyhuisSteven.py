# CTI-110
# P4T1-Turtle Lab
# turtle graphics programs
# Steven Nyhuis
# 04/10/18

'''
Using turtle graphics, and either a while or for loop, write a program that
draws both a square and a triangle. (In this case, it's okay if they overlap
- just make sure both shapes are visible.)

However, your code should use a while loop or a for loop to draw both the square
and the triangle.
'''

# initiating turles and back ground

import turtle       
win = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

# my square

for x in range (1, 5):
    t.pensize(4)            
    t.pencolor("blue")
    t.forward(100)
    t.right(90)

# my triangle

for x in range (1, 4):
    t.pensize(4)            
    t.pencolor("green")
    t.forward(-100)
    t.right(120)
