# A hangman game
import random

# The variable below is in caps to define it is a variable that is constant theres no rules for that.
# Multi line strings put in the list variable HANGMAN_PICSn 
HANGMAN_PICS = [''' 
    +---+
        |
        |
        |
      =====''', ''' 
     +---+
     O  |
        |
        |
      =====''', '''
     +---+
     O  |
     |  |
        |
      =====''', '''
      +---+
     O  |
    /|  |
        |
      =====''', '''
      +---+
     O  |
    /|\ |
        |
      =====''', '''
      +---+
     O  |
    /|\ |
    /   |
      =====''', '''
        +---+
     O  |
    /|\ |
    / \ |
      =====''']




words = "switch psychedelic soak zip woebegone thundering torpid well off dime carriage grouchy need rule robin vase frightening unit coherent weiting credit tested intelligent cry group faint auspicious modern glue silky sordid scratch cat ground purring seal holiday thoughtful rub yawn wicked hungry science digestion history ".split()  # 45 words in total
# words is going to turn into a list with the split function -- [a, b, c, d, e, f]

print(len(words))  # 45


def get_random_word(word_list):  # def example(any_name):

    # word_index stored the index number from the variable "words" list provided by random.randint(0,(45) - 1)
    # word_index = random.randint(0, len(words) - 1)  
    
    word_index = random.choice(words)
    # the second parameter get the length of words from the split since indexes start at 0  so it would be the length of len(word) minus 1 since the second parameter is inclusive to cycle through all the list of words.

    # prints the random number stored in the word_index variable.
    # print(word_index)
    # prints out the word "thundering" at index 5 from the words variable list on line 38
    # print(word_list[5]) # The variable words on line 46 list passed to get random word function   

    return word_list[word_index]  # returns  the "word_list" parameter passing the global "words" variable on line 123
# print(get_random_word(words))


def display_board(missed_letters, correct_letters, secret_word):
    # display_board function takes in three parameters: missed_letters, correct_letters, secret_word

    print(HANGMAN_PICS[len(missed_letters)])
    # prints out the hangman pic from the global variables HANGMAN_PICS list starting at index 0 from the global variables HANGMAN_PICs.
    print()

    print("Missed letters:", end=" ")
    for letter in missed_letters: # This loop is going to iterate through and print the missed letter in the global variable missed_letters on line 121 

        print(letter, end=" ") # printing the missed letters with a character spacing in between them using  end=" ". exp. f r g h h h

    print() # prints empty space for seperation

    blanks = "_" * len(secret_word)
    # blanks = "_" * len(thundering) would result in 10 underscores __________

    for i in range(len(secret_word)):
        # exp len(thundering) = 10 ---> for i in range(10):
        if secret_word[i] in correct_letters:
            # if the letter at index i from the word is within the correct letters list
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
            # blank = blanks[:i = : 10 ="thundering"] + secret_word[i iterate the fist index of the string "thundering"] + blanks[i + 1] moves to the next index of thundering 
            # blanks get updated to

    for letter in blanks: # Word "Thundering" 
        print(letter, end=" ") # T_________

    print()


def get_guess(already_guessed):
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1: # if  its "true" the player input is not equal to a single character it will print on line 106
            print("Please enter a single letter.")
        elif guess in already_guessed: #That single character from the player input will pass and check if the letter is in the parameter this being passed on line 130 which is the combine of line 121 + line 122
            print("You have already guessed that letter. choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz": # if that single character is not in the string of characters it will print
            print("Please enter a LETTER.")
        else:
            return guess


def play_again():
    print("Do you want to play again? (yes or no")
    return input().lower().startswith("y")


print("H A N G M A N") # The program start running 
missed_letters = " "
correct_letters = " "
secret_word = get_random_word(words)
game_is_done = False



while True:
    display_board(missed_letters, correct_letters, secret_word) # call the function on line 69 and assign line 121 to line 123
    guess = get_guess(missed_letters + correct_letters) # on line 100 takes in the user input of one character

    if guess in secret_word: # if the return of the single character from line 100 is in the secret word
        correct_letters = correct_letters + guess # The guess is true the guess character is in the secret_word it will start with empty string on line 122 which would concatenate with the local guess variable that contained that single character


        found_all_letters = True

        for i in range(len(secret_word)): # loops through the length of the secret_word
            if secret_word[i] not in correct_letters: # if in the word "thundering" which is 10 characters, it will loop through the word's length and check each of the index checking line 133 
                found_all_letters = False  
                break # the program will break out of the for loop code block and move to line 148

        if found_all_letters: # if every single character in the word "thundering" is in the list that stored on line 133,
            print("Yes! The secret word is {s}! You have won!".format(s = secret_word)) # message for winning the game.

            game_is_done = True # since all the letters is in the list the game is done 

    else:
        missed_letters = missed_letters + guess   # same thing on line 132 taking line 121 and concact to line 130 in the local scope

        if len(missed_letters) == len(HANGMAN_PICS) - 1: # if missed letters on line 149 has an index length of the HANGMAN_PICS which is 6 because theres no index 7  the it will print out updated data whi
            display_board(missed_letters, correct_letters, secret_word)

            print("You have run out of guesses!\nAfter {m} missed guesses and {c} correct guess, the word was {s}.".format(
                m =len(missed_letters), c =len(correct_letters), s =secret_word))

            game_is_done = True # all the above would be true which the game is done if not the code will run again on line 127 because the of the while loop is still true 


    if game_is_done: # if line 157 is true 
        if play_again(): # if line 115 is true and the player input "Yes" 
            missed_letters = " "
            correct_letters = " "
            game_is_done = False 
            secret_word = get_random_word(words)
        else:
            break

        