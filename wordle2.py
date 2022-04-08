import random # package is required to select a random word to be guessed by the player
import csv # package is required to import and read a csv file that contains all possible five letter words

## A csv file containing five letter words is imported:
csv_reader = csv.reader(open('/Users/timgust/OneDrive - stud.hs-bremen.de/Pi42/five_letter_words.csv', 'r'))
five_letter_words = list(csv_reader) # the five letter words are stored in a list for further processing
random_word = random.choice(five_letter_words) # from the word list, a random word is selected
word = random_word[0] # in order to be able to use the chosen word, it must be extracted from the random_word list

#word = "aabbb" # static word that can be used for test purposes; requires that the wordtest variable (ln25) and condition (ln29) are reversed
## Some initial variables are defined:
attempt = 0 # will be used to count the attempts of the player
player_input = [] # is necessary to be defined because the while condition is otherwise not met
game_valid = True # is necessary to be defined because the while condition is otherwise not met

## A welcome message is displayed at the start of a new game:
print("------------------------------------\nHi! Let's play wordle! (You can end the game at any point by entering \"eeeee\").")
## A while condition is defined: 
while attempt < 6 and player_input != word and game_valid == True: # As longer as the player has had less than six attempts, has not guessed the word or has not aborted the game, the game can run
    answer = ["⬛","⬛","⬛","⬛","⬛"] # inital answer list 
    player_input = input("Enter a five letter word: ") # player input is requested and stored
    ## Verification checks
    memory_string = [] # important for later
    char_check = [] # necessary to check verify that the player's input only contains letter and no numbers, etc.
    wordtest = False # important for the following check
    ## Checks if the player's input is a word from the word list:
    for thatword in five_letter_words:
        if thatword[0] == player_input:
            wordtest = True # if the input is in the word list, wordtest is set to true
        else:
            continue # if the input is not equal to the current word in the word list, no changes are made and the check continues to the next word in the list
    ## Checks if the player's input does only contain letters and no numbers, etc. (technically unnesescary since we there are no words in the word list that contain numbers, but there's never something like to much verification ;))
    for character in player_input:
        char = character.isalpha() # if the letter is a character, char is set to True
        if char == True:
            char_check += "1" # if char == True, a "1" is added to the char_check list
    ## Abort criteria: the player can exit the game and reveal the solution if they enter "eeeee". 
    if player_input == "eeeee":
        if attempt == 1:
            print("Okay, end of game after " + str(attempt) + " round. The word we were looking for was \"" + word + "\".")
        else: 
            print("Okay, end of game after " + str(attempt) + " rounds. The word we were looking for was \"" + word + "\".")
        game_valid = False
    ## If the player has not aborted the game but any of the verification checks fails, an error message is displayed. 
    elif len(player_input) != 5 or wordtest == False or char_check != ["1","1","1","1","1"]:
        print("Wrong input! Try again!")
    ## If everything is go, the real fun can begin:
    else:
        ## Check if there are any letter from the player's input in the correct position:
        for position in range(len(word)):
            if player_input[position] == word[position]:
                answer[position] = "🟩" # if the player's input for a certain position is correc, a green box replaces the respective black box in the answer list
                memory_string += player_input[position] # the letter is added to the memory (important for the next step)
        ## Check if the any letter from the player's input is in the word but not in the correct position:
        for position in range(len(word)):
            if (player_input[position] in word) and (memory_string.count(player_input[position]) < word.count(player_input[position])) and (answer[position] != "🟩"): # conditions are necessary to ensure that there are no incorrect outputs 
                answer[position] = "🟨" # if all the conditions are met, a yellow box replaces the respective black box in the answer list
                memory_string += player_input[position] # letter is added to the memory to ensure that there are no errors in the answer displayed to the player
        ## The answer is displayed:
        print(answer)
        ## A counter shows how many attempts the player has left:
        if player_input != word and attempt < 6:
            print("You have " + str((5 - attempt)) + " guesses left.")
        attempt = attempt + 1 # after each round, the attempt counter is increased by one
## If the player did not guess the word in 6 attempts, the game ends and the word is displayed to the player:
if attempt == 6 and player_input != word:
    print("Sorry, you didn't guess the word. We were looking for \"" + word + "\".")
## If the player guessed the word on the first attempt, a congratulation message is displayed:
elif player_input == word and attempt == 1:
    print("Yes! You got the word \"" + word + "\" in " + str(attempt) + " guess! Good job!")
## If the player guessed the word in more than attempt, a congratulation message is displayed:
elif player_input == word and attempt > 1 and attempt <= 6:
    print("Yes! You got the word \"" + word + "\" in " + str(attempt) + " guesses! Good job!")
## No else is used because in case of an abort, a wrong message would be displayed.