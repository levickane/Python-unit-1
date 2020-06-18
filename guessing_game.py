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
    
    
def guessing_numbers():
    key = random.randrange(0,10)
    while True:
      guess = int(input("Pick a number between 0 and 10.  "))
      all_guesses.append(guess)
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
    print("It took you {} guesses to get it right!".format(len(all_guesses)))
    print()


def start_again():
  while True:
    print()
    print("The HIGHSCORE is {}".format(len(all_guesses)))
    print()
    play_again = input("Would you like to play again? Y/N  ")
    print()
    if play_again.lower() == "y":
      guessing_numbers()
    elif play_again.lower() == "n":
      break
  print("GAME OVER")



# Kick off the program by calling the start_game function.
start_game()
guessing_numbers()
start_again()
