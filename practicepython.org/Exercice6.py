inp = input("Give me a random word\n")

if inp.lower() == inp[::-1].lower(): 
    print("{} is a palindrome!".format(inp))
    
else: 
    print("{} is not a palindrome!".format(inp))