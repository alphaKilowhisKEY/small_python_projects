"""
NATO Phonetic Alphabet Translator

This script imports the Pandas library to read a CSV file containing the NATO phonetic alphabet.
It then creates a dictionary mapping letters to their corresponding NATO phonetic code words.
The script prompts the user to input a word, converts it to uppercase, and prints the NATO 
phonetic code words for each letter in the word.

Dependencies:
    - Pandas: A powerful data analysis and manipulation library.

Usage:
    - Ensure you have the Pandas library installed. You can install it via pip:
        pip install pandas
    - Place the CSV file containing the NATO phonetic alphabet in the same directory as this script.
    - Run the script and follow the prompt to input a word.

Example:
    $ python3 main.py
    Give a name: Hello
    ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']

"""
import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

#Create a dictionary:
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Give a name: ").upper()
result = [nato_dict[letter] for letter in user_input if letter in nato_dict]
print(result)