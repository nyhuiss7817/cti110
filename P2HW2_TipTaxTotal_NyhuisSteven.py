# CTI-110
# P2HW2 TipTaxTotal
# Calculator for tip, tax, and total from user imput
# Steven Nyhuis
# 02/20/18

'''
Write a program that calculates the total cost of a meal purchased at a restaurant.
The program should ask the user to enter the charge for the food. It should then
calculate the amount of the tip and the amount for sales tax. (Assume 18% tip and 7% sales tax.)

Display both of these amounts as well as the total cost of the meal. 
'''

# List Constants (sales tax and tip rate)
TIP = 0.18
TAX = 0.07

# list of varables (actual sales tax and tip amount not rate)
meal = 0.0
tax = 0.0
tip = 0.0

# Recibe the cost of meal from user imput.
meal = float(input('Enter the price of the meal: '))

# Calculate the sales tax, tip, and total from user imput.
tax = meal * TAX
tip = meal * TIP
total = tax + tip + meal

# Display the sales tax, tip, and total cost.
print('The subtotal is.............. $', format(meal, ',.2f'))
print('7% sales tax is............... $', format(tax, ',.2f'))
print('15% tip is.................... $', format(tip, ',.2f'))
print('The total cost of the meal is $', format(total, ',.2f'))
