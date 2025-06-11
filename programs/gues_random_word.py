import random

words = ["ball", "bat", "wicket"]
choice = random.choice(words)
print(f"Random choice is {choice}")
blank_word = "_" * len(choice)
choice_replace = choice
for i in range(len(choice)*2):
    if blank_word == choice:
        print("You won")
        break
    guess = input("Guess the latter:")
    print(f"guessed word is{guess}")
    if guess in choice_replace:
        letter_index = choice_replace.index(guess)
        print(letter_index)
        blank_word = blank_word[:letter_index] + guess + blank_word[letter_index+1:]
        choice_replace = choice_replace[:letter_index] + "*" + choice_replace[letter_index+1:]
        print(choice_replace)
    else:
        print("You guessed a wrong letter")
    print(blank_word)
else:
    print("you loss")
