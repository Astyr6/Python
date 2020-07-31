from getpass import getpass
import os
clear = lambda: os.system('cls')
clear()
while True:
    print("==================================================")
    print("Rock, paper, scissors !")
    print("==================================================")    
    print("")
    print("New game ?")
    ng = input("(Y)es / (N)o > ")

# GAME BLOCK

    if ng == "Y" or ng == "y":

        ng = None
        clear()
        print("==================================================")
        print("Rock, paper, scissors !")
        print("==================================================")   
        print("")
        print("R for rock, P for paper, S for scissors, press Enter to confirm your input")
        print("")
        p1 = getpass("Player 1 Turn > ")
        print("")
        p2 = getpass("Player 2 Turn > ")
        print("")


        if p1 == "r" or p1 == "R":
            if p2 == "r" or p2 == "R":
                print("------------------------------------------")
                print("Rock against rock, no one won.")
            elif p2 == "p" or p2 == "P":
                print("------------------------------------------")
                print("Paper wins against rock, Player 2 won !")
            elif p2 == "s" or p2 == "S":
                print("------------------------------------------")
                print("Rock wins against scissors, Player 1 won !")

        elif p1 == "p" or p1 == "P":
            if p2 == "r" or p2 == "R":
                print("------------------------------------------")
                print("Paper wins against rock, Player 1 won !")
            elif p2 == "p" or p2 == "P":
                print("------------------------------------------")
                print("Paper against paper, no one won.")
            elif p2 == "s" or p2 == "S":
                print("------------------------------------------")
                print("Scissors win against paper, Player 2 won !")

        elif p1 == "s" or p1 == "S":
            if p2 == "r" or p2 == "R":
                print("------------------------------------------")
                print("Rock wins against scissors, Player 2 won !")
            elif p2 == "p" or p2 == "P":
                print("------------------------------------------")
                print("Scissors win against paper, Player 1 won !")
            elif p2 == "s" or p2 == "S":
                print("------------------------------------------")
                print("Scissors against scissors, no one won.")

        else:
            print("Oops, you have have entered an invalid option, press Enter to continue...")
            getpass("")
            clear()
            continue


        print("------------------------------------------")
        print("")
        getpass("Press Enter to continue...")
        clear()

# EXIT BLOCK

    elif ng == "N" or ng == "n":
        ng = None
        break