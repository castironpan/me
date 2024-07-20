"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    # do try catch for non int inputs 
    #

    print("\nWelcome to the guessing game!")
    lowerBound = input("Enter a lower bound: ")

    while intValidityChecker(lowerBound) == False:
      lowerBound = input("Enter a VALID lower bound pleet: ")
    
    print(f"OK then, lower bound is: {lowerBound}")
    lowerBound = int(lowerBound)

    upperBound = input("Now, enter an upper bound: ")
    
    while intValidityChecker(upperBound) == False:
      upperBound = input("Enter a VALID upper bound pleet: ")

    upperBound = int(upperBound)

    while upperBound <= lowerBound:
      print("Upper Bound can't be the same or lower than the lower bound!")
      upperBound = input("Enter an upper bound: ")

      while intValidityChecker(upperBound) == False:
        upperBound = input("Enter a VALID upper bound pleet: ")

      upperBound = int(upperBound)

    print(f"OK then you will be guessing, a number between {lowerBound} and {upperBound}!")

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber  = input("Guess a number: ")

        while intValidityChecker(guessedNumber) == False:
          guessedNumber = input("Enter a VALID guess pleet: ")

        guessedNumber = int(guessedNumber)

        print(f"You guessed {guessedNumber},")
        
        if guessedNumber == actualNumber:
            print(f"It was {actualNumber}")
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again : '(")
        else:
            print("Too big, try again : '(")

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!

def intValidityChecker(var):

  try:
    int(var)
  except ValueError:
    print('NOT A VALID INTEGER !!')
    return False
  else:
    return True

if __name__ == "__main__":
    print(advancedGuessingGame())
