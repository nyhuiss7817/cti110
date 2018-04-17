# CTI-110
# P3HW2 Software Sales
# Calculator for sales of software with possible discounts
# Steven Nyhuis
# 03/22/18

'''
A software company sells a package that retails for $99. They offer bulk discounts
for volume purchases. The discounts are as follows:

Quantity 10-19: 10% discount
Quantity 20-49:	20% discount
Quantity 50-99:	30% discount
Quantity 100+:	40% discount

Write a program that asks the user to enter the number of packages purchased. The
program should then display the amount of the discount (if any) and the total purchase
cost with the discount applied.
 
'''


# create a method to figure discount
def discount():

    # discount list
    ONE = 0.10
    TWO = 0.20
    THREE = 0.30
    FOUR = 0.40

    # calculate discount and cost

    software = int(input('Enter quantity of software: '))

    if software >= 100:
        discount = software * FOUR * 99
        tcost = software * 99 - discount
        print('You have a 40% discount of $', format(discount, ',.2f'))
        print('Your total cost is $', format(tcost, ',.2f'))
    else:
        if software >= 50:
            discount = software * THREE * 99
            tcost = software * 99 - discount
            print('You have a 30% discount of $', format(discount, ',.2f'))
            print('Your total cost is $', format(tcost, ',.2f'))
        else:
            if software >= 20:
                discount = software * TWO * 99
                tcost = software * 99 - discount
                print('You have a 20% discount of $', format(discount, ',.2f'))
                print('Your total cost is $', format(tcost, ',.2f'))
            else:
                if software >= 10:
                    discount = software * ONE * 99
                    tcost = software * 99 - discount
                    print('You have a 10% discount of $', format(discount, ',.2f'))
                    print('Your total cost is $', format(tcost, ',.2f'))
                else:
                    tcost = software * 99
                    print('You do not have a discount.')
                    print('Your total cost is $', format(tcost, ',.2f'))
    # add a line space
    print ('\n')
    
# run method

discount()
discount()
discount()
discount()
discount()
discount()
discount()
discount()
discount()
discount()
