#Hangman Project
import random


start_game = input('Do you want to play Hangman?\n')

if start_game == "yes":
    print ("Lets Play...")


words = ['apple', 'bannana', 'orange']
guess_word = random.choice(words)
new_word = ['_' for x in guess_word]

print(' '.join(new_word))


while True:
    guess = (input('\nGuess a letter\n'))
    if guess in guess_word:
                for x, letter in enumerate(guess_word):
                    if letter == guess:
                        new_word[x] = guess
                        print(' '.join(new_word))

                if ''.join(new_word) == guess_word:
                    congratulations = "you correctly guessed"
                    print(f"{congratulations}" + " " + ''.join(new_word))
                    print('Game Over')
                    break
                elif ''.join(new_word) != guess_word:
                    print('Well done! Try another')









