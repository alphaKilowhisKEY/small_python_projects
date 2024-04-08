"""
Blackjack Game

This script implements a simplified version of the Blackjack card game.
It utilizes the random module to deal cards and determine outcomes.
The game is played between a user and a dealer controlled by the computer.

Dependencies:
    - random: A module to generate random numbers and choices.
    - logo: A module containing the ASCII art for the game logo.

Functions:
    - deal_card(): Returns a random card from the deck (values 2 to 11).
    - calculate_score(cards): Takes a list of cards and returns their total score.
    - compare(user_score, dealer_score): Compares the scores of the user and the dealer to determine the winner.
    - play_game(): Manages the game flow, dealing cards to the user and the dealer, and determining the winner.

Usage:
    - Run the script to play the Blackjack game.
    - Follow the prompts to decide whether to take another card or pass.
    - The game ends when the user decides to pass, goes over 21, or achieves a Blackjack.
    - After the user finishes, the dealer draws cards until their score is 17 or higher.
    - The winner is determined based on the scores.
    - You can play multiple rounds by entering 'y' when prompted.

Example:
    $ python blackjack_game.py
    Do you want to play a game of Blackjack? Type 'y' or 'n': y
    # Game output will be displayed based on the gameplay.
"""
import random
import logo
#from replit import clear

# Returns a random card from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Take a list of cards and return the sum
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose."    
    elif dealer_score > 21:
        return "Dealer went over. You win." 
    elif user_score > dealer_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():    

    print(logo.logo)
    user_cards = []
    dealer_cards = []
    is_game_over = False

    # Adding randomly cards fro user and dealer
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:    

        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True    

    while dealer_score !=0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand:  {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': "):
    #clear()
    play_game()

    

        

    