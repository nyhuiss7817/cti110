# CTI-110
# P4T1c: Snowflake
# turtle graphics programs with snowflakes
# Steven Nyhuis
# 04/10/18

# window design and condition setup
import turtle
import random                       #a random generator
win = turtle.Screen()
win.bgcolor("powderblue")
t = turtle.Turtle()
t.shape("turtle")
colours = ["red", "white", "blue"]  #my "color" pool
t.pensize(3)
t.color("red")

# the snow flake method

def snowflake():
    for x in range(10):
        t.forward(100)
        t.right(60)
        t.forward(100)
        for x in range(2):   #the tip of the flake
            t.forward(20)
            t.left(60)
            t.forward(20)
            t.left(120)
        t.right(120)
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(156)
        t.color(random.choice(colours))

#now to place the snowflakes in four places

t.penup()
t.forward(150)
t.right(90)
t.forward(150)
t.pendown()
snowflake()
for x in range(3):
    t.penup()
    t.right(90)
    t.forward(300)
    t.pendown()
    snowflake()

