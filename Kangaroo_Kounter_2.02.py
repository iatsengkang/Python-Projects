#-----------------------------------------------------------------------------
# Name:        Kangaroo Kounter 2.0
# Purpose:     a fun game about counting kangaroos
# Author:      Iat Seng Kang
# Created:     14-Nov-2024
# Updated:     20-Dec-2024
#----------------------------------------------------------------------

#imports modules used in code
import random
import time
import os

def pause(sleep_time, clear = True):
    '''Pauses the code for a certain amount of time and clears the console if needed

    Parameters
    ----------
    sleep_time: int or float
        amount of seconds the program should pause for

    Returns
    -------
    None
                
    '''
    
    #pauses the code for variable "sleep_time" seconds
    time.sleep(sleep_time)
    
    #clears the console if variable "clear" is True
    if clear == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    #returns None
    return None

def check_validity(occurrence, user_input, score = None, trial = None):
    '''Checks the validity for different instances of inputs

    Parameters
    ----------
    occurrence: str
        whether we are checking the validity of "hint" or "guess"
        
    user_input: int
        which number is being checked
    
    score: int
        the current score of the game
        
    trial: list
        a list that contains run number, round number, list of all the number of joeys, user's guess and correct amount

    Returns
    -------
    int
        the user's input
                
    Raises
    ------
    TypeError
        If user_input is not an int
    ValueError
        Varies depending on the occurrence
    Exception
        If something goes awry
    '''
    
    #raises an error if the input was not an int
    if not isinstance(user_input, (int)):
        raise TypeError("input expected to be an int")
    
    #raises an error if input is smaller than 0 if the variable "occurrence" is set to "guess"
    if occurrence == "guess" and user_input < 0:
        raise ValueError("input expected to be a whole number")

    #raises an error if input is smaller or equal to 0 or if its larger than the the amount of waves that exist if the variable "occurrence" is set to "hint"
    elif occurrence == "hint" and (user_input <= 0 or user_input > score + 3):
        raise ValueError("input expected to be an existing round")
    
    #raises an error if input is smaller or equal to 0 or if its larger the amount of attempts made if the variable "occurrence" is set to "last_attempt"
    elif occurrence == "last_attempt" and (user_input <= 0 or user_input > len(trial)/5):
        raise ValueError("input expected to be an existing attempt")
        
    return(user_input)


#defines variables
high_score = {}
trial = []
run = 1
answer = "1"

#introduction, prints the rules of the game if "rules" is inputted then clears the system and begins the game
print("Welcome to The Kangaroo Kounter!")
rules = input('Please type "rules" to read the rules. Type anything else to start the game.\n')
if rules.lower() == "rules":
    print("The Kangaroo Kounter is pretty simple, it's about a game where you have to count the amount of kangaroos there are.")
    print("As you begin the game, the game will tell you how many baby kangaroos jumped into the mama's pouch.")
    print("After 5 seconds, you will need to tell me how many kangaroos there are. Don't forget to include the mama kangaroo!")
    print("If you guess the incorrect number, you will lose a life!")
    print("Don't worry too much though, you will start the game with 2 lives.")
    print("If you guess the correct number, you will earn a point and move onto the next round!")
    print("However, there will be one more wave of kangaroos to count this time.")
    print("I'm also feeling pretty generous, so each round you will be able to use a hint.")
    print('To use a hint, type "hint" when it asks you for the amount of kangaroos.')
    print("Then, input a number, and I'll tell you how many baby kangaroos had jumped in the pouch during that specific wave.")
    print("That's it! It's time to begin the game.")
    input("Press enter to start the game.\n")


#while loop to initiate the game as long as user wants to keep playing ("1" is inputted at the end)
while answer == "1":

    #defines more variables that are reset each game
    lives = 2
    score = 0
    hint = False

    #runs game while you still have lives left
    while lives != 0:

        #defines more variables that are reset each round
        kangaroo_num = [1]
        total_kangaroos = 0

        #clears the console and prints what round it is, then pauses for 1.5 seconds
        pause(0)
        print(f"ROUND {score + 1}")
        time.sleep(1.5)

        #prints and stores your current "score" + 3 random random numbers then finds and stores the sum of all those numbers
        for i in range (score + 3):
            num = random.randint(1,9)
            if num == 1:
                print(f"{num} joey jumps into the mama's pouch")
            else:
                print(f"{num} joeys jump into the mama's pouch")
            kangaroo_num.append(num)
        for i in kangaroo_num:
            total_kangaroos += i

        #waits for 5 seconds for the user to memorize the numbers then clears the console so the user can't cheat
        pause(5)

        #sets variables that keep the next portion of code running until a valid input is inputted by the user
        guess_validity = False
        hint_validity = False
        
        #asks for user's guess
        while guess_validity == False:
            guess = input("How many kangaroos are there?\n")
            
            #asks user for which wave they would like to know about if hint is inputted
            if guess.lower() == "hint" and hint == False:
                while hint_validity == False:
                    wave_num = input("Which wave would you like to know about?\n")
                    
                    #checks validity of the "hint" input, returns error message if the input was invalid and tries again
                    try:
                        check_validity("hint", int(wave_num), score)
                        print(f"During wave {wave_num}, {kangaroo_num[int(wave_num)]} joeys had jumped into the pouch")
                        hint_validity = True
                        hint = True
                        guess = input("how many kangaroos are there?\n")
                    except (ValueError, TypeError) as e:
                        if "invalid literal for int() with base 10" in str(e):
                            print("Input Error: input expected to be a whole number, please try again")
                        else:
                            print(f"Input Error: {e}, please try again")
                        continue
                    except Exception as e:
                        print(f"Unexpected Error: {e}")
                        break
                    
                    #waits for 1 second and clears the console regardless of the input
                    finally:
                        pause(1)
            
            #asks for a new input if "hint" is inputted and has been already been used up
            while guess.lower() == "hint" and hint == True:
                print("You have already used your hint")
                pause(1)
                guess = input("how many kangaroos are there?\n")
                
            #checks validity of the "guess" input, returns error messages if the input was invalid and tries again
            try:
                guess = check_validity("guess", int(guess), score)
                guess_validity = True
            except (ValueError, TypeError): 
                print(f"Input Error: input expected to be a whole number, please try again")
                continue
            except Exception as e:
                print(f"Unexpected Error: {e}")
                break
            
            #waits for 1 second and clears the console regardless of the input
            finally:
                pause(1)

        #adds 1 to the score of the user if user's input is correct then loops previous code
        if int(guess) == total_kangaroos:
            print("Correct! There were a total of " + str(total_kangaroos) + " kangaroos!")
            score += 1

        #subtracts 1 from remaining lives if user's input is incorrect then tells user how many lives they have remaining
        else:
            lives -= 1
            print("Aw man! There were actually a total of " + str(total_kangaroos) + " kangaroos")
            print("You now have " + str(lives) + " lives left")

        #waits 1.5 seconds and then clears the console
        pause(1.5)

    #adds your run number and score to a dictionary
    kangaroo_num.pop(0)
    high_score.setdefault(run, score)

    #adds run number, round number, list of all the number of joeys, user's guess and correct amount to a list 
    trial.append(str(run))
    trial.append(score + 1)
    trial.append(kangaroo_num)
    trial.append(guess)
    trial.append(total_kangaroos)

    #adds one to the amount of games played
    run += 1


    #prints the end screen and score when amount of lives run out, and asks user whether they want to play again, see their previous scores, see their high score or see the last round of a certain game they played
    print("GAME OVER")
    print("Score: " + str(score))
    answer = input("Type 1 if you would like to play again and try to beat your old score!\nType 2 if you want to see that last round of any previous game played\nType 3 if you want to see all your previous scores\nType 4 to see your current high score\nType anything else to exit the game\n")

    #asks for input based on what the user wants to do next, exits code if "1", "2", "3", or "4" are not inputted.
    while answer == "2" or answer == "3" or answer == "4":
        pause(0)

        #if "3" is inputted, prints all previous attempt scores and asks for new input
        if answer == "3":
            for key, value in high_score.items():
                print(f"Attempt {key} score: {value}\n")
            print("-" * 100)
            answer = input("Type 1 if you would like to play again and try to beat your old score!\nType 2 if you want to see that last round of any previous game played\nType 3 if you want to see all your previous scores\nType 4 to see your current high score\nType anything else to exit the game\n")

        #if "4" is inputted, prints the high score and asks for new input
        elif answer == "4":
            highest = 0
            for key, value in high_score.items():
                if value > highest:
                    highest = value
            print(f"Current high score: {highest}")
            print("Play again to try to beat your high score!")
            print("-" * 100)
            answer = input("Type 1 if you would like to play again and try to beat your old score!\nType 2 if you want to see that last round of any previous game played\nType 3 if you want to see all your previous scores\nType 4 to see your current high score\nType anything else to exit the game\n")

        #if "2" is inputted, asks user which attempt they would like to know about regarding the last round of that attempt and asks for new input
        else:
            last_check = False
            
            #continuously asks for a new input if the previous input was invalid
            while last_check == False:
                last = input("for which attempt would you like to see the last round you played?\n")

                #checks for validity
                try:
                    check_validity("last_attempt", int(last), None, trial)
                    last_check = True
                    
                    #prints the attempt and round number
                    for i in range(len(trial)):
                        if trial[i] == last:
                            list_num = int(i)
                    print(f"ATTEMPT {last}, ROUND {trial[list_num + 1]}\n")
                    
                    #prints all the joeys that existed in that particular attempt's last round
                    for i in trial[list_num + 2]:
                        if i == 1:
                            print(f"{i} joey jumps into the mama's pouch")
                        else:
                            print(f"{i} joeys jump into the mama's pouch")
                    
                    #prints the user's guess and correct amount then asks for a new input
                    print(f"\nYour Guess: {trial[list_num + 3]}")
                    print(f"Correct Amount: {trial[list_num + 4]}")
                    print(f"Score: {trial[list_num + 1] - 1}")
                    print("-" * 100)
                    answer = input("Type 1 if you would like to play again and try to beat your old score!\nType 2 if you want to see that last round of any previous game played\nType 3 if you want to see all your previous scores\nType 4 to see your current high score\nType anything else to exit the game\n")
                
                #prints an error message corresponding to the type of invalid input
                except (ValueError, TypeError) as e:
                    if "invalid literal for int() with base 10" in str(e):
                        print("Input Error: input expected to be a whole number, please try again")
                    else:
                        print(f"Input Error: {e}, please try again")
                    continue
                except Exception as e:
                    print(f"Unexpected Error: {e}")
                    break
                