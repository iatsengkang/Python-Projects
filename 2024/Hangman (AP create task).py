#----------------------------------------------------------------------
# Name:        HangNoMan
# Purpose:     A way to play Hangman with common boy and girl names, with lives instead of a hang man
#
# Created:     11-Apr-2024
# Updated:     24-Apr-2024
#----------------------------------------------------------------------
import random


def checkGuess(guess, answer, display_list, guessed_letters):
    # CODES
    # -1: INVALID GUESS
    #  0: INCORRECT GUESS
    #  1: LETTER EXISTS
    #  2: CORRECT/COMPLETE ANSWER

    result = {"code": -1, "message": "", "display_list": display_list}

    # Check if the guess is not a letter or if the user inputted nothing
    if not guess.isalpha() or len(guess) == 0:
        result["code"] = -1
        result["message"] = "You must guess a letter or a word!"
        result["display_list"] = None
        return result

    # Check if the user is guessing the word
    if len(guess) != 1:
        result["code"] = 2 if guess == answer else 0
        result["message"] = str(guess == answer)
        result["display_list"] = None
        return result

    # Check if the letter was already guessed
    if guess in guessed_letters:
        result["code"] = -1
        result["message"] = "You already guessed this letter!"
        result["display_list"] = None
        return result

    # Loop through the answer to check if the letter matches anything
    result["code"] = 0
    guessed_letters.append(guess)
    for i in range(len(answer)):
        if guess == answer[i]:
            display_list[i] = guess
            result["code"] = 1

    result["display_list"] = display_list

    # If there are no unsolved letters left
    if display_list.count("_") == 0:
        result["code"] = 2

    return result


# Get a random correct answer from the name list
word_list = [
    'james', 'robert', 'john', 'michael', 'david', 'william', 'richard',
    'joseph', 'thomas', 'christopher', 'charles', 'daniel', 'matthew',
    'anthony', 'mark', 'donald', 'steven', 'andrew', 'paul', 'joshua',
    'kenneth', 'kevin', 'brian', 'george', 'timothy', 'ronald', 'jason',
    'edward', 'jeffrey', 'ryan', 'jacob', 'gary', 'nicholas', 'eric',
    'jonathan', 'stephen', 'larry', 'justin', 'scott', 'brandon', 'benjamin',
    'samuel', 'gregory', 'alexander', 'patrick', 'frank', 'raymond', 'jack',
    'dennis', 'jerry', 'mary', 'patricia', 'jennifer', 'linda', 'elizabeth',
    'barbara', 'susan', 'jessica', 'sarah', 'karen', 'lisa', 'nancy', 'betty',
    'sandra', 'margaret', 'ashley', 'kimberly', 'emily', 'donna', 'michelle',
    'carol', 'amanda', 'melissa', 'deborah', 'stephanie', 'dorothy', 'rebecca',
    'sharon', 'laura', 'cynthia', 'amy', 'kathleen', 'angela', 'shirley',
    'brenda', 'emma', 'anna', 'pamela', 'nicole', 'samantha', 'katherine',
    'christine', 'helen', 'debra', 'rachel', 'carolyn', 'janet', 'maria',
    'catherine', 'heather'
]
answer = random.choice(word_list)

# Create a list of some number of underscores equal to the length of the answer
display_list = ["_"] * len(answer)

# Start game
user_guess = ""
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 5
code = 0
print(" ".join(display_list))
print("You have " + (max_incorrect_guesses - incorrect_guesses) * "❤️" +
      " incorrect guesses left")

while code != 2 and incorrect_guesses != max_incorrect_guesses:
    user_guess = input("Guess a letter or a word: ").lower()
    result = checkGuess(user_guess, answer, display_list, guessed_letters)
    code = result["code"]
    # Checks for validity
    while code == -1:
        print(result["message"])
        print("Please fix this in your next guess!")
        user_guess = input("Guess a letter or a word: ").lower()
        result = checkGuess(user_guess, answer, display_list, guessed_letters)
        code = result["code"]

    # Prints display_list, letters and amount of guesses left
    if result["display_list"] != None:
        display_list = result["display_list"]
    if code == 0:
        incorrect_guesses += 1
    print(" ".join(display_list))
    if incorrect_guesses != 5:
        print("You have " +
              (max_incorrect_guesses - incorrect_guesses) * "❤️" +
              " incorrect guesses left.")
    else:
        print("You have no guesses left.")

# Game over statement
print("GAME OVER!!!!")
if incorrect_guesses == 5:
    print("YOU LOOOOOOOSEEEEEE!!!!")
    print(f"The answer was: {answer}.")
else:
    print(
        "YOU WIN!!!!!!!!!!! WOOOOOOOOOOOOOOOOOOOOOOHHHHHHHHHHHHHHHHHHHHHHHHHHOOOOOOOOOOOOOOOO!!!!"
    )
