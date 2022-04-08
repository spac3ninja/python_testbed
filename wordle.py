#from multiprocessing.connection import answer_challenge
import random
import csv 

csv_reader = csv.reader(open('/Users/timgust/OneDrive - stud.hs-bremen.de/Pi42/five_letter_words.csv', 'r'))
five_letter_words = list(csv_reader)
random_word = random.choice(five_letter_words)
word = random_word[0]

attempt = 0
player_input = []
# test test
while attempt < 6 and player_input != word:
    answer = []
    memory_string = []
    wordtest = False
    player_input = input("Enter a five letter word: ")
    for thatword in five_letter_words:
        if thatword[0] == player_input:
            wordtest = True
        else:
            continue
    if len(player_input) != 5 or wordtest == False:
        print("Wrong input! Try again!")
    else:
        current_position = 0
        for letter in player_input:
            if letter == word[current_position]:
                answer += "🟩"
                memory_string += letter
            elif letter in word:                  
                if letter != letter in memory_string: 
                    answer += "🟨"
                    memory_string += letter  
                elif memory_string.count(letter) < word.count(letter):  
                    answer += "🟨"
                    memory_string += letter  
                else:
                    answer += "⬛"          
            else:
                answer += "⬛"
            current_position += 1
        print(answer)
        if player_input != word:
            print("You have " + str((5 - attempt)) + " guesses left.")
        attempt = attempt + 1
if attempt == 6 and answer != word:
    print("Sorry, you didn't guess the word. We were looking for \"" + word + "\".")
else:
    print("Yes! You got the word \"" + word + "\" in " + str(attempt) + " guesses! Good job!")
