#Hangman Project
import random

start_game = input('Do you want to play Hangman?\n')

if start_game == "yes":
    print ("Lets Play...")


words = ['apple', 'bannana', 'orange']
guess_word = random.choice(words)

print(guess_word)

