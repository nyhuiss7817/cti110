# CTI-110
# P4T2-Bug Collector
# program using the for loop to count and compile
# Steven Nyhuis
# 03/29/18

'''
An entomologist (someone who collects and studies insects) collects bugs every day for seven days. 

Write a program to help them with their studies. Your program should calculate a running total of
the number of bugs collected during the seven day period. 

You should write this program using a loop (the video suggests a for loop). Each time through the
loop, the program should ask for the number of bugs collected for that day.

When the loop is finished, the program should display the total number of bugs collected.
'''

# my varables

x = 0
bugs = 0
collected = 0

# my basic loop

for x in range (1, 8):
    print('On day ', x)
    bugs = int(input('How many bugs did you collect day?  '))
    collected += bugs

# my end of week total
    
if collected >= 1:
    print('Wow, you collected a total of ', collected, ' bugs this week!')
else:
    print ('Really, you collected ', collected, ' bugs and you are an entomologist?!?!')
