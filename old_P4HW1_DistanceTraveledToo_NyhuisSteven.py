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
time = 0
speed = 0

# Ask for user input

speed = input('What was the speed of the vehicle in mph?  ')


# validate input

if speed != int:
    print('Please inter a whole number.')
    speed = input('What was the speed of the vehicle in mph?  ')
else:
    print('\n')

time = input('How many whole hours has it traveled?  ')
if time != int:
    print('Sorry, but this calculator is for one or more whole hours.')
    hour = input('How many whole hours has it traveled?  ')
else:
    print('\n')
       
print('Your vehicle speed in mph is:', speed)   #need to finish
print('You have traveled:', time)              #need to finish
print('Hour          Distance Traveled')
print('-------------------------------')


# starting loop

for x in range (1, time+1):
    distance = speed * x
    print(x,'\t','\t', distance)









