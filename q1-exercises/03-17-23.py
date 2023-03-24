import random 

# Function that checks if user wansts to play again
def retryGame(inputValue):
        if(inputValue.lower() == 'yes'):
            print("\n" * 10)
            guessingGame()
        else:
            print("\n" * 10)
            print("Goodbye!")
            quit()

# Foundational logic of the guessing game  
def guessingGame():
    random_number = random.randint(1,10) # numbers 1 - 10 
    #random_number = 1
    guess = input("I'm thinking of a number between 1 and 10. What do you think it is?\t")
    guess = int(guess)
    if(guess == random_number):
        print(f"You guessed the number {guess}. The value was {random_number}, you win!\n")
        retry = input("Would you like to play again?(yes or no):\t")
        retryGame(retry)
    elif(guess < 1 or guess > 10):
        print(f"You need to guess a number between 1 amd 10")
        retry = input("Would you like to play again?(yes or no):\t")
        retryGame(retry)
    else:
        print(f"You guessed the number {guess}. The value was {random_number}. Better luck next time!\n")
        retry = input("Would you like to play again?(yes or no):\t")
        retryGame(retry)


guessingGame()