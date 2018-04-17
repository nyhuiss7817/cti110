# CTI-110
# P4HW2_RunningTotal
# running total of positive input
# Steven Nyhuis
# 04/11/18


'''
Write a program that asks the user to enter a series of numbers. It should
loop, adding these numbers to a running total, until the user enters a negative
number. When a negative number is entered, the program should exit the loop.
(It should not add the negative number to the total.) The program should then
print the total before exiting. . 
'''


# List the varables

number = 0
total = 0

# input loop for accumulator with negitive number filter

number = float(input("Please enter a number."))

while number >= 0:
    total = total + number
    number = float(input("Please enter a number."))

# output

print('Total: ', total)







