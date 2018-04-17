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
length1_SN = 0
width2_SN = 0
length2_SN = 0
width2_SN = 0
area1_SN = 0
area2_SN = 0

# Get the dimensions of rectangle 1.
length1_SN = int(input('Enter the length of rectangle 1: '))
width1_SN = int(input('Enter the width of rectangle 1: '))

# Get the dimensions of rectangle 2.
length2_SN = int(input('Enter the length of rectangle 2: '))
width2_SN = int(input('Enter the width of rectangle 2: '))

# Calculate the areas of the rectrangles.
area1_SN = length1_SN * width1_SN
area2_SN = length2_SN * width2_SN

# Determine which has the greater area.
if area1_SN > area2_SN:
    print('Rectangle 1 has the greater area.')
else:
    if area2_SN > area1_SN:
        print('Rectangle 2 has the greater area.')
    else:
        print('Both have the same area.')

# Printing the area for SA
print('The area of Rectangle 1 is ', area1_SN)
print('The area of Rectangle 2 is ', area2_SN)
