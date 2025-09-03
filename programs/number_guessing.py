"""Module for number guessing"""
import random
def get_random_number() -> int:
    """Function to get a random number"""
    print(" I'm Thinking of number between 1 to 100.")
    number = random.choice(range(1, 101))
    return number

def make_a_choice(difficulty_level: int, number: int):
    """Function to make a choice and check the guess"""
    for i in range(difficulty_level, 0, -1):
        print(f"You have {i} attempts remaining to gues the number")
        guessed_number = int(input("Make a gues"))
        if guessed_number == number:
            print("You made a correct choice")
            break
        else:
            if guessed_number > number:
                print("Hint: To high")
            else:
                print("Hint: To low")
        print("Guess again")
    else:
        print("You've run out of guesses, you lose.")

def guess_a_number():
    """Function to guess a number"""
    print("Welcome to the number guessing game.")
    random_number = get_random_number()
    chosen_difficulty_level = input("Chose a difficulty level, Type 'e' for Easy or 'h' hard ")
    difficulty_level = None
    if chosen_difficulty_level == 'e':
        difficulty_level = 10
    elif chosen_difficulty_level == 'h':
        difficulty_level = 5
    else:
        print("Chosen wrong choice!")
    make_a_choice(difficulty_level, random_number)

guess_a_number()




