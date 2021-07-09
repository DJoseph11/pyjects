def bacon():
    spam = 99 # a local variable inside the function bacon()
    print(spam) # This would print 99 from the local variable

spam = 42 # This variable is outside the bacon() function therefore its a global variable

print(spam) # This would print 42 
bacon() # calls the function bacon() which would print 99 within its local scope tha was assign to its spam variable.

print(spam) # This would print 42 again because global spam variable is assigned 42 from line 5 of the code above.