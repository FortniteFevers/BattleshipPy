import os
import time
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'
]

emojis = {
    "empty": "🟦",
    "ship": "🟨",
    "hit": "🟥",
    "miss": "⬜",
    "sunk": "💥"
}

def printboard(board):
    print("  1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣") # Column numbers for the board
    for i, row in enumerate(board):
        print(alphabet[i], end=' ')
        for cell in row:
            print(cell, end=' ')
        print()

def place_ship(board, ship_size):
    while True:
        try:
            start_point = input("Enter the starting point for your ship (e.g., A1): ").upper()
            if start_point[0] not in alphabet or int(start_point[1:]) < 1 or int(start_point[1:]) > 9:
                raise ValueError
            direction = input("Enter the direction for your ship (H for horizontal, V for vertical): ").upper()
            if direction not in ['H', 'V']:
                raise ValueError

            col_index = alphabet.index(start_point[0])
            row_index = int(start_point[1:]) - 1

            if direction == 'H':
                if col_index + ship_size > 9:
                    raise ValueError
                for i in range(ship_size):
                    if board[row_index][col_index + i] != emojis["empty"]:
                        raise ValueError
                for i in range(ship_size):
                    board[row_index][col_index + i] = emojis["ship"]
            else:
                if row_index + ship_size > 9:
                    raise ValueError
                for i in range(ship_size):
                    if board[row_index + i][col_index] != emojis["empty"]:
                        raise ValueError
                for i in range(ship_size):
                    board[row_index + i][col_index] = emojis["ship"]
            break
        except ValueError:
            print("Invalid input! Please try again.")

def check_win(board):
    for row in board:
        for cell in row:
            if cell == emojis["ship"]:
                return False
    return True

def play_game():
    clear()
    print("WELCOME TO BATTLESHIP!\n")
    print("PLAYER 1, LET'S MAKE YOUR BOARD.\n")
    player1_board = [[emojis["empty"] for _ in range(9)] for _ in range(9)]
    for ship_size in [4, 3, 3, 2, 2, 2, 1, 1]:
        printboard(player1_board)
        print(f"Placing a ship of size {ship_size}")
        place_ship(player1_board, ship_size)
        clear()
    print("PLAYER 1 BOARD IS READY!")
    input("Press Enter to continue...")
    clear()
    
    print("PLAYER 2, LET'S MAKE YOUR BOARD.\n")
    player2_board = [[emojis["empty"] for _ in range(9)] for _ in range(9)]
    for ship_size in [4, 3, 3, 2, 2, 2, 1, 1]:
        printboard(player2_board)
        print(f"Placing a ship of size {ship_size}")
        place_ship(player2_board, ship_size)
        clear()
    print("PLAYER 2 BOARD IS READY!")
    input("Press Enter to start the game...")

    clear()
    current_player = 1
    while True:
        if current_player == 1:
            print("PLAYER 1's TURN\n")
            printboard(player2_board)
            target = input("Enter your target (e.g., A1): ").upper()
            row = alphabet.index(target[0])
            col = int(target[1:]) - 1
            if player2_board[row][col] == emojis["ship"]:
                player2_board[row][col] = emojis["hit"]
                print("HIT!")
            else:
                player2_board[row][col] = emojis["miss"]
                print("MISS!")
            if check_win(player2_board):
                print("PLAYER 1 WINS!")
                break
            current_player = 2
        else:
            print("PLAYER 2's TURN\n")
            printboard(player1_board)
            target = input("Enter your target (e.g., A1): ").upper()
            row = alphabet.index(target[0])
            col = int(target[1:]) - 1
            if player1_board[row][col] == emojis["ship"]:
                player1_board[row][col] = emojis["hit"]
                print("HIT!")
            else:
                player1_board[row][col] = emojis["miss"]
                print("MISS!")
            if check_win(player1_board):
                print("PLAYER 2 WINS!")
                break
            current_player = 1
        input("Press Enter to continue...")
        clear()

play_game()
