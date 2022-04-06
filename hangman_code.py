from hangman_drawings import *
from hangman_functions import *

# Game launch
print("\n")
loading_game()

print("""
                            ######################
                            #    Hangman Game    #
                            ######################
""")

print("""
                       # Bienvenue dans le jeu du pendu #

""")


# Random word selection and preparing the guess line
word = word_selection(words_list).upper()
word_fill = word_length(word) * word_shape()

# Initialising variables 
attempts = 0
list_used = []
win = False

# While loop with the number of allowed attempts while the player hasn't won
while attempts < 9 and not win: 
    print(f"\nWord to guess: {word_fill}\n")
    # Calling for user input
    letter_choice = input("Choose a letter: ")
    clear()
    
    # Correct input
    if letter_choice.isalpha() and len(letter_choice) == 1:  
        letter_choice = letter_choice.upper()
        print(f"You chose the letter: {letter_choice}\n")
        #time.sleep(1)

        # Success - letter in the word
        if letter_choice not in list_used and letter_choice in word:
            print("Well done! You found a letter.\n")
            word_fill = letter_found(word, letter_choice, word_fill)

        # Fail - letter not in the word
        elif letter_choice not in list_used and letter_choice not in word:
            print("Sorry, this letter is not in the word.\n")
            attempts += 1

        # Error - letter already used
        else:
            print("You've already tried this letter. Please give a new letter.\n")
            continue    # continue to get out of the "if" condition and ask again for player input
        
        # Drawing the current hangman 
        drawing_number(attempts)   

        # After processing the input, we add the letter to the list of used letters
        list_used.append(letter_choice)
        print(f"Used letters: {list_used}\n")
        time.sleep(1)

        # Checking if the player hasn't already guessed all the letters + Win message
        if "_" not in word_fill:
            print(f"You found the word: {word}\n")
            print(f"CONGRATS! YOU WIN!!!\n")
            win = True
            break

    # Incorrect input
    else:
        print("Wrong input. Please provide a letter.\n")

# If player loses
if not win:
    dead_func()
    time.sleep(1)
    print(f"The word to guess was: {word}\n")

print("""
    ######################
""")
