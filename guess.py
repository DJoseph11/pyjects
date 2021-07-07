#This is a Guess the number game program.
import random

guesseTaken = 0 # This line of code sets a counter for the amount of guesses

print("Hello! What is your name?")
name = input() # Takes the name of the player

number = random.randint(1, 100) # This line of code generate a number that is assigned to the number variable name
print("Well, " + name + ", I am thinking of a number between 1 and 100.")


for guesseTaken in range(6): # This line of code use a for loop to start guesseTaken at 0 up to 6 guesses
    print("Take a guess.")
    guess = input()  #Input is always entered as a string
    guess = int(guess) 

# The conditions below consist of the main core of the game.
    if guess < number: 
        print("Your guess is to low.")

    if guess > number:
        print("Your guess is too high.")
    
    if guess == number:
        break 

if guess == number:
    guesseTaken = str(guesseTaken + 1)
    print("Good job, " + name + "! You guessed my number in " + guesseTaken + " guesses!")

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number + ".")


