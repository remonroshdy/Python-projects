# This is A hangman game  where you are supposed to guess a word letter by letter.
# Everytime you guess a letter correctly  the letters of the word appears in its correct position
# Everytime you guess a letter mistakenly you loose a life of 7  chances you are given. a draw of the
# draw of the hangman appears in front of you.

import random

# here is the stages draws
from hangman_art import stages
from hangman_art import logo
print(logo)

#Step 1  our word of choice
from hangman_words import word_list


# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(word_list)

#print(word)

# this what is the word  will appear [ -,- , - ]
display = []
for _ in range(len(word)):
    display += "_"
print(display)

# these Variable to mark end of game and count number of lives chances player has
end_game = False
lives = 6

# the game

while not end_game:
    if lives == 0 :
        print("You loose")
        print(f"The word is {word}")
        print(logo)
        break

    # match var is used to know if the guessed letter is correct and based on that number of lives updated
    # and the hangman graph presented to the player  based on number of lives left

    guess = input("guess a letter  ").lower()

    # to update the guessed letters in the word
    for pos in range(len(word)):
        if word[pos] == guess:
            display[pos] = guess


    print(display)

    # here if the guessed letter is wrong we decrease lives and present the graph
    if guess not in word:
        lives -= 1
        print(stages[lives])
        print(f"The letter {guess} is not in the word ")


# to mark end of game when we guessed all letters and no more empty spaces..
    if "_" not in display:
        end_game = True
        print("You won !")
        print(f" you got it the correct word is { word}")
