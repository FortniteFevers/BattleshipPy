import os
import time

def clear():
      os.system('cls' if os.name == 'nt' else 'clear')

Player1_A = [{ # Player 1's actual board. Bottom of deck
    "A": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "B": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "C": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "D": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "E": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "F": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "G": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "H": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "I": ["0", "0", "0", "0", "0", "0", "0", "0", "0"]
}]
Player1_B = [{ # Player 1's documetation of where they fire bombs on the other persons missiles. Top of board,
    "A": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "B": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "C": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "D": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "E": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "F": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "G": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "H": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "I": ["0", "0", "0", "0", "0", "0", "0", "0", "0"]
}]

Player2_A = [{
    "A": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "B": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "C": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "D": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "E": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "F": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "G": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "H": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "I": ["0", "0", "0", "0", "0", "0", "0", "0", "0"]
}]
Player2_B = [{
    "A": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "B": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "C": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "D": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "E": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "F": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "G": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "H": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    "I": ["0", "0", "0", "0", "0", "0", "0", "0", "0"]
}]

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'
]

emojis = [
    {
        "empty": "🟦", # Nothing yet!
        "ship": "🟨", # A players ship is here!
        "hitmissile": "🟥", # A ship has been hit!
        "missedmissile": "⬜" # Missile has been fired, but no ship has been hit!
    }
]

def printboard(listname): # The function to turn a gameboard list into a readable, clear board.
    print("  1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣") # Column numbers for the board
    final = "" # Setup the empty string. The final result will be the full list.
    for x in listname[0]: # Gets values of each row. Row1, Row2, etc
        final += f"{x} "
        data = listname[0]
        for num in range(9):
            final += f"{data[x][num]}"
        final += "\n"
    e = emojis[0]
    final = final.replace("0", e["empty"]).replace( "1", e["ship"]).replace("2", e["hitmissile"]).replace("3", e["missedmissile"]) # Replaces numbers with emojis
    return final # Returns the final string WITH replaced emojis!

def checkforwin():
    """
    PLAN:
    In both A lists, count for each "1" is present. If the count of "1"s is now 0, that means there are no ships left, which means they lost and the other player won
    """

    player1_ships_left = sum(row.count("1") for row in Player1_A[0].values())  # Count occurences of "1" in Player 1s board
    player2_ships_left = sum(row.count("1") for row in Player2_A[0].values())  # Count occurences of"1" in Player 2s board
    #print("Player 1 ships:",player1_ships_left,"Player 2 ships", player2_ships_left)
    if player1_ships_left == 0:
        print("Player 2 wins! All of Player 1's ships have been sunk.")
        return True
    elif player2_ships_left == 0:
        print("Player 1 wins! All of Player 2's ships have been sunk.")
        return True
    else:
        return False

def startgame(player1name, player2name):
    clear() # Could remove for debugging purposes

    i = 0
    while True: # Cycle through player 1 and player 2 endlessly and run checkforwin function until one player wins
        clear() # Could remove for debugging purposes
        print("REMINDER: (⬜) is a MISSED missile and (🟥) is a HIT missile. (🟨) is showing a ship on YOUR board.")

        if i % 2 == 0:
            player = "1" # Number is even, player 1 turn
            print(f'<<< Your move, {player1name} >>>\n') # PLAYER A TURN
            print("YOUR BOARD:")
            print(printboard(Player1_A))
            print("YOUR MOVES:")
            print(printboard(Player1_B))

            while True: # GOING INTO PLAYER 1!!! PLAYER 1_A SHOULD NOT BE EDITED AT ALL
                print("") # New lineeeee :)
                peginput = input(">> ") # Want to seperate into LETTERNUMBER (actual input should be ex. E7)
                try:
                    column_name = peginput[0].upper() # Letter column (ex: E)
                    row_number = int(peginput[-1]) - 1 # The row num (ex: 7)
                    Player1_B[0][column_name][row_number] = "3" # SHOW THE MISSILE ON A BOARD B MISSED
                    print("MISSILE FIRED!!!")
                    time.sleep(.5)

                    if Player2_A[0][column_name][row_number] == "1": # Checks to see if piece is already occupied. If it is, let the user know.
                        Player1_B[0][column_name][row_number] = "2" # Indicates that theres a ship there
                        Player2_A[0][column_name][row_number] = "2" # HIT MISSILE
                        print("\nITS A HIT!")

                        print("\nYour updated moves:")
                        print(printboard(Player1_B))

                        print("Enter another input to keep your streak going!\n")
                        continue
                    else:
                        print("\nITS A MISS!")
                        Player2_A[0][column_name][row_number] = "3" # MISSED (showing on player 2 board)

                        print("Your updated moves:")
                        print(printboard(Player1_B))
                

                    print("\nPlayer 1 has made their move. Moving onto player 2 in 3 seconds...")
                    time.sleep(3)
                    break
                except:
                    print("Enter a valid input! (Example: E7)\n")
                    continue

        else:
            player = "2" # Number is odd, player 2 turn
            print(f'<<< Your move, {player2name} >>>\n')
            print("YOUR BOARD:")
            print(printboard(Player2_A))
            print("YOUR MOVES:")
            print(printboard(Player2_B))

            while True: # GOING INTO PLAYER 1!!! PLAYER 2_A SHOULD NOT BE EDITED AT ALL
                print("") # New lineeeee :)
                peginput = input(">> ") # Want to seperate into LETTERNUMBER (actual input should be ex. E7)
                try:
                    column_name = peginput[0].upper() # Letter column (ex: E)
                    row_number = int(peginput[-1]) - 1 # The row num (ex: 7)
                    Player2_B[0][column_name][row_number] = "3" # SHOW THE MISSILE ON A BOARD B MISSED
                    print("MISSILE FIRED!!!")
                    time.sleep(.5)

                    if Player1_A[0][column_name][row_number] == "1": # Checks to see if piece is already occupied. If it is, let the user know.
                        Player2_B[0][column_name][row_number] = "2" # Indicates that theres a ship there
                        Player1_A[0][column_name][row_number] = "2" # HIT MISSILE
                        print("\nITS A HIT!")

                        print("\nYour updated moves:")
                        print(printboard(Player1_B))

                        print("Enter another input to keep your streak going!\n")
                        continue
                    else:
                        print("\nITS A MISS!")
                        Player1_A[0][column_name][row_number] = "3" # MISSED (showing on player 2 board)

                        print("Your updated moves:")
                        print(printboard(Player2_B))
                

                    print("\nPlayer 2 has made their move. Moving onto player 2 in 3 seconds...")
                    time.sleep(3)
                    break
                except:
                    print("Enter a valid input! (Example: E7)\n")
                    continue

        
        i += 1

        if checkforwin():  # Call the checkforwin() function after each player's turn
            break
    exit()

def createboard():
    #BEGIN PLAYER 1:
    print("Player 1, let's make your board.\n")
    print(printboard(Player1_A))
    for i in range(2): # 4-PEG (x2)
        while True:
            print(f"Enter your starting point for a 4-PEG ship ({i+1}/2)")
            peginput = input(">> ")
            try:
                column_name = peginput[0].upper() # Letter column (ex: E)
                row_number = int(peginput[-1]) - 1 # The row num (ex: 7)
                colnum = alphabet.index(column_name) # Finds the index for the number 

                if Player1_A[0][column_name][row_number] == "1": # Checks to see if piece is already occupied. If it is, let the user know.
                    print("Ship already exists in the selected positions! Choose a new starting point.\n")
                    continue
                break
            except:
                print("Enter a valid input! (Example: E7)\n")
                continue
            
        while True:
            print("\nWould you like to move up (U), down (D), left (L), or right (R)?")
            move = input(">> ").upper()
            Player1_A[0][column_name][row_number] = "1"
            try:
                if move == "U":
                    if column_name == "D" or column_name == "C" or column_name == "B" or column_name == "A":
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player1_A[0][alphabet[colnum-1]][row_number] = "1"
                    Player1_A[0][alphabet[colnum-2]][row_number] = "1"
                    Player1_A[0][alphabet[colnum-3]][row_number] = "1"
                elif move == "D":
                    if column_name == "F" or column_name == "G" or column_name == "H" or column_name == "I":
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player1_A[0][alphabet[colnum+1]][row_number] = "1"
                    Player1_A[0][alphabet[colnum+2]][row_number] = "1"
                    Player1_A[0][alphabet[colnum+3]][row_number] = "1"
                elif move == "L":
                    if row_number <= 4:
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player1_A[0][column_name][row_number-1] = "1"
                    Player1_A[0][column_name][row_number-2] = "1"
                    Player1_A[0][column_name][row_number-3] = "1"
                elif move == "R":
                    if row_number >= 6:
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player1_A[0][column_name][row_number+1] = "1"
                    Player1_A[0][column_name][row_number+2] = "1"
                    Player1_A[0][column_name][row_number+3] = "1"
                else:
                    print("Ship does not place here! Please chose a new starting point or orientation.")
                    continue
                print(printboard(Player1_A))
                break
            except:
                print("Ship does not place here! Please chose a new starting point or orientation.")
                continue

    for i in range(3): # 3-PEG (3x)
        while True:
            print(f"Enter your starting point for a 3-PEG ship ({i+1}/3)")
            peginput = input(">> ")
            try:
                column_name = peginput[0].upper() # Letter column (ex: E)
                row_number = int(peginput[-1]) - 1 # The row num (ex: 7)
                colnum = alphabet.index(column_name)

                if Player1_A[0][column_name][row_number] == "1": # Checks to see if piece is already occupied. If it is, let the user know.
                    print("Ship already exists in the selected positions! Choose a new starting point.\n")
                    continue
                break
            except:
                print(f"Enter a valid input! (Example: E7)\n")
                continue
            
        while True:
            print("\nWould you like to move up (U), down (D), left (L), or right (R)?")
            move = input(">> ").upper()
            Player1_A[0][column_name][row_number] = "1"
            try:
                if move == "U":
                    if column_name == "C" or column_name == "B" or column_name == "A":
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player1_A[0][alphabet[colnum-1]][row_number] = "1"
                    Player1_A[0][alphabet[colnum-2]][row_number] = "1"
                elif move == "D":
                    if column_name == "G" or column_name == "H" or column_name == "I":
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player1_A[0][alphabet[colnum+1]][row_number] = "1"
                    Player1_A[0][alphabet[colnum+2]][row_number] = "1"
                elif move == "L":
                    if row_number < 3:
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player1_A[0][column_name][row_number-1] = "1"
                    Player1_A[0][column_name][row_number-2] = "1"
                elif move == "R":
                    if row_number > 7:
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player1_A[0][column_name][row_number+1] = "1"
                    Player1_A[0][column_name][row_number+2] = "1"
                else:
                    print("Ship does not place here! Please chose a new starting point or orientation.")
                    continue
                print(printboard(Player1_A))
                break
            except:
                print("Ship does not place here! Please chose a new starting point or orientation.")
                continue

    for i in range(1): # 2-PEG (1x)
        while True:
            print(f"Enter your starting point for a 2-PEG ship ({i+1}/1)")
            peginput = input(">> ")
            try:
                column_name = peginput[0].upper() # Letter column (ex: E)
                row_number = int(peginput[-1]) - 1 # The row num (ex: 7)
                colnum = alphabet.index(column_name)

                if Player1_A[0][column_name][row_number] == "1": # Checks to see if piece is already occupied. If it is, let the user know.
                    print("Ship already exists in the selected positions! Choose a new starting point.\n")
                    continue
                break
            except:
                print("Enter a valid input! (Example: E7)\n")
                continue
            
        while True:
            print("\nWould you like to move up (U), down (D), left (L), or right (R)?")
            move = input(">> ").upper()
            Player1_A[0][column_name][row_number] = "1"
            try:
                if move == "U":
                    if column_name == "B" or column_name == "A":
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player1_A[0][alphabet[colnum-1]][row_number] = "1"
                elif move == "D":
                    if column_name == "H" or column_name == "I":
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player1_A[0][alphabet[colnum+1]][row_number] = "1"
                elif move == "L":
                    if row_number <= 2:
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player1_A[0][column_name][row_number-1] = "1"
                elif move == "R":
                    if row_number >= 8:
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player1_A[0][column_name][row_number+1] = "1"
                else:
                    print("Ship does not place here! Please chose a new starting point or orientation.")
                    continue
                print(printboard(Player1_A))
                break
            except:
                print("Ship does not place here! Please chose a new starting point or orientation.")
                continue

    for i in range(2): # 1-PEG (1x)
        while True:
            print(f"Enter your starting point for a 1-PEG ship ({i+1}/2)")
            peginput = input(">> ")
            try:
                column_name = peginput[0].upper() # Letter column (ex: E)
                row_number = int(peginput[-1]) - 1 # The row num (ex: 7)
                colnum = alphabet.index(column_name)

                if Player1_A[0][column_name][row_number] == "1": # Checks to see if piece is already occupied. If it is, let the user know.
                    print("Ship already exists in the selected positions! Choose a new starting point.\n")
                    continue
                break
            except:
                print("Enter a valid input! (Example: E7)\n")
                continue

        Player1_A[0][column_name][row_number] = "1"
        print(printboard(Player1_A))
            
    print("\nPlayer 1 has succesfully made their board!\nClearing terminal for player 2 in 5 seconds...")
    time.sleep(5)
    clear()

    # NEED TO ADD ALREADY PLACED CODE HERE
    """
    SWITCH TO PLAYER 2
    """

    print("Player 2, let's make your board.\n")
    print(printboard(Player2_A))
    for i in range(2): # 4-PEG (x2)
        while True:
            print(f"Enter your starting point for a 4-PEG ship ({i+1}/2)")
            peginput = input(">> ")
            try:
                column_name = peginput[0].upper() # Letter column (ex: E)
                row_number = int(peginput[-1]) - 1 # The row num (ex: 7)
                colnum = alphabet.index(column_name)

                if Player2_A[0][column_name][row_number] == "1": # Checks to see if piece is already occupied. If it is, let the user know.
                    print("Ship already exists in the selected positions! Choose a new starting point.\n")
                    continue

                break
            except:
                print("Enter a valid input! (Example: E7)\n")
                continue
            
        while True:
            print("\nWould you like to move up (U), down (D), left (L), or right (R)?")
            move = input(">> ").upper()
            Player2_A[0][column_name][row_number] = "1"
            try:
                if move == "U":
                    if column_name == "D" or column_name == "C" or column_name == "B" or column_name == "A":
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player2_A[0][alphabet[colnum-1]][row_number] = "1"
                    Player2_A[0][alphabet[colnum-2]][row_number] = "1"
                    Player2_A[0][alphabet[colnum-3]][row_number] = "1"
                elif move == "D":
                    if column_name == "F" or column_name == "G" or column_name == "H" or column_name == "I":
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player2_A[0][alphabet[colnum+1]][row_number] = "1"
                    Player2_A[0][alphabet[colnum+2]][row_number] = "1"
                    Player2_A[0][alphabet[colnum+3]][row_number] = "1"
                elif move == "L":
                    if row_number <= 4:
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player2_A[0][column_name][row_number-1] = "1"
                    Player2_A[0][column_name][row_number-2] = "1"
                    Player2_A[0][column_name][row_number-3] = "1"
                elif move == "R":
                    if row_number >= 6:
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player2_A[0][column_name][row_number+1] = "1"
                    Player2_A[0][column_name][row_number+2] = "1"
                    Player2_A[0][column_name][row_number+3] = "1"
                else:
                    print("Ship does not place here! Please chose a new starting point or orientation.")
                    continue
                print(printboard(Player2_A))
                break
            except:
                print("Ship does not place here! Please chose a new starting point or orientation.")
                continue

    for i in range(3): # 3-PEG (3x)
        while True:
            print(f"Enter your starting point for a 3-PEG ship ({i+1}/3)")
            peginput = input(">> ")
            try:
                column_name = peginput[0].upper() # Letter column (ex: E)
                row_number = int(peginput[-1]) - 1 # The row num (ex: 7)
                colnum = alphabet.index(column_name)

                if Player2_A[0][column_name][row_number] == "1": # Checks to see if piece is already occupied. If it is, let the user know.
                    print("Ship already exists in the selected positions! Choose a new starting point.\n")
                    continue

                break
            except:
                print("Enter a valid input! (Example: E7)\n")
                continue
            
        while True:
            print("\nWould you like to move up (U), down (D), left (L), or right (R)?")
            move = input(">> ").upper()
            Player2_A[0][column_name][row_number] = "1"
            try:
                if move == "U":
                    if column_name == "C" or column_name == "B" or column_name == "A":
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player2_A[0][alphabet[colnum-1]][row_number] = "1"
                    Player2_A[0][alphabet[colnum-2]][row_number] = "1"
                elif move == "D":
                    if column_name == "G" or column_name == "H" or column_name == "I":
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player2_A[0][alphabet[colnum+1]][row_number] = "1"
                    Player2_A[0][alphabet[colnum+2]][row_number] = "1"
                elif move == "L":
                    if row_number < 3:
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player2_A[0][column_name][row_number-1] = "1"
                    Player2_A[0][column_name][row_number-2] = "1"
                elif move == "R":
                    if row_number > 7:
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player2_A[0][column_name][row_number+1] = "1"
                    Player2_A[0][column_name][row_number+2] = "1"
                else:
                    print("Ship does not place here! Please chose a new starting point or orientation.")
                    continue
                print(printboard(Player2_A))
                break
            except:
                print("Ship does not place here! Please chose a new starting point or orientation.")
                continue

    for i in range(1): # 2-PEG (1x)
        while True:
            print(f"Enter your starting point for a 2-PEG ship ({i+1}/1)")
            peginput = input(">> ")
            try:
                column_name = peginput[0].upper() # Letter column (ex: E)
                row_number = int(peginput[-1]) - 1 # The row num (ex: 7)
                colnum = alphabet.index(column_name)

                if Player2_A[0][column_name][row_number] == "1": # Checks to see if piece is already occupied. If it is, let the user know.
                    print("Ship already exists in the selected positions! Choose a new starting point.\n")
                    continue

                break
            except:
                print("Enter a valid input! (Example: E7)\n")
                continue
            
        while True:
            print("\nWould you like to move up (U), down (D), left (L), or right (R)?")
            move = input(">> ").upper()
            Player2_A[0][column_name][row_number] = "1"
            try:
                if move == "U":
                    if column_name == "B" or column_name == "A":
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player2_A[0][alphabet[colnum-1]][row_number] = "1"
                elif move == "D":
                    if column_name == "H" or column_name == "I":
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player2_A[0][alphabet[colnum+1]][row_number] = "1"
                elif move == "L":
                    if row_number <= 2:
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player2_A[0][column_name][row_number-1] = "1"
                elif move == "R":
                    if row_number >= 8:
                        print("Ship does not place here! Please chose a new starting point or orientation.")
                        continue
                    Player2_A[0][column_name][row_number+1] = "1"
                else:
                    print("Ship does not place here! Please chose a new starting point or orientation.")
                    continue
                print(printboard(Player2_A))
                break
            except:
                print("Ship does not place here! Please chose a new starting point or orientation.")
                continue

    for i in range(2): # 1-PEG (1x)
        while True:
            print(f"Enter your starting point for a 1-PEG ship ({i+1}/2)")
            peginput = input(">> ")
            try:
                column_name = peginput[0].upper() # Letter column (ex: E)
                row_number = int(peginput[-1]) - 1 # The row num (ex: 7)
                colnum = alphabet.index(column_name)

                if Player2_A[0][column_name][row_number] == "1": # Checks to see if piece is already occupied. If it is, let the user know.
                    print("Ship already exists in the selected positions! Choose a new starting point.\n")
                    continue

                break
            except:
                print("Enter a valid input! (Example: E7)\n")
                continue

        Player2_A[0][column_name][row_number] = "1"
        print(printboard(Player2_A))
            
    print("\nPlayer 2 has succesfully made their board!")
    time.sleep(1)
    clear()
    print("Both players have created their boards. Clearing terminal and starting the game in 5 seconds...")
    print("\n!!! ONLY PLAYER 1 SHOULD BE LOOKING AT THE COMPUTER SCREEN! IT IS PLAYER 1s TURN COMING UP !!!")
    time.sleep(5)
    clear()
    return


def main():
    print("LET'S GET YOUR NAMES.\n")
    time.sleep(1)
    print("PLAYER 1, ENTER YOUR NAME.")
    player1name = input(">> ")
    time.sleep(1)
    print("\nPLAYER 2, ENTER YOUR NAME.")
    player2name = input(">> ")
    time.sleep(1)
    print(f"\nWelcome, {player1name} and {player2name}. GOOD LUCK SOLDIERS.")
    time.sleep(1)
    print(
         f"""
Directions:
- Before we start the game, both players will create their game boards.
- Player 1 ({player1name}) will go first. Player 2 ({player2name}) will go second.
- The game consists of two boards, 9x9. You will have 8 ships total.
- EACH PLAYER WILL HAVE:  2x FOUR SHIPS, 3x THREE SHIPS, 1x TWO SHIPS, 2x ONE SHIP
- You can place your ships anywhere on the board. They can not be touching eachother. They can not be diagonal. They can not be overlapping another ship.
- Have fun :)
        """
    )
    time.sleep(3)
    print("Player 1, MAKE YOUR BOARD!!!")
    time.sleep(1)
    clear()
    createboard() # Creates both Player 1 and Player 2s game boards
    startgame(player1name, player2name) # Once the program has created both Player 1 and Player 2 (A) boards it starts the game

clear()
print(
    """
                  WELCOME TO...\n
    ____        __  __  __          __    _
   / __ )____ _/ /_/ /_/ /__  _____/ /_  (_)___
  / __  / __ `/ __/ __/ / _ \/ ___/ __ \/ / __ |
 / /_/ / /_/ / /_/ /_/ /  __(__  ) / / / / /_/ /
/_____/\__,_/\__/\__/_/\___/____/_/ /_/_/ .___/
                                       /_/

    """
)
time.sleep(1)
main()
