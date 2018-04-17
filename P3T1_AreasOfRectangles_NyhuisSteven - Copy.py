# CTI-110
# P3T1-Areas of rectangle
# program to compare the size of two retangles
# Steven Nyhuis
# 03/06/18

'''
Write a program that asks for the length and width of two rectangles.
The program should tell the user which rectangle has the greater area,
or if the two rectangles have equal area.

This program’s logic should have three branches:
1.	The first rectangle has the larger area
2.	The second rectangle has the larger area
3.	Both rectangles have equal area
'''


# list of varables


# def function of rectangle
def rectangle_area():

# list of varables in fuction

    length_SN = 0
    width_SN = 0
    area = 0

# get dimintions and figure area of rectangle

    length_SN = int(input('Enter the length of rectangle: '))
    width_SN = int(input('Enter the width of rectangle: '))
    area = length_SN * width_SN
    print('The area of Rectangle is ', area)

rectangle_area(1)
rectangle_area(2)


# Determine which has the greater area.
if rectangle_area(1) > rectangle_area(2):
    print('Rectangle 1 has the greater area.')
else:
    if rectangle_area(2) > rectangle_area(1):
        print('Rectangle 2 has the greater area.')
    else:
        print('Both have the same area.')


