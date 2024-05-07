
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(user_guess, answer, turns):
    if user_guess > answer:
        print("Too high")
        return turns - 1
    elif user_guess < answer:
        print("Too low")
        return turns - 1
    elif user_guess == answer:
        print(f"You win! the answer is {answer}")




def game_level():
    level = input("Choose a level, Type 'easy' or 'hard': ")
    if level == "easy":
       return EASY_LEVEL
    else:
        return HARD_LEVEL
    

def game_on()  :
    answer = randint(1, 100)
    print("You need to guess a number between 1 and 100")
    turns = game_level()

    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} left")
        user_guess = int(input("Make a guess: "))
        turns = check_answer(user_guess, answer, turns)
        if turns == 0 :
            print("You have no more guesses left. You lost.")
            print(f"the answer is {answer}")
            return
        elif user_guess != answer:
            print("Guess again...")


game_on()
