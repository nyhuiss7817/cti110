# CTI-110
# P3HW1 Age Classifier
# Classifier of a person by age
# Steven Nyhuis
# 03/20/18

'''
Write a program that asks the user to enter a person’s age. The person should display a
message indicating whether the person is an infant, a child, a teenager, or an adult.
Follow these guidelines:
If the person is 1 year old or less, he or she is an infant.
If the person is older than one year, but younger than 13 years, he or she is a child.
If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
If the person is at least 20 years old, he or she is an adult. 
'''

# create a def for main classifier
def age():

    # age list
    ADULT = 20
    TEEN = 13
    CHILD = 1

    # define the rest of the scores

    age = float(input('Enter age in years: '))

    if age >= ADULT:
        print('You are an Adult')
    else:
        if age >= TEEN:
            print('You are a Teenager')
        else:
            if age > CHILD:
                print('You are a Child')
            else:
                print('You are an Infant')

    # Finish with the def age() 


# program start
age()
age()
age()
age()
age()
age()
age()
age()
age()
