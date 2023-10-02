# Initialize the game board as a list of empty cells
board = ["-" for _ in range(9)]

# Define a function to print the game board
def print_board():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))

# Define a function to handle a player's turn
def take_turn(player):
    print(player + "'s turn.")
    while True:
        position = input("Choose a position from 1-9: ")
        if position.isdigit() and 1 <= int(position) <= 9:
            position = int(position) - 1
            if board[position] == "-":
                board[position] = player
                break
            else:
                print("Position already taken. Choose a different position.")
        else:
            print("Invalid input. Choose a position from 1-9.")

# Define a function to check if the game is over
def check_game_over():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "-":
            return "win"

    if "-" not in board:
        return "tie"

    return "play"

# Define the main game loop
def play_game():
    print_board()
    current_player = "X"
    game_over = False

    while not game_over:
        take_turn(current_player)
        print_board()
        game_result = check_game_over()

        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
