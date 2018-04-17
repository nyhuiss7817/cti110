# CTI-110
# P4HW1_DistanceTraveledToo
# Distance table from imput
# Steven Nyhuis
# 04/11/18


'''
Write a program that asks the user two questions: The speed of a vehicle, and
the number of hours it has traveled. The program should then display the
distance that the vehicle has traveled for each hour of that time period. Your
output should be displayed in table format. 
'''


# List the varables
distance = 0
time = int
speed = int

# Ask for user input

speed = int(input('What was the speed of the vehicle in mph?  '))
time = int(input('How many whole hours has it traveled?  '))

# set up the table

print('\n')
print('Hour          Distance Traveled')
print('-------------------------------')


# starting loop

for x in range (1, time+1):
    distance = speed * x
    print(x,'\t','\t', distance)









