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