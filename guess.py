#This is a Guess the number game program.
import random

guesseTaken = 0

print("Hello! What is your name?")
name = input()

number = random.randint(1, 100)
print("Well, " + name + ", I am thinking of a number between 1 and 100.")


for guesseTaken in range(6):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

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


# for i in range(3):
#     print("hello! i is set to",i)