'''There three of type of errors
1. Syntax errors
2.Runtime errors
3.Semantic errors'''

import random

number1 = random.randint(1,10)
number2 = random.randint(1,10)
print("What is {a} + {b}?".format(a = number1, b = number2))
# A bug has showed below base on the variable did not contain an int since input is always in a string
answer = int(input())
if answer == number1 + number2:
    # Both number1 and number2 are both intergers therefore answer has to be an interger as well
    print("CORRECT!")
else:
    # a bug had showed in the terminal where the output of the print for the answer variable if printed within
    print("NOPE, {a} + {b} is {c}".format(a =number1, b = number2, c=number1 + number2))
