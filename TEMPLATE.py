import random
import sys

words = [["", ""],["", ""],["", ""],["", ""],["", ""],["", ""],["", ""]]
guesses = 5
guesses_left = 5
random_word = random.choice(words)
word = random_word[0]
hint = random_word[1]

for x in range(6):
    print(hint)
    answer = input("Your Answer: ")
    if answer == word:
        print("You Won!")
        sys.exit()

    elif answer != word:    
        print("Please Try Again!")

print("Game Over!")
print("You Lose!")
