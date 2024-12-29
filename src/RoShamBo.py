from random import choice

def main():
    print("Welcome to RoShamBo!")
    player = input("Enter [Rock, Paper, Scissors]: ").capitalize()
    choose = ["Rock", "Paper", "Scissors"]
    Ai = choice(choose)

    print(f"You chose {player} and the AI chose {Ai}")

    if player == Ai:
        print("It's a tie!")
    elif player == "Paper":
        if Ai == "Rock":
            print("You win!")
        else:
            print("You lose!")
    elif player == "Scissors":
        if Ai == "Paper":
            print("You win!")
        else:
            print("You lose!")
    elif player == "Rock":
        if Ai == "Scissors":
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    main()
