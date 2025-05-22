def treasure_island_game():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    # First decision
    choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
    if choice1 != "left":
        print("You fall into a hole. Game Over.")
        return

    # Second decision
    choice2 = input("You come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if choice2 != "wait":
        print("You are attacked by trout. Game Over.")
        return

    # Third decision
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue.\nWhich door do you choose? ").lower()
    if choice3 == "red":
        print("Burned by fire. Game Over.")
    elif choice3 == "blue":
        print("Eaten by beasts. Game Over.")
    elif choice3 == "yellow":
        print("You Win!")
    else:
        print("Game Over.")

# Start the game
treasure_island_game()
