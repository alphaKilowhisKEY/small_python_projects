"""
Number Guessing Game

This script allows users to play a number guessing game. The program randomly selects a number between 1 and 100,
and the user must guess the number within a limited number of attempts.

Dependencies:
    - randint: From the random module for generating random integers.

Constants:
    - EASY_LEVEL_TURNS (int): The number of attempts allowed for the easy level.
    - HARD_LEVEL_TURNS (int): The number of attempts allowed for the hard level.

Usage:
    Run this script to start the Number Guessing Game by: >>python3 guess_number.py
    Follow the prompts to choose a difficulty level (easy or hard) and make guesses to determine the chosen number.
    You have a limited number of attempts to guess the correct number.
"""

from random import randint
chosen_number = randint(1, 100)

#print(chosen_number)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_level():
    level = input("Choose a diffuclty. Type 'easy' or 'hard': ")
    if level == 'easy':
        attempts = EASY_LEVEL_TURNS
    else:
        attempts = HARD_LEVEL_TURNS
    return attempts    

def check_guess(guess):
    if guess == chosen_number:
        print(f"You got it! The answer was {guess}.")
        return attempts
    elif guess < chosen_number:
        print("Too low!")
        return attempts - 1
    else:
        print("Too high!")
        return attempts - 1
        
    
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
attempts = set_level()
guess = 0

while attempts > 0 and guess != chosen_number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = check_guess(guess)

if attempts <= 0:
    print("You lose!")