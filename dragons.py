import random
import time

def display_intro(): #setting a function for the introduction of the game
    print('''You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.''')

    print()  #prints and empty line

def choose_cave():  # This function let the player choose a cave based on the input 

    cave = "" #Sets a variable to contain of the option of the player
    while cave != "1" and cave != "2": # a loop thats saying while the empty variable "cave" is not = 1 or 2
        print("Which cave will you go into? (1 or 2)") # This is going to print the line of question.
        cave = input() #This line of code is going to get the option of 1 or 2 
    return cave #This line fo code would return the cave with its value of either 1 or 2

def check_cave(chosen_cave): # A new function with a parameter
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(2)

    friendly_cave = random.randint(1,2) #This would make any random option of 1 and 2 to set to a friendly cave

    if chosen_cave == str(friendly_cave): # A condition thats going to make the random number for friendly_cave into a string
        print("Gives you one of his treasures")
    else: # if the chosen_cave does not match this line of code runs
        print("Gobbles you down in one bite!!")

play_again = "yes" #This is the first line that runs from the program because its the only global variable thats assign "yes"
while play_again == "yes" or play_again == "y": #setting the condition of the player type yes or y 
    display_intro() # On line 4 of the code thats being called to display the intro to the player
    cave_number = choose_cave() # The function on line 12 catch the input string saved it to the variable called cave_number
    check_cave(cave_number) #The function on line 20 cave_number take the output of choose_cave which was a string

    print("Do you want to play again? (yes or no)")
    play_again = input()