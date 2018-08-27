import random

game = input("Do you wanna play RPS? Yes (y) or no (n)?")


while game == "y":
    
    player = input("Choose rock (r) paper (p) or scissors (s):")

    computer = random.randint(1,3)
    ploop = str()
    if computer == 1:
        ploop = "r";
    if computer == 2:
        ploop = "p";
    if computer == 3:
        ploop = "s";

    if player == ploop:
        if player == "r":
            print("Computer got rock, too. Tie.")
        if player == "p":
            print("Computer got paper, too. Tie.")
        if player == "s":
            print("Computer got scissors, too. Tie.")

    if player == "r" and computer == 2:
        print("Computer got paper.")
        print("You lose.")

    if player == "r" and computer == 3:
        print("Computer got scissors.")
        print("You win!")

    if player == "p" and computer == 1:
        print("Computer got rock.")
        print("You win!")

    if player == "p" and computer == 3:
        print("Computer got scissors.")
        print("You lose.")


    if player == "s" and computer == 2:
        print("Computer got paper.")
        print("You win!")

    if player == "s" and computer == 1:
        print("Computer got rock.")
        print("You lose.")

    again = input("Do you wanna play again? Yes (y) or no (n)?")
    if again == "y":
        game = "y"
    if again == "n":
        crap = input("Are you sure? Yes (y) or no (n)?")
        if crap == "y":
            game = "bitch"
        if crap == "n":
            bloop = input("Do you wanna play a game? Yes (y) or no (n)?")
            if bloop == "y":
                game = "y"
            if bloop == "n":
                game = "bitch"
            
            
    else:
        print("Invalid answer.")
        
if game == "n":
    sure = input("Are you sure? Yes (y) or no (n)?")
    if sure == "y":
        print("Bye.")
    if sure == "n":
        clap = input("Do you wanna play RPS? Yes (y) or no (n)?")
        if clap == "y":
            game = "y"
        if clap == "n":
            print("Bye.")
            
if game == "bitch":
    print("Bye.")

else:
    print("Invalid answer.")





