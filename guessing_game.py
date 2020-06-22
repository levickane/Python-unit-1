"""This is a number guessing game. While True: the game will continue to prompt you to guess
random number between 0 and 20. It will store the amount of guesses in a list and then when
you finally guess the correct number it will tell you how many guesses it took you to get it
correct.
"""

import random

current_guesses = []   
high_score = [1,2,3,4,5,6,7,8,9,0]

def start_game():
    print("""
------------------------------------
Welcome to the number guessing game!
------------------------------------
    """)
    
    
def guessing_numbers():
    key = random.randrange(0,10)
    while True:
        try:
            guess = int(input("Pick a number between 0 and 10.  "))
            current_guesses.append(guess)
            if (guess < 0) or (guess > 10):
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
        except ValueError:
            print("INVALID. Try Again.")
    print() 
    print("You got it!")
    print("It took you {} guesses to get it right!".format(len(current_guesses)))
    print()
    if len(current_guesses) < len(high_score):
        high_score.clear()
        high_score.extend(current_guesses)     
    
      

    
def start_again():
    while True:
      print()
      play_again = input("Would you like to play again? Y/N  ")
      print()
      if play_again.lower() == "y":
        current_guesses.clear()
        print()
        print("The HIGHSCORE is {}".format(len(high_score)))
        print()
        guessing_numbers()
      elif play_again.lower() == "n":
        print ("The HIGHSCORE of the game was {}".format(len(high_score)))
        break
    print("GAME OVER")



# Kick off the program by calling the start_game function.
start_game()
guessing_numbers()
start_again()