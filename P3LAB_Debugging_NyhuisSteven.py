# CTI-110
# P3LAB_Debugging
# Complete and debug provided program
# Steven Nyhuis
# 03/20/18

'''
For this lab we will be simulating a very common situation you will experience in
real-world software development.
Your manager calls you into his office. You’re being assigned to work on a program that
faculty will use to calculate student grades. Your manager has good news, and bad news.

The Good News: The program is already partially finished!

The Bad News: The program is only partially finished. Also, it’s full of bugs.
In particular, the indentation blocks are all wrong.

Your assignment is to complete and debug the provided program, test it, and
submit the working program.
'''


# This program takes a number grade and outputs a letter grade.
def main():

    # System uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    # define the rest of the scores

    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
            print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is: C')
            else:
                if score >= D_score:
                    print('Your grade is: D')
                else:
                    print('Your grade is: F')

    # Finish with def main() 



# program start
main()

