def display_map(player_position, xRange, yRange):
    for i in range(xRange):
        for j in range(yRange):
            if (i, j) == player_position:
                print("P", end=" ")  # Player position
            else:
                print("-", end=" ")  # Empty space
        print()

def move_player(direction, player_position, xRange, yRange):
    x, y = player_position
    if direction == "north":
        x = max(x - 1, 0)
    elif direction == "south":
        x = min(x + 1, xRange-1)
    elif direction == "east":
        y = min(y + 1, yRange-1)
    elif direction == "west":
        y = max(y - 1, 0)
    return x, y

def main():
    print("Welcome to the Map Traverse Game!")
    print("Instructions:")
    print("Move the player 'P' around the map using: north, south, east, west")
    print("Enter 'q' to quit the game.")

    xRange = int(input("Enter how many columns long"))     #could drop a loop to prevent user from entering non-ints

    yRange = int(input("Enter how many rows down"))        #could drop a loop to prevent user from entering non-ints

    player_position = (round(xRange/2), round(yRange/2))   #Initial position
    
    while True:
        print("\nCurrent Map:")
        display_map(player_position,xRange, yRange)
        user_input = input("Enter direction: ").lower()
        if user_input == "q":
            print("Quitting the game.")
            break
        elif user_input in ["north", "south", "east", "west"]:
            player_position = move_player(user_input, player_position, xRange, yRange)
        else:
            print("Invalid direction. Please enter north, south, east, west, or q to quit.")

if __name__ == "__main__":
    main()
