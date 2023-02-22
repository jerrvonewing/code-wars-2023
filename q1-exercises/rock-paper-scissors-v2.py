import random

print("Rock...")
print("Papers...")
print("Scissors...")

def rock_paper_scissors(player1, player2):
    # Player 1 Selects Rock
    if(player1 == "rock"):
        if(player2 == "scissors"):
            print("Player 1 wins! You rock!")
        elif(player2 == "paper"):
            print("Player 2 wins!")
        elif(player2 == "rock"):
            print("It's a draw!")
        else:
            print("Someone didn't pick rock, paper, or scissors...")
        return
    # Player 1 Selects Paper
    elif(player1 == "paper"):
        if(player2 == "scissors"):
            print("Player 2 wins!")
        elif(player2 == "rock"):
            print("Player 1 wins!")
        elif(player2 == "paper"):
            print("It's a draw!")
        else: 
            print("Someone didn't pick rock, paper, or scissors...")
        return
    # Player 1 Selects Scissors
    elif(player1 == "scissors"):
        if(player2 == "scissors"):
            print("It's a draw!")
        elif(player2 == "rock"):
            print("Player 2 wins! You rock!")
        elif(player2 == "paper"):
            print("Player 1 wins!")
        else: 
            print("Someone didn't pick rock, paper, or scissors...")
        return
    else:
        exit()

choices = ["rock","paper","scissors"]
player1 = input("Player 1: Make your move:\t")
while player1 != "quit":
    player2 = random.choice(choices)
    rock_paper_scissors(player1, player2)
    player1 = input("Player 1: Make your move:\t")
    if player1 == "quit":
        exit()
