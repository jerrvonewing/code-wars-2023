print("Rock...")
print("Papers...")
print("Scissors...")

player1 = input("Player 1: Make your move:\t")
player2 = input("Player 2: Make your move:\t")

def rock_paper_scissors(player1, player2):
    if(player1 == "rock" and player2 == "paper"):
        print("Player 2 wins!")
        return
    elif(player1 == "paper" and player2 == "rock"):
        print("Player 1 wins!")
        return
    elif(player1 == "scissors" and player2 == "paper"):
        print("Player 1 wins!")
        return
    elif(player1 == "paper" and player2 == "scissors"):
        print("Player 2 wins!")
        return
    elif(player1 == "rock" and player2 == "scissors"):
        print("Player 1 wins! You rock!")
        return
    elif(player1 == "scissors" and player2 == "rock"):
        print("Player 2 wins! You rock!")
        return
    elif(player1 == player2):
        print("It's a draw!")
        return
    else:
        print("Someone didn't pick rock, paper, or scissors...")
        return

rock_paper_scissors(player1, player2)