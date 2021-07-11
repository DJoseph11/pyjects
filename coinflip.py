import random 
print(" I will flip a coin 1000 times. Guess how many times it will comp up heads. (Press Enter to begin")
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0,1) == 1:
        heads += 1
    flips = flips + 1

    if flips == 900:
        print(" 900 flips and there have been {h} heads.".format(h = heads))

    if flips == 100:
        print(" 100 flips and there have been {h} heads".format(h = heads))

    if flips == 500:
        print(" 500 flips your halfway there and there have been {h} heads".format(h = heads))

print()
print("Out of 1000 tosses, heads came up {h} heads times.".format(h = heads))
print("Where you close?")
