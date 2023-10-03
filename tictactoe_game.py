# Initialize the game board as a list of empty cells
board = ["-" for _ in range(9)]

# Define a function to print the game board
def print_board():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))

# Define a function to get a valid player move
def get_player_move(player):
    while True:
        position = input(f"{player}'s turn. Choose a position from 1-9: ")
        if position.isdigit():
            position = int(position) - 1
            if 0 <= position < 9 and board[position] == "-":
                return position
            else:
                print("Invalid position. Choose a different position.")
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
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    current_player = "X"
    game_over = False

    while not game_over:
        position = get_player_move(current_player)
        board[position] = current_player
        print_board()
        
        game_result = check_game_over()
        if game_result == "win":
            print(f"{current_player} wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

    print("Thank you for playing Tic-Tac-Toe!")

# Start the game
if __name__ == "__main__":
    play_game()
