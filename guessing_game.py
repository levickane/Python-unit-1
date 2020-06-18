"""This is a number guessing game. While True: the game will continue to prompt you to guess
random number between 0 and 20. It will store the amount of guesses in a list and then when
you finally guess the correct number it will tell you how many guesses it took you to get it
correct.
"""
import random

all_guesses = []    
high_score = []


def start_game():
    print("""
------------------------------------
Welcome to the number guessing game!
------------------------------------
    """)
    
    
def guessing_numbers():
    current_guesses = all_guesses.copy()
    key = random.randrange(0,10)
    while True:
      guess = int(input("Pick a number between 0 and 10.  "))
      current_guesses.append(guess)
      if (guess < 0) or (guess > 20):
        print("That's not within the range. Guess again")
        continue
      elif guess < key:
        print("It's higher")
        continue
      elif guess > key:
        print("It's lower")
        continue
      elif guess == key:
        break   
    print() 
    print("You got it!")
    print("It took you {} guesses to get it right!".format(len(current_guesses)))
    print()
    for item in current_guesses:
      high_score.append(item)
    
def start_again():
    while True:
      print()
      play_again = input("Would you like to play again? Y/N  ")
      print()
      if play_again.lower() == "y":
        print()
        print("The HIGHSCORE is {}".format(len(high_score)))
        print()
        guessing_numbers()
      elif play_again.lower() == "n":
        break
    print("GAME OVER")



# Kick off the program by calling the start_game function.
start_game()
guessing_numbers()
start_again()
