# imports
import os
import time
import string
import random
import sys


def printy(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Load screen
os.system('clear')
print(
    '''  __  __ __  __  ___ _____    ___ __  _   ____  _ _    __ _____ __  ___  
/' _/|  V  |/  \| _ \_   _|  / _//  \| | / _/ || | |  /  \_   _/__\| _ \ 
`._`.| \_/ | /\ | v / | |   | \_| /\ | || \_| \/ | |_| /\ || || \/ | v / 
|___/|_| |_|_||_|_|_\ |_|    \__/_||_|___\__/\__/|___|_||_||_| \__/|_|_\ 

Loading...''')
time.sleep(5)
os.system('clear')


def calculate():
    operation = input('''
  __  __ __  __  ___ _____    ___ __  _   ____  _ _    __ _____ __  ___  
/' _/|  V  |/  \| _ \_   _|  / _//  \| | / _/ || | |  /  \_   _/__\| _ \ 
`._`.| \_/ | /\ | v / | |   | \_| /\ | || \_| \/ | |_| /\ || || \/ | v / 
|___/|_| |_|_||_|_|_\ |_|    \__/_||_|___\__/\__/|___|_||_||_| \__/|_|_\ 

Please type in the math operation you would like to use:
+ for addition
- for subtraction
x for multiplication
/ for division
** for power
% for modulo

>>> ''')
    os.system('clear')
    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        os.system('clear')
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        os.system('clear')
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == 'x':
        os.system('clear')
        print('{} x {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        os.system('clear')
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '**':
        os.system('clear')
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1**number_2)

    elif operation == '%':
        os.system('clear')
        print('{} % {} = '.format(number_1, number_2))
        print(number_1 % number_2)

    else:
        os.system('clear')
        print('You have not typed a valid operator.')

    # Add again() function to calculate() function
    again()


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.

>>> ''')

    if calc_again.upper() == 'Y':
        os.system('clear')
        calculate()
    elif calc_again.upper() == 'N':
        os.system('clear')
        print(
            '''  __  __ __  __  ___ _____    ___ __  _   ____  _ _    __ _____ __  ___  
/' _/|  V  |/  \| _ \_   _|  / _//  \| | / _/ || | |  /  \_   _/__\| _ \ 
`._`.| \_/ | /\ | v / | |   | \_| /\ | || \_| \/ | |_| /\ || || \/ | v / 
|___/|_| |_|_||_|_|_\ |_|    \__/_||_|___\__/\__/|___|_||_||_| \__/|_|_\ 

Stoping Program... Goodbye!''')
    else:
        os.system('clear')
        again()


calculate()
