"""
Hangman Game

This script implements a simple Hangman game where players must guess letters in a randomly chosen word.
Players have a limited number of lives, and incorrect guesses result in losing a life.
The game ends when the player correctly guesses the word or runs out of lives.

Dependencies:
    - random: For generating random choices.
    - word_list: A module containing a list of words for the game.
    - ascii_hangman: A module containing ASCII art for Hangman stages.

Usage:
    Run this script to start the Hangman game by: >> python3 hangman.py
    Players must guess letters to complete the hidden word.
    Players have 6 lives to guess incorrectly before losing the game.
"""

import random
import word_list
import ascii_hangman

# Randomly choose the word from list of words
chosen_word = random.choice(word_list.word_list)
end_of_game = False
lives = 6

print(ascii_hangman.logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = ['_'] * len(chosen_word)
print(display)

# Game loop
while not end_of_game:
    print(f"You have {lives} lives.") 
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            
    if(guess not in chosen_word):
        lives -= 1 
        if lives == 0:
            end_of_game = True
            print("You loose!")  
            print(f"The right word was: {chosen_word}.")  

    print(display)

    if '_' not in display:
        end_of_game  = True
        print("You win!")

    print(ascii_hangman.stages[lives])