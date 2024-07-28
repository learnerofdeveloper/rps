import random

while True:
    print("\n")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
    selection = int(input("Enter Throw (1-3): "))

    if selection == 1:
        player_throw = "Rock"
    elif selection == 2:
        player_throw = "Paper"
    elif selection == 3:
        player_throw = "Scissors"
    else:
        print("Invalid selection, please choose 1, 2, or 3.")
        continue

    print("\n")
    print("Player picks", player_throw)

    throws = ["Rock", "Paper", "Scissors"]
    ai_throw = random.choice(throws)

    print("AI throws", ai_throw)

    if player_throw == ai_throw:
        print("Tie Game")
    elif player_throw == "Rock":
        if ai_throw == "Paper":
            print("AI Wins")
        else:
            print("Player Wins")
    elif player_throw == "Paper":
        if ai_throw == "Scissors":
            print("AI Wins")
        else:
            print("Player Wins")
    elif player_throw == "Scissors":
        if ai_throw == "Rock":
            print("AI Wins")
        else:
            print("Player Wins")

    print("\n")
    print("1) Play Again")
    print("2) Quit")
    selection = int(input("Enter Choice (1-2): "))

    if selection == 2:
        break
    elif selection != 1:
        print("Please enter 1 to continue and 2 to exit")
        while selection != 1 or selection != 2:
            selection = int(input("Enter Choice (1-2): "))
    else:
        continue

    if selection == 2:
        break
            


