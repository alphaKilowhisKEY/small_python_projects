from random import randint
from data import data
import logo

NUM_ITEMS = len(data) # 50 different items
game_is_over = False
user_score = 0

# display function for item, return a string
def display(item):
    return f"{data[item]['name']}, a {data[item]['description']}, from {data[item]['country']}."   

# choose 2 different items from list randomly, return both
def pick_item():
    item1 = randint(0, NUM_ITEMS - 1)
    item2 = randint(0, NUM_ITEMS - 1)
    if item1 == item2:
        item2 = randint(0, NUM_ITEMS -1)
    return item1, item2    

# compare them and return the biggest accroding number of followers
def compare(item1, item2):
    if data[item1]['follower_count'] > data[item2]['follower_count']:
        return 'A'
    else:
        return 'B'


print(logo.logo)

# Game loop
while not game_is_over:
    item1, item2 = pick_item()
    print(f"Compare A: {display(item1)}")
    print(logo.vs)
    print(f"Against B: {display(item2)}")
    result = compare(item1, item2)
    user_guess = input("Who has more followers? Type 'A' or 'B': ")
    if user_guess == result:
        user_score += 1
        print(f"Right! Your score: {user_score}")
    else:
        print(f"Sorry, that's wrong. Final score: {user_score}")
        game_is_over= True