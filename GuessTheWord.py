import random
import sys

words = [["music", "People love my beats!"], ["origami", "The art of folding."], ["line", "I am a dot, that went for a walk."], ["cell", "I am in all living things (one way or the other)."], ["atom", "I make up all objects."], ["bag", "I can hold many objects."], ["cotton candy", "I am the confection made by a dentist."], ["fuel", "I make cars work (and trucks and other machines)."], ["water", "I am also known as H2O."], ["hydrox", "I am the origial Oreo."]]
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