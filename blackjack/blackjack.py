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

    

        

    