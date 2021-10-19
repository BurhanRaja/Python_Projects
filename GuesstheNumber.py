# Let's make a new game called Guessing game by both the user and the computer 
# First We will write the code for the user to guess and computer to decide the random number

# User Guessing game

# Define a function for the user to guess and computer to determine

import random

def user_guess(x):
    random_number_user = random.randint(1, x)
    guess=0
    while guess != random_number_user:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number_user:
            print(f'Sorry! The number you have guessed is too low.')
        elif guess > random_number_user:
            print(f'Sorry! The number you have guessed is too high')
    print(f'Yay! You guessed the number correctly : {random_number_user}')

user_guess(20)

# This will be the ouput you will be getting for this function or game

# Guess a number between 1 and 20: 15
# Sorry! The number you have guessed is too low.
# Guess a number between 1 and 20: 18
# Sorry! The number you have guessed is too high
# Guess a number between 1 and 20: 16
# Yay! You guessed the number correctly : 16


# Computer Guessing game

# Define a function for the computer to guess and user to determine

def computer_guess(y):
    low = 1
    high = y
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # Here it could also be high because low=high
        feedback = input(f'Is {guess} is too high(h), too low(l) or correct(c): ') # Here the computer will ask us and we have to give it an arguement i.e. if it is h, l or c.
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! the computer has guessed your number, {guess}, correctly')

computer_guess(10)


# This is how the computer will guess the number correctly

# Is 2 is too high(h), too low(l) or correct(c): l
# Is 6 is too high(h), too low(l) or correct(c): l
# Is 7 is too high(h), too low(l) or correct(c): l
# Is 10 is too high(h), too low(l) or correct(c): h
# Is 8 is too high(h), too low(l) or correct(c): c
# Yay! the computer has guessed your number, 8, correctly