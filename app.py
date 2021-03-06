#  Create a number guessing game where you get three chances to guess a rand number generated by the computer.
# Lets you know if you are hot or cold
# The number doesn't change until you guess it or until you run out of guesses.
# Intro enter name
# gen a number
# track gueses

# intro has 3 functions
# intro explains the game
# ready to play gives player 3 chances to answer the question, if not answered properly ends game.
# play_game starts the game.
import random


def ready_or_not():
    chances = 3
    while(chances > 0):
        print("Are you ready to play?")
        print("Enter y for Yes and n for No")
        answer = input()
        if(answer != 'y' and answer != 'n'):
            chances -= 1
        elif(answer == 'n'):
            print("please return")
            return answer
        else:
            return answer


def play_game():
    guess_number = random.randint(0, 9)
    guesses = 3
    print(
        f"Guess the number. Its single digits no decimals between 1 - 9. You only get {guesses} chances")
    while(guesses > 0):
        guess = input()
        if(guess_number == int(guess)):
            print("Hey you got it right!!!")
            break
        elif(guess != guess_number and guesses == 1):
            print("Sorry, you Lose")
            print(f"The answer was {guess_number}")
            guesses -= 1
        else:
            guesses -= 1
            print("Try again")


def intro():
    print("Welcome to Number Guesser, where we generate random numbers and You get to guess")
    answer = ready_or_not()
    if(answer == 'y'):
        play_game()


intro()
