from random import randint as rdt
import sys

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")
number = rdt(1, 99)
value = input("What's your guess between 1 and 99?\n")
if (value == "exit"):
        print("Goodbye!")
        sys.exit()
if (int(value) == number):
    print("Congratulations! You got it on your first try!")
    sys.exit()
loop = 1
while(1):
    if (value == "exit"):
        print("Goodbye!")
        sys.exit()
    elif (int(value) > number):
        print("Too high!")
    elif (int(value) < number):
        print("Too low!")
    elif (int(value) == number):
        print("Congratulations, you've got it!")
        if (int(value) == 42):
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        print("You won in " + str(loop) + " attempts!")
        sys.exit()
    value = input("What's your guess between 1 and 99?\n")
    loop += 1