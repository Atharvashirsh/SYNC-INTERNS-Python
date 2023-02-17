import random
import time

choices = ["rock", "paper", "scissors"]
running = True

print()
print("*"*100)
print("\nWelcome to Rock, Paper and Scissors\n")
print("*"*100)
print()

time.sleep(2)

user = input("\nEnter Your Name : ")

print("\nHello {}".format(user))
print("\nLet's play")
print("\nYour choices are rock, paper and scissors\n")

while running:

    print("*"*100)
    userchoice = input("\nEnter Your choice (Type exit to quit):")

    if userchoice == "exit":
        running = False

    if userchoice in choices:

        computerchoice = random.choice(choices)
        print("\n", userchoice, " vs ", computerchoice)

        if userchoice == computerchoice:
            print("\nIts a Draw !!!\n")

        elif userchoice == "rock" and computerchoice == "paper":
            print("\nPaper beats Rock\n\nComputer Wins !!!\n")

        elif userchoice == "rock" and computerchoice == "scissors":
            print("\nRock beats Scissors\n\n{} Wins !!!\n".format(user))

        elif userchoice == "scissors" and computerchoice == "rock":
            print("\nRock beats Scissors\n\nComputer Wins !!!\n")

        elif userchoice == "scissors" and computerchoice == "paper":
            print("\nScissors beats paper\n\n{} Wins !!!\n".format(user))

        elif userchoice == "paper" and computerchoice == "scissors":
            print("\nScissors beats Paper\n\nComputer Wins !!!\n")

        elif userchoice == "paper" and computerchoice == "rock":
            print("\nPaper beats Rock\n\n{} Wins !!!\n".format(user))

print()
print("*"*100)
print("\nThank You for playing :)\n")
print("*"*100)
print()
