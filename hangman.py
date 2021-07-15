# A hangman game
import random



































words = "switch psychedelic soak zip woebegone thundering torpid well off dime carriage grouchy need rule robin vase frightening unit coherent weiting credit tested intelligent cry group faint auspicious modern glue silky sordid scratch cat ground purring seal holiday thoughtful rub yawn wicked hungry science digestion history ".split()  # 45 words in total
 # words is going to turn into a list with the split function -- [a, b, c, d, e, f]

print(len(words)) # 45

def get_random_word(word_list): # def example(any_name):

    word_index = random.randint(0, len(words) - 1) # word_index stored the index number from the variable "words" list provided by random.randint(0,(45) - 1)
    # the second parameter get the length of words from the split since indexes start at 0  so it would be the length of len(word) minus 1 since the second parameter is inclusive to cycle through all the list of words.

    print(word_index) # prints the random number stored in the word_index variable.
    print(word_list[5])  # prints out the word "thundering" at index 5 from the words variable list on line 38 

    return word_list[word_index] # returns get_random_word(list[index])
# print(get_random_word(words))

def display_board(missed_letters, correct_letters,secret_word):
    # display_board function takes in three parameters: missed_letters, correct_letters, secret_word

    print(HANGMAN_PICS[len(missed_letters)])
    # prints out the hangman pic from the global variables HANGMAN_PICS list.
    print()

    print("Missed letters:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")

    print()

    blanks = "_" * len(secret_word)
    # blanks = "_" * len(thundering) would result in 10 underscores __________ 

    for i in range(len(secret_word)):
        # exp len(thundering) = 10 ---> for i in range(10):
        if secret_word[i] in correct_letters:
            # if the letter at index i from the word is within the correct letters list
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1]
            # blanks get updated to

    for letter in blanks:
        print(letter, end=" ")

    print()


def get_guess(already_guessed):
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.toLower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. choose again.")
        elif guess not in "abcdefghijklmnopqrstwxyz":
            print("Please enter a LETTE")
