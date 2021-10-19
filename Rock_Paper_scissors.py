# Making Computer play Rock Paper Scissors with us
# We will first define a fuction for the input choice

import random



def play():
    user = input('What\'s your choice Rock(r), Paper(p), Scissors(s): ')
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a Tie'
    
    # Apply the below steps after creating the other def function for the winning conditions
    if is_win(user, computer):
        return 'You won!'

    return 'You Lost!'


# Then We will make another function for when will a player(user) win
def is_win(player, opponent):
    # reutrn the True for the win
    # Here are the conditions r breaks s, s cuts p, p blocks r:
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())

# These are the output You will get:

#1. What's your choice Rock(r), Paper(p), Scissors(s): s
# It's a Tie

#2. What's your choice Rock(r), Paper(p), Scissors(s): p
# You Lost!

#3. What's your choice Rock(r), Paper(p), Scissors(s): p
# You won!