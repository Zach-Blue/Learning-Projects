#Hangman Project
import random

start_game = input('Do you want to play Hangman?\n')

if start_game == "yes":
    print ("Lets Play...")


words = ['apple', 'bannana', 'orange']
guess_word = random.choice(words)
new_word = len(guess_word) *str('_')

print(new_word)

#for x in guess_word:
    #print ("_", end = "")

guess = (input('\nGuess a letter\n'))
if guess in guess_word:
            for index, letter in enumerate(guess_word):
                if letter == guess:
                    guess_word[index] = guess
            print('Word to guess:', ' '.join(guess_word))

    #print(guess)

#print(guess_word)


