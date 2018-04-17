# CTI-110
# P2HW1_DistanceTraveled
# Distance calculator for three different distances
# Steven Nyhuis
# 02/20/18


'''
Write a program that solves the following problem:

A car is traveling at 70 miles per hour. Display the following:
    The distance the car will travel in 6 hours
    The distance the car will travel in 10 hours
    The distance the car will travel in 15 hours

In Python, assuming the variables speed and time are already defined, this could be written as
distance = speed * time
'''


# List the constants
SPEED = 70

# List the varables
distance = 0
time = 0

# use def to define formula and output

def distance_formula():
    distance = SPEED * time
    print('The distance after', time, 'hours is', distance, 'miles')

# Output

print('While driving a car at 70 miles per hour...')
time = 6
distance_formula()
time = 10
distance_formula()
time = 15
distance_formula()
