"""This is a number guessing game. While True: the game will continue to prompt you to guess
random number between 0 and 20. It will store the amount of guesses in a list and then when
you finally guess the correct number it will tell you how many guesses it took you to get it
correct.
"""
import random

all_guesses = []    

def start_game():
    print("""
------------------------------------
Welcome to the number guessing game!
------------------------------------
    """)
    key = random.randrange(0,20)
    while True:
      guess = int(input("Pick a number between 0 and 20.  "))
      all_guesses.append(guess)
      if guess < key:
        print("It's higher")
        continue
      elif guess > key:
        print("It's lower")
        continue
      elif guess == key:
        break
    print("You got it!")
    print("It took you {} guesses to get it right!".format(len(all_guesses)))
    print("The game is over now.")



# Kick off the program by calling the start_game function.
start_game()
