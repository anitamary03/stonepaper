import random

def get_computermove():
    moves = ['rock', 'paper', 'scissors']
    return random.choice(moves)

def get_usermove():
    move = input("ROCK PAPER OR SCISSORS : ")
    while move not in ['rock', 'paper', 'scissors','ROCK','PAPER','SCISSORS']:
        move = input("Invalid move. Please enter rock, paper, or scissors: ")
    return move

def finalpoints(usermove, computermove):
    if usermove == computermove:
        return "tie"
    elif usermove == 'rock' and computermove == 'scissors':
        return "user"
    elif usermove == 'paper' and computermove == 'rock':
        return "user"
    elif usermove == 'scissors' and computermove == 'paper':
        return "user"
    else:
        return "computer"

def playgame(numrounds):
    print("lets play rock paper scissors")
    userscore = 0
    computerscore = 0
    for i in range(1, numrounds+1):
        print(f"\nRound {i}:")
        usermove = get_usermove()
        computermove = get_computermove()
        print(f"You chose {usermove}.")
        print(f"The computer chose {computermove}.")
        winner = finalpoints(usermove, computermove)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            userscore += 1
            print("You win this round!")
        else:
            computerscore += 1
            print("The computer wins this round!")
        print(f"Score: You {userscore} - {computerscore} Computer")
    print("\nGame Over!")
    if userscore > computerscore:
        print("!!! YOU WIN !!!")
    elif computerscore > userscore:
        print("YOU LOSE, COMPUTER WINS")
    else:
        print("GAME TIED")

numrounds = int(input("How many rounds do you want to play?: "))
playgame(numrounds)
