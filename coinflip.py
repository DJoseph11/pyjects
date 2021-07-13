import random 
print(" I will flip a coin 1000 times. Guess how many times it will comp up heads. (Press Enter to begin")
input()
flips = 0 # a counter variable to keep track of how many flips has been made
heads = 0 # another counter variable to keep track of how many heads pop from the while loop in the if statement.
while flips < 1000: # if the flip is less then a 1000 cycles when true it recycles if false the program continues to line 20
    if random.randint(0,1) == 1: # two options for 0 = tail 1 = heads 
        heads += 1 # if line 7 is true where random = 1 it will go to line 8 where heads = heads + 1 line 5 get updated 
    flips += 1 # regardless of line 7 is true or false the counter for flips is still added to line 4

    if flips == 900: #once the flip count reach 900 the program will print line 12
        print(" 900 flips and there have been {h} heads.".format(h = heads))

    if flips == 100:
        print(" 100 flips and there have been {h} heads".format(h = heads))

    if flips == 500:
        print(" 500 flips your halfway there and there have been {h} heads".format(h = heads))

print()
print("Out of 1000 tosses, heads came up {h} heads times.".format(h = heads))
print("Where you close?")
