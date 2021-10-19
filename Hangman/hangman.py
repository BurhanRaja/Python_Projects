# Hangman is my folder name
from words import words
import random
import string
from hangman_visual import lives_visual_dict

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words) # Random words we get from above function
    alphabet = set(string.ascii_uppercase) # All the alphabets in English Diction
    word_letters = set(word) # Set of letters in a word
    used_letters = set() # Set of used letters

  
    lives = 7   # Lives You get to guess the number

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters)) # ' '.join(['a', 'b', 'cd']) --> 'a b cd' shows no. of lives left and what letters have you guessed
        word_list = [letter if letter in used_letters else '-' for letter in word] # what current word is (ie W - R D)
        print(lives_visual_dict[lives]) # Dictionary from hangman_visual.py
        print('Current word: ', ' '.join(word_list)) # Here you keep the track of the letter you have guessed and what more is to be guessed

        user_letter = input('Guess Word: ').upper()
        if user_letter in alphabet - used_letters: # This loop is for Removing the alphabets that are used and adding it to the list i.e. used_letters
            used_letters.add(user_letter)
            if user_letter in word_letters: # This loop is for the letters that are in words
                word_letters.remove(user_letter)
                print('')
            else: # This else is for if you guess the wrong letter than the message below will be shown
                lives = lives-1 
                print('The letter',user_letter ,'you guessed is not in the word')
        elif user_letter in used_letters: # This loop is for that you have already used the letters
            print('You have already used this letter')
        else:
            print('The letter is invalid') # If the letters are not used and are not valid will print this
    if lives==0:
        print('Sorry! You died. The word was', word) # This will be print when you lose
    else:
        print('Yay! You won the game. You guess the word correctly.', word) # This will be print when you win the game

if __name__ == '__main__':
    hangman()



# The situation below is when you lose the game
# This is how the game is played




# You have 7 lives left and you have used these letters:  

# Current word:  - - - -
# Guess Word: a

# You have 7 lives left and you have used these letters:  A

# Current word:  - A - -
# Guess Word: p
# The letter P you guessed is not in the word
# You have 6 lives left and you have used these letters:  A P

#                |
#                |
#                |
#                |
#                |

# Current word:  - A - -
# Guess Word: f
# The letter F you guessed is not in the word
# You have 5 lives left and you have used these letters:  F A P

#                 ___________
#                | /
#                |/
#                |
#                |
#                |

# Current word:  - A - -
# Guess Word: t
# The letter T you guessed is not in the word
# You have 4 lives left and you have used these letters:  F A P T

#                 ___________
#                | /        |
#                |/
#                |
#                |
#                |

# Current word:  - A - -
# Guess Word: r
# The letter R you guessed is not in the word
# You have 3 lives left and you have used these letters:  F R T A P

#                 ___________
#                | /        |
#                |/        ( )
#                |
#                |
#                |

# Current word:  - A - -
# Guess Word: s
# The letter S you guessed is not in the word
# You have 2 lives left and you have used these letters:  F S R T A P

#                 ___________
#                | /        |
#                |/        ( )
#                |          |
#                |
#                |

# Current word:  - A - -
# Guess Word: w
# You have 1 lives left and you have used these letters:  F S R T W A P

#                 ___________
#                | /        |
#                |/        ( )
#                |          |
#                |         /
#                |

# Current word:  - A - -
# Guess Word: m
# The letter M you guessed is not in the word
# Sorry! You died. The word was HAND











# The situation below is when you win the game

# PS C:\Users\burhan\Desktop\AI and DS files\Python Projects> python hangman.py
# You have 7 lives left and you have used these letters:  

# Current word:  - - - - - -
# Guess Word: h
# The letter H you guessed is not in the word
# You have 6 lives left and you have used these letters:  H

#                |
#                |
#                |
#                |
#                |

# Current word:  - - - - - -
# Guess Word: a

# You have 6 lives left and you have used these letters:  A H

#                |
#                |
#                |
#                |
#                |

# Current word:  - A - - - -
# Guess Word: b

# You have 6 lives left and you have used these letters:  A H B

#                |
#                |
#                |
#                |
#                |

# Current word:  B A B - - -
# Guess Word: r
# The letter R you guessed is not in the word
# You have 5 lives left and you have used these letters:  A R H B

#                 ___________
#                | /
#                |/
#                |
#                |
#                |

# Current word:  B A B - - -
# Guess Word: e

# You have 5 lives left and you have used these letters:  A R B H E

#                 ___________
#                | /
#                |/
#                |
#                |
#                |

# Current word:  B A B - E -
# Guess Word: d
# The letter D you guessed is not in the word
# You have 4 lives left and you have used these letters:  A R B D H E

#                 ___________
#                | /        |
#                |/
#                |
#                |
#                |

# Current word:  B A B - E -
# Guess Word: c
# The letter C you guessed is not in the word
# You have 3 lives left and you have used these letters:  A R B D C H E

#                 ___________
#                | /        |
#                |/        ( )
#                |
#                |
#                |

# Current word:  B A B - E -
# Guess Word: i

# You have 3 lives left and you have used these letters:  A R B I D C H E

#                 ___________
#                | /        |
#                |/        ( )
#                |
#                |
#                |

# Current word:  B A B I E -
# Guess Word: r
# You have already used this letter
# You have 3 lives left and you have used these letters:  A R B I D C H E

#                 ___________
#                | /        |
#                |/        ( )
#                |
#                |
#                |

# Current word:  B A B I E -
# Guess Word: z
# The letter Z you guessed is not in the word
# You have 2 lives left and you have used these letters:  A R B I D C Z H E

#                 ___________
#                | /        |
#                |/        ( )
#                |          |
#                |
#                |

# Current word:  B A B I E -
# Guess Word: s

# Yay! You won the game. You guess the word correctly. BABIES