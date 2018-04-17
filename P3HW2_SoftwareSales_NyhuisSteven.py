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

    # varable list
    tcost = 0
    discount = 0
    software = 0

    # discount list converted from above list (constant)
    ONE = 0.10
    TWO = 0.20
    THREE = 0.30
    FOUR = 0.40

    # method for figuring and printing cost

    def cost():
        tcost = software * 99 - discount
        print('You have a discount of $', format(discount, ',.2f'))
        print('Your total cost is $', format(tcost, ',.2f'))

   # logic for discount amount

    software = int(input('Enter quantity of software: '))

    if software >= 100:
        discount = software * FOUR * 99
        cost()
    else:
        if software >= 50:
            discount = software * THREE * 99
            cost()
        else:
            if software >= 20:
                discount = software * TWO * 99
                cost()
            else:
                if software >= 10:
                    discount = software * ONE * 99
                    cost()
                else:
                    discount = 0
                    cost()
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
