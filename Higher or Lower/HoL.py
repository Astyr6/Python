from getpass import getpass
import random
import os
clear = lambda: os.system('cls')
clear()

# ENDLESS LOOP

while True:
    print("==================================================")
    print("Higher or Lower ?")
    print("==================================================")
    print("")
    print("New game ?")
    ng = input("(Y)es / (N)o > ")

# GAME BLOCK

    if ng == "Y" or ng == "y":

        ng = None
        clear()
        print("==================================================")
        print("Higher or Lower ?")
        print("==================================================")   
        print("")
        print("Difficulty Level :")
        print("(1) Baby")
        print("(2) Easy")
        print("(3) Medium")
        print("(4) Hard")
        print("(5) Demon")
        print("(6) Is this even possible ?")
        lvl = input("> ")

        tries = 1
        num = 0

        clear()
        print("==================================================")
        print("Higher or Lower ?")
        print("==================================================")

        if lvl == "1": num = random.randint(1, 11); print("Between 1 and 10")

        elif lvl == "2": num = random.randint(1, 21); print("Between 1 and 20")

        elif lvl == "3": num = random.randint(1, 51); print("Between 1 and 50")

        elif lvl == "4": num = random.randint(1, 101); print("Between 1 and 100")

        elif lvl == "5": num = random.randint(1, 1001); print("Between 1 and 1000")

        elif lvl == "6": num = random.randint(1, 1000000001); print("Between 1 and 1000000000")

        elif lvl == "opgp": num = random.randint(1, 1000000000001); print("ULTRA HARDCORE DIFFICULTY, RANGE 1 TO 1 TRILLION")

        else: clear(); continue

        print("")
        
        while True:
            try:
                ipt = int(input("Type your guess > "))
                if ipt == num:
                    break
                else:
                    tries += 1
                    clear()
                    print("==================================================")
                    print("Higher or Lower ?")
                    print("==================================================")
                    print("")
                    if ipt < num:
                        print("Higher !")
                    elif ipt > num:
                        print("Lower !")
            except ValueError:
                pass
                
                

        print("")
        print("--------------------------------------------------")
        print("You guessed the number " + str(num) + " in " + str(tries) + " try/ies !")
        print("--------------------------------------------------")
        print("")
        getpass("Press Enter to continue...")
        clear()

# EXIT BLOCK

    elif ng == "N" or ng == "n":
        ng = None
        break

    else:
        clear()